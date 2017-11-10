# -*- coding: utf-8 -*-
# Module: Smart
# Author: CvA
# Created on: 10.11.2017

import requests

data = requests.get("https://explorer.smartcash.cc/api/getdifficulty")

difficulty = data.content.decode()
test = float(difficulty)
test2 = float(105000)

log = open("SmartDiff", "w")
if test < test2:
    mine = "YES"
else:
    mine = "NO"
log.write(mine)
log.close()

test2 = data
