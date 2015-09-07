#!/usr/bin/env python

import flask

from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

def cachebust():
	return str(time.time())

app.add_template_global(cachebust)

projects = [
	{ "name":"Report UI", "image":"https://farm3.staticflickr.com/2897/14727605844_f98b00c09d.jpg", "tags": ["drawing","ui","ux"], "path": "report-ui.html" },
	{ "name":"The Lord of the Rings", "image":"http://farm7.static.flickr.com/6066/6110880278_e415427101.jpg", "tags":["fun","drawing"], "path": "tlor.html" },
	{ "name":"App design", "image":"https://farm4.staticflickr.com/3911/15021186471_4f4850d94e.jpg", "tags":["ui","ux"], "path": "careapp.html" },
	{ "name":"Welcome", "image":"http://farm7.static.flickr.com/6081/6110337919_f6f7c9a70f.jpg", "tags":["drawing"], "path": "welcome.html" },
	{ "name":"Rose", "image":"http://farm7.static.flickr.com/6063/6110882438_100f76818e.jpg", "tags":["drawing"], "path": "rose.html" },
	{ "name":"Halloween", "image":"http://farm7.static.flickr.com/6083/6110886390_9a2ae69c10.jpg", "tags":["drawing"], "path": "halloween.html" },
	{ "name":"clock", "image":"http://farm7.static.flickr.com/6188/6110336375_f6471b7804.jpg", "tags":["drawing"], "path": "clock.html" },
	{ "name":"Sakura", "image":"http://farm7.static.flickr.com/6206/6110884458_c6c4d97ab8.jpg", "tags":["drawing"], "path": "sakura.html" },
	{ "name":"Qubit Platform", "image":"https://farm4.staticflickr.com/3903/14551308727_aa5053200c.jpg", "tags":["ui","ux"], "path": "qubit-platform.html" },
	{ "name":"Rammo Jammo", "image":"https://farm6.staticflickr.com/5565/14726685291_37aa464ae2.jpg", "tags":["drawing"], "path": "rammo-jammo.html" },
	{ "name":"Running Guinea", "image":"https://farm4.staticflickr.com/3900/14737122085_58cd5e7cac.jpg", "tags":["drawing"], "path": "running-guinea.html" },
	{ "name":"Qubit Lab", "image":"https://farm4.staticflickr.com/3835/14558662919_084df87767.jpg", "tags":["ui","ux"], "path": "qubit-lab.html" },
	{ "name":"Motilo", "image":"https://farm6.staticflickr.com/5574/14722042416_7793c71601.jpg", "tags":["ui","ux"], "path": "motilo.html" },
	{ "name":"Podcast app", "image":"https://farm3.staticflickr.com/2935/14706972606_a51887d5e2.jpg", "tags":["ui","ux"], "path": "podcast.html" },
	{ "name":"Tool website", "image":"https://farm4.staticflickr.com/3843/14729690842_9a3c349744.jpg", "tags":["ui","ux"], "path": "tools-website.html" },
	{ "name":"Tool", "image":"https://farm4.staticflickr.com/3863/14543329258_a698f8b97d.jpg", "tags":["ui","ux"], "path": "tool.html" },
	{ "name":"Opentag", "image":"https://farm4.staticflickr.com/3859/14543328228_b017133a2d.jpg", "tags":["ui","ux"], "path": "opentag.html" },
	{ "name":"E-motion", "image":"http://farm5.static.flickr.com/4085/4992555539_01e8397ef5.jpg", "tags":["product-design""interactive"], "path": "emotion.html" },
	{ "name":"No more NFL", "image":"https://farm8.staticflickr.com/7330/16237209187_a0c5454112.jpg", "tags":["ui","product-design"], "path": "nomorenfl.html" },
	{ "name":"Lemonaid", "image":"http://farm2.static.flickr.com/1101/5111828846_a271eb722e.jpg", "tags":["interactive"], "path": "lemonaid.html" },
	{ "name":"BarkBuddy", "image":"https://farm4.staticflickr.com/3912/14818480780_2be8601792.jpg", "tags":["ui","ux"], "path": "barkbuddy.html" },
	{ "name":"3d2d", "image":"http://farm5.static.flickr.com/4083/4992594515_4f7b681095.jpg", "tags":["interactive","art"], "path": "3d2d.html" },
	{ "name":"Snowflake", "image":"http://farm7.static.flickr.com/6184/6095092752_367cf66be0.jpg", "tags":["product-design"], "path": "snowflake.html" },
	{ "name":"Stickers for BarkCam", "image":"https://farm1.staticflickr.com/255/19618362893_72ceccaa94_b.jpg", "tags":["drawing", "ui"], "path": "barkcam-stickers.html" },
	{ "name":"HeartB", "image":"http://farm7.static.flickr.com/6197/6098079165_a2fc82a952.jpg", "tags":["product-design","interactive"], "path": "heartb.html" },
	{ "name":"Medusa light", "image":"http://farm2.static.flickr.com/1333/5131921939_4dbf91d3e2.jpg", "tags":["product-design"], "path": "medusalight.html" },
	{ "name":"Horizon lighting design", "image":"http://farm7.static.flickr.com/6187/6095234284_3fce146b1b.jpg", "tags":["product-design"], "path": "horizon-lighting-design.html" },
	{ "name":"Dancing Shoes", "image":"http://farm7.static.flickr.com/6192/6098494544_4e7af4fa1f.jpg", "tags":["interactive"], "path": "dancing-shoes.html" },
	{ "name":"I.S.Share", "image":"http://farm2.static.flickr.com/1374/5112293133_f303d1e0a7.jpg", "tags":["product-design","ui","ux"], "path": "isshare.html" },
	{ "name":"W3C website design", "image":"https://farm4.staticflickr.com/3850/14765356503_4776f725ff.jpg", "tags":["ui","ux"], "path": "w3c-tool.html" },
	{ "name":"Han Xu", "image":"http://farm7.static.flickr.com/6083/6101874914_f39c5e9c45.jpg", "tags":["product-design"], "path": "hanxu.html" },
	{ "name":"BarkCam", "image":"https://farm4.staticflickr.com/3857/14947059405_9d75a86c17.jpg", "tags":["product-design","ui","ux"], "path": "barkcam.html" },
	{ "name":"Tabula Rasa", "image":"http://farm6.static.flickr.com/5135/5415961689_9beb9d7627.jpg", "tags":["product-design","ui","ux"], "path": "tabularasa.html" },
	{ "name":"Shapes", "image":"https://farm4.staticflickr.com/3841/14749506623_3c98fe9ebf.jpg", "tags":["art"], "path": "shapes.html" },
	{ "name":"BarkPost app", "image":"https://farm1.staticflickr.com/559/20052270090_d9d64e2134_z.jpg", "tags":["product-design","ui","ux"], "path": "barkpost-app.html" },
]

links = {}
for i,l in enumerate(projects):
	links[l["path"]] = {
		"prev": "/projects/" + projects[(i + 1) % len(projects)]["path"],
		"next": "/projects/" + projects[(i - 1) % len(projects)]["path"],
	}

related = {}
for p in projects:
	rel = []
	for rp in projects:
		if p == rp:
			continue
		if len(set(p["tags"]).intersection(set(rp["tags"]))) > 0:
			rel.append(rp)
	related[p["path"]] = rel

print related.keys()

@app.route('/')
def main1():
    return render_template("index.html", **{
    	"works": projects,
    })

@app.route('/<path>')
def main2(path):
	return render_template(path)

@app.route('/projects/<path>')
def project(path):
	c = {}
	if path in links:
		c['next'] = links[path]['next']
		c['prev'] = links[path]['prev']
	if path in related:
		c['related'] = related[path]

	template = "/projects/%s" % path
	return render_template(template, **c)

app.debug = True
app.run()
