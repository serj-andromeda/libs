#! /usr/bin/env python3

import sys, ps_files, shcolar

fn = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.fb2"
fn2 = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_2.fb2"
fnm = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_mod.fb2"
fnm2 = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_mod2.fb2"

if len(sys.argv)>=2:
	if sys.argv[1]=="2":
		fn=fn2
	elif sys.argv[1]=="m":
		fn=fnm
	elif sys.argv[1]=="m2":
		fn=fnm2

fb2=ps_files.formats.fb2.fb2 ()
fb2.setFilename (fn)
c=fb2.getContent()
print ("type of c b4 read:", type(c))
fb2.readFile(dontDecode=True, isBinFile=False)
print ("type of c aft read but bef getcontent:", type(c))
c=fb2.getContent()
print ("type of c aft getcontent:", type(c))
print (shcolar.bold(shcolar.empty)+"First 300 chars of content: "+shcolar.reset, c[:300], sep="\n")
fb2.parse()
#print ("-"*10+"\n", "mdxml_elems dict:", fb2.mdxml_elems)
print ("@@@genre lst:", fb2.get_genre_lst())
print ("@@@suthors lst:", fb2.get_author_lst())

fb2.set_str_includes_annotation_bool (True)
#fb2.add_author_str ("test author")
#fb2.add_genre_str ("test genre")
print (shcolar.underline(shcolar.empty)+"book info:"+shcolar.reset, "\n", fb2, sep="")
