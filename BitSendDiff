# -*- coding: utf-8 -*-
# Module: Smart
# Author: CvA
# Created on: 10.11.2017

import requests

data = requests.get("https://chainz.cryptoid.info/bsd/api.dws?q=getdifficulty")

difficulty = data.content.decode()
test = float(difficulty)
test2 = float(90)

log = open("BitSendDiff", "w")
if test < test2:
    mine = "YES"
else:
    mine = "NO"
log.write(mine)
log.close()

test2 = data
