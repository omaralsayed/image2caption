# Image2Caption
Vision Transformer (ViT) + Text-to-Text Transfer Learning Transformer (T5) to Caption Images.

## Requirements
Python 3.6+

## Installation
```sh
git clone https://github.com/omaralsayed/image2caption.git
cd image2caption
pip install -r requirements.txt
uvicorn main:app --reload
```

## Resources
(https://huggingface.co/transformers/)[Hugging Face Documentation]
(https://arxiv.org/pdf/2010.11929.pdf)[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale] by Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby.
(https://arxiv.org/pdf/1910.10683.pdf)[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer] by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.
