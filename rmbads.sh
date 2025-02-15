#! /usr/bin/env bash
find . -name py -type l -exec rmfile.py {} \;
find . -name __pycache__ -type d -exec rmfile.py {} \;
find . -name testrmbad.dummy.txt -type f -exec rmfile.py {} \;
