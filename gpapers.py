#!/usr/bin/env python

import urllib.request 

# https://earthview.withgoogle.com/download/2037.jpg

for i in range(1, 2037):
    try:
        urllib.request.urlretrieve("http://earthview.withgoogle.com/download/{}.jpg".format(i), "{}.jpg".format(i))
    except:
        print("{} not found...".format(i))
