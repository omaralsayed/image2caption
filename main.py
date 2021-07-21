from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from transformers import ViTFeatureExtractor, ViTForImageClassification, \
    AutoModelWithLMHead, AutoTokenizer

from PIL import Image
import requests

app = FastAPI()

def generate_caption(model, tokenizer, concepts, max_length=32):
    input_text = concepts

    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], 
                attention_mask=features['attention_mask'],
                max_length=max_length)

    return tokenizer.decode(output[0])

@app.post('/upload/')
async def image2caption(image_url: str = Form(...)):
    image = Image.open(requests.get(image_url, stream=True).raw)

    feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-large-patch32-384')
    model = ViTForImageClassification.from_pretrained('google/vit-large-patch32-384')

    inputs = feature_extractor(images=image, return_tensors='pt')
    outputs = model(**inputs)
    logits = outputs.logits

    predicted_class_idx = logits.argmax(-1).item()
    classes = model.config.id2label[predicted_class_idx]
    classes = list(classes.split(','))

    model = AutoModelWithLMHead.from_pretrained('mrm8488/t5-base-finetuned-common_gen')
    tokenizer = AutoTokenizer.from_pretrained('mrm8488/t5-base-finetuned-common_gen')

    return generate_caption(model, tokenizer, ' '.join(classes))

@app.get('/')
async def main():
    content = \
    '''
        <body>
        <form action='/upload/' method='post'>
        <input type='image_url' name='image_url'>
        <input type='submit'>
        </form>
        </body>
    '''

    return HTMLResponse(content=content)
