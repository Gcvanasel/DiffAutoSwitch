# -*- coding: utf-8 -*-
# Module: Solaris
# Author: CvA
# Created on: 10.11.2017

import requests

data = requests.get("https://solaris.blockexplorer.pro/api/getdifficulty")

difficulty = data.content.decode()
test = float(difficulty)
test2 = float(45)

log = open("SolarisDiff", "w")
if test < test2:
    mine = "YES"
else:
    mine = "NO"
log.write(mine)
log.close()
