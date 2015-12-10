#!/usr/bin/env python
import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect
from os import environ

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


import os
import sys
import json
import hashlib

app = Flask(__name__, static_folder="templates/static")
GoogleMaps(app)
app.debug = True

db = shelve.open("map.db")

@app.route('/')
def load_root():
    return flask.render_template('index.html')

@app.route('/upload')
def upload():
    return flask.render_template('upload.html')
'''
def load_file(name=None):
    url = 'public_html/upload.html'
    f = open(url, 'r')
    raw_data = f.read()
    return raw_data
    '''

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route("/map",methods=['POST'])
def mapview():
	mapData = request.form.get('mappoints')
	mapData = eval(mapData)
	print mapData

    # creating a map in the view
	sndmap = Map(
		identifier="sndmap",
		lat= 39.5,
		lng= -98.35,
		zoom = 3,
		style = "height: 100%; width: 100%; top:0; left:0; position:absolute; z-index:200",
		markers= {'http://maps.google.com/mapfiles/ms/icons/green-dot.png': mapData}
	)

	urlData = request.form.get('short')
	if urlData not in db:
		db[urlData] = render_template('map.html', sndmap=sndmap)

	return render_template('map.html', sndmap=sndmap)

@app.route("/<url>", methods=['GET'])
def load_redirect(url):
    """
    Redirect the request to the URL associated =short=, otherwise return 404
    NOT FOUND
    """
    print url

    if url in db:
        return db[url]
    else:
        #return render_template('404.html'),404
        abort(404)

if __name__ == "__main__":
    app.run()