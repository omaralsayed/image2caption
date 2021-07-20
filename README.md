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
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/pdf/2010.11929.pdf) by Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby.
- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf) by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.
