#!/bin/bash

rm -r projects
mkdir static
mkdir projects
curl http://127.0.0.1:5000/index.html -o index.html
curl http://127.0.0.1:5000/about.html -o about.html
curl http://127.0.0.1:5000/projects/report-ui.html -o projects/report-ui.html
curl http://127.0.0.1:5000/projects/tlor.html -o projects/tlor.html
curl http://127.0.0.1:5000/projects/welcome.html -o projects/welcome.html
curl http://127.0.0.1:5000/projects/rose.html -o projects/rose.html
curl http://127.0.0.1:5000/projects/halloween.html -o projects/halloween.html 
curl http://127.0.0.1:5000/projects/clock.html -o projects/clock.html
curl http://127.0.0.1:5000/projects/sakura.html -o projects/sakura.html
curl http://127.0.0.1:5000/projects/qubit-platform.html -o projects/qubit-platform.html
curl http://127.0.0.1:5000/projects/rammo-jammo.html -o projects/rammo-jammo.html
curl http://127.0.0.1:5000/projects/running-guinea.html -o projects/running-guinea.html 
curl http://127.0.0.1:5000/projects/qubit-lab.html -o projects/qubit-lab.html
curl http://127.0.0.1:5000/projects/motilo.html -o projects/motilo.html
curl http://127.0.0.1:5000/projects/podcast.html -o projects/podcast.html
curl http://127.0.0.1:5000/projects/tools-website.html -o projects/tools-website.html
curl http://127.0.0.1:5000/projects/tool.html -o projects/tool.html
curl http://127.0.0.1:5000/projects/opentag.html -o projects/opentag.html
curl http://127.0.0.1:5000/projects/emotion.html -o projects/emotion.html
curl http://127.0.0.1:5000/projects/lemonaid.html -o projects/lemonaid.html
curl http://127.0.0.1:5000/projects/barkbuddy.html -o projects/barkbuddy.html
curl http://127.0.0.1:5000/projects/3d2d.html -o projects/3d2d.html
curl http://127.0.0.1:5000/projects/snowflake.html -o projects/snowflake.html
curl http://127.0.0.1:5000/projects/heartb.html -o projects/heartb.html
curl http://127.0.0.1:5000/projects/medusalight.html -o projects/medusalight.html
curl http://127.0.0.1:5000/projects/horizon-lighting-design.html -o projects/horizon-lighting-design.html
curl http://127.0.0.1:5000/projects/dancing-shoes.html -o projects/dancing-shoes.html
curl http://127.0.0.1:5000/projects/isshare.html -o projects/isshare.html
curl http://127.0.0.1:5000/projects/w3c-tool.html -o projects/w3c-tool.html
curl http://127.0.0.1:5000/projects/hanxu.html -o projects/hanxu.html
curl http://127.0.0.1:5000/projects/barkcam.html -o projects/barkcam.html
curl http://127.0.0.1:5000/projects/tabularasa.html -o projects/tabularasa.html
curl http://127.0.0.1:5000/projects/shapes.html -o projects/shapes.html

cp -R source/static/ static/
