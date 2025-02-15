"""
# PS_ZIP (ps_zip)
This module provides various utility functions for [Python](https://python.org) to work wih zip files
"""


import subprocess, os, sys, re, zipfile, datetime, ps_funcs
import xml.dom.minidom as mdom

def getZipInfo (filename:str, confident:bool=True)->dict|None:
    rx=r"^(?P<filename>.+?\.zip)(:(#(?P<nmb>\d+))|(?P<arcfilename>[^#]+))?$"
    print ("filename in zipinfo:", filename)
    print ("rx for zipinfo:", rx)
    m=re.search (rx, filename)
    print ("m:", m, "mtype:", type(m))