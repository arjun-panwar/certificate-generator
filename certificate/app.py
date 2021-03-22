# doing necessary imports

from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS,cross_origin
import requests
from urllib.request import urlopen as uReq
#import pymongo
import csv
from flask_cors import CORS,cross_origin
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

app = Flask(__name__)


def homePage():
    return render_template("index.html")

@app.route('/',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()

def index():
    if request.method == 'POST':

        email = request.form['content'].replace(" ", "")  # obtaining the search string entered in the form
        try:
            df = pd.read_csv('list.csv')
            df.set_index("email", inplace=True)
            try:
                #name=df.Title[email].strip()+" "+df["First Name"][email].strip()+" "+df["Last Name"][email].strip()
                name="PIL is the Python Imaging Library which provides the python interpreter \n with image editing capabilities. The ImageDraw module provide simple 2D graphics for Image objects. You can use this module to create new images,\n annotate or retouch existing images, and to generate graphics on the fly for web use."
                font = ImageFont.truetype('LibreBaskerville-Regular.ttf', 20)
                #for index, j in df.iterrows():
                img = Image.open('certificate.jpg')
                draw = ImageDraw.Draw(img)
                image_width = img.width
                image_height = img.height
                text_width, _ = draw.textsize(name, font=font)

                draw.multiline_text(xy=((image_width - text_width) / 2, 560), text='{}'.format(name), fill=(0, 0, 0),font=font,spacing=0, align="center")
                pdf = img.convert('RGB')
                os.remove("static/pictures/certificate.pdf")
                pdf.save('static/pictures/certificate.pdf')
                return render_template('results.html', result=name)
            except:
                return render_template('index.html', result="Email address not found!! Enter a valid email address!!")

        except Exception as e:
                print('The Exception message is: ', e)
                return 'something is wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(port=8028, debug=True)  # running the app on the local machine on port 8000
    app.run(debug=True)
