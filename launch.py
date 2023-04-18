import pandas as pd
import numpy as np
import torch
import cloudpickle
import torch
from PIL import Image 
import os
import base64
import requests
from io import BytesIO


def loadmodel(logger):
    """Get model from cloud object storage."""
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model  

def preprocessing(features,logger):
    """ Applies preprocessing techniques to the raw data"""
    logger.info("no preprocessing required")
    return False
    
def predict(features,model,logger):
    """Predicts the results for the given inputs"""
    logger.info("model prediction")

    def url_to_img(url):
        """
        Convert Url to PIL Image
        : param url : string with the link to the image
        : return : PIL Image object
        """
        response = requests.get(url)
        return Image.open(BytesIO(response.content))


    def img_to_bytes(img):
        """
        Convert PIL image to base64
        :param img : PIL Image object
        :return string : image in the form of base64
        """
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        return img_str.decode("utf-8")
     # Inference
    img = url_to_img(features)
    results = model(img) 
    results.render()
    return img_to_bytes(Image.fromarray(results.ims[0]))