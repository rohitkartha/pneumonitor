from urllib import response
from flask import Blueprint, redirect, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return  render_template("base.html")


@views.route('/tool', methods=["POST", "GET"])
def tool():
    if request.method == "POST":

        file = request.files["file"]
        print(file.filename)
        

    return  render_template("tool.html")

  