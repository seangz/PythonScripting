#!/bin/python

import os

stage = os

stage = (os.getenv("STAGE") or "development").upper()

output = "We're running %s" % stage

if stage.startswith("PROD"):
    output = "DANGER !!! - " + output
    
print(output)