"""
# PS_CLI (ps_cli)
This package provides various utility functions splitted by modules for [Python](https://python.org) to work wih command line interface
"""


import subprocess, os, sys, re, zipfile, datetime, ps_funcs
import xml.dom.minidom as mdom
from . import args
from . import table
from . import dialog
from . import env

#import functools as env

__all__=[args, table, dialog,
env,
]
