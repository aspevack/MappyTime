#!/usr/bin/env python
import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect, url_for
from os import environ
from werkzeug import secure_filename

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


import os
import sys
import json
import hashlib

UPLOAD_FOLDER = 'uploads'
allowed_extensions = set(['csv'])

app = Flask(__name__, static_folder="templates/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
GoogleMaps(app)
app.debug = True

db = shelve.open("map.db")

@app.route('/')
def load_root():
    return flask.render_template('index.html')

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit('.',1)[1] in allowed_extensions

@app.route('/upload')
def upload():
    return flask.render_template('upload.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route("/map",methods=['POST'])
def map():
    mapData = request.form.get('mappoints')
    mapData = mapData.split("),(")
    for i in range(len(mapData)):
        mapData[i] = mapData[i].strip(')').strip('(')
        mapData[i]=mapData[i].split(',')
        mapData[i][0]=float(mapData[i][0])
        mapData[i][1]=float(mapData[i][1])
    print mapData


    urlData = request.form.get('short')
    if urlData not in db:
        db[urlData] = render_template('map.html', urldata= urlData, mapData=mapData)
    return render_template('map.html',urldata= urlData, mapData=mapData)
    

'''
def upload_file():
    if request.method == 'POST':
        file = request.files['fileToUpload']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print os.path   
            print os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            '''


@app.route("/<url>", methods=['GET'])
def load_redirect(url):
    print url
    if url in db:
        return db[url]
    else:
        #return render_template('404.html'),404
        abort(404)

if __name__ == "__main__":
    app.run()