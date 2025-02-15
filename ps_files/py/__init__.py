#! /usr/bin/env python3
__version__="1.0.0"
__author__="Serj.by"
__doc__ = """
Doc updated for v1.0.0
ps_files module brings suuport of various file formats
Currently supported:
fb2 : [Fiction Book 2](https://en.m.wikipedia.org/wiki/FictionBook) - popular eBook format
mp3 (partly)
"""

from ps_files.formats import fb2

__all__=['PS_FileFormat', 'fb2', 'mp3']


__readme__=\
'''
##List of colors available in three main modules (fg, bg, colors):
Links leads to the color description on Wikipedia since GH md syntax is not allow to use colors in docs:
<a href='https://en.m.wikipedia.org/wiki/Black'>Black</a>

<a href='https://en.m.wikipedia.org/wiki/Red'>Red</a>

<a href='https://en.m.wikipedia.org/wiki/Green'>Green</a>

<a href='https://en.m.wikipedia.org/wiki/Yellow'>Yellow</a>

<a href='https://en.m.wikipedia.org/wiki/Blue'>Blue</a>

<a href='https://en.m.wikipedia.org/wiki/Magenta'>Magenta</a>

<a href='https://en.m.wikipedia.org/wiki/Cyan'>Cyan</a>

<a href='https://en.m.wikipedia.org/wiki/White'>White</a>

<a href='https://en.m.wikipedia.org/wiki/Gray'>Gray</a>

<a href='https://en.m.wikipedia.org/wiki/BrightRed'>BrightRed</a>

<a href='https://en.m.wikipedia.org/wiki/BrightGreen'>BrightGreen</a>

<a href='https://en.m.wikipedia.org/wiki/BrightYellow'>BrightYellow</a>

<a href='https://en.m.wikipedia.org/wiki/BrightBlue'>BrightBlue</a>

<a href='https://en.m.wikipedia.org/wiki/BrightMagenta'>BrightMagenta</a>

<a href='https://en.m.wikipedia.org/wiki/BrightCyan'>BrightCyan</a>

<a href='https://en.m.wikipedia.org/wiki/BrightWhite'>BrightWhite</a>


'''

#if (__name__=="__main__"):
#	print ("in init_main")
#	f= fb2.fb2("testfrominit")
#	print ("fn from obj:", f.getFilename())
#else:
#	print("in ps_files.__init__ not __main__ but ", __name__)

