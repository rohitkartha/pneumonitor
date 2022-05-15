from urllib import response
from flask import Blueprint, redirect, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
from resnet.model_v1 import ResBlock, ResNet18
import torch

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return  render_template("base.html")


@views.route('/tool', methods=["POST", "GET"])
def tool():
    if request.method == "POST":
        img_size = 150
        file = request.files["file"]
        imgobj = Image.open(file)
        new_img = imgobj.resize((img_size, img_size))
        new_img = np.asarray(new_img, dtype=np.float32)
        arr = new_img.reshape((1, img_size, img_size, 1))
        arr /= 255.0
        tensor_arr = torch.Tensor(arr)
        print(tensor_arr)

        model = ResNet18(150, ResBlock, 1)
        model.load_state_dict(torch.load('resnet\myFirstModel.pth'))

        output = model.forward(tensor_arr)
        print("Output: ", output)

        if (output > 0.5):
            status = "pneumonia"
            return  render_template("pneumonia.html")

        else:
            status = "normal"
            return  render_template("normal.html")



    


        
        


        

    return  render_template("tool.html")

  