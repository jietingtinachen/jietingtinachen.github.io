#!/usr/bin/env python

import flask

from flask import Flask
from flask import render_template

app = Flask(__name__)

order = [
	"/projects/report-ui.html",
	"/projects/tlor.html",
	"/projects/welcome.html",
	"/projects/rose.html",
	"/projects/halloween.html",
	"/projects/clock.html",
	"/projects/sakura.html",
	"/projects/qubit-platform.html",
	"/projects/rammo-jammo.html",
	"/projects/running-guinea.html",
	"/projects/qubit-lab.html",
	"/projects/motilo.html",
	"/projects/podcast.html",
	"/projects/tools-website.html",
	"/projects/tool.html",
	"/projects/opentag.html",
	"/projects/emotion.html",
	"/projects/lemonaid.html",
	"/projects/3d2d.html",
	"/projects/snowflake.html",
	"/projects/heartb.html",
	"/projects/medusalight.html",
	"/projects/horizon-lighting-design.html",
	"/projects/dBn.html",
	"/projects/isshare.html",
	"/projects/w3c-tool.html",
	"/projects/hanxu.html",	
	"/projects/tabularasa.html",
	
	
	
	
	
	
	
	
	
	
	
	
	
	


	
	
	
	
	
	
	

	
	
	
	

]
links = {}
for i,l in enumerate(order):
	links[l] = {
		"prev": order[(i + 1) % len(order)],
		"next": order[(i - 1) % len(order)],
	}

@app.route('/')
def main1():
    return render_template("main.html")

@app.route('/<path>')
def main2(path):
	return render_template(path)

@app.route('/projects/<path>')
def project(path):
	path = "/projects/%s" % path
	c = {}
	if path in links:
		c['next'] = links[path]['next']
		c['prev'] = links[path]['prev']
	return render_template(path, **c)

app.debug = True
app.run()
