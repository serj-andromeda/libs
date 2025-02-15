#! /usr/bin/env python3
import xml.dom.minidom as mdom
import ps_funcs as psf, zipfile
import ps_funcs

fn = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.fb2"
fn2 = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_2.fb2"
fnm = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_mod.fb2"
fnz = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.zip"
fnmc = "/data/data/com.termux/files/home/dev/_data/files4tests/test_mc.ext"



mode=1


def getNodeAttributes_lst (node:mdom.Node)->list:
	"""
	 Get list of node attributes in form of tuples (name, value) like in DOM
	 """
	return node.attributes

def printXML(node:mdom.Node, lvl:int=0, indent_per_lvl_int:int=2, max_lvl_int=1000, indent_char_str=" "):
	if lvl>=max_lvl_int:
		print ("@@@Exit by reaching limit")
		return
	indent_chars_n_int=lvl*indent_per_lvl_int
#	print ("@ntl:", node, type(node), lvl)
	data_str="???"
	close_data_str=None
	goDeep=False
	match node.nodeType:
		case node.ELEMENT_NODE:
			data_str="<"+node.tagName+"@"+ps_funcs.getNodeAttrs_str(node)+"/#"+">"
			close_data_str="</"+node.tagName+">"
			goDeep=True
		case node.TEXT_NODE:
			data_str="\""+node.nodeValue+"\""
		case _:
			data_str="@unknown node type "+str(node.nodeType)+" for node "+str(node)
	print (indent_char_str*indent_chars_n_int, data_str, sep="")
	if goDeep:
		for cn in node.childNodes:
			printXML(cn, lvl+1)
		if lvl==0:
			print ("@@#Exit because of end of top level node reached")
	print (close_data_str if close_data_str is not None else "", end="" if close_data_str is None else "\n")




mode_name="unknown"
match mode:
	case 1:
		fn=fn
		mode_name="simple"
	case _:
		fn=fn
		mode_name="fallback to simple due to unknown mode "+str(mode)
	
print ("Starting xmltest with mode", mode_name)




doc=mdom.parse(fn)
root=doc.documentElement
body_lst=root.getElementsByTagName("body")
body_el=[el for el in body_lst if el.attributes.get("name") is None][0]
notes_el=[el for el in body_lst if el.attributes.get("name") is not None and el.attributes.get("name").value=="notes"][0]
desc_el=psf.getChildByTagName(root, "description")
titleinfo_el=psf.getChildByTagName(desc_el, "title-info")
annotation_el=psf.getChildByTagName(titleinfo_el, "annotation")
printXML(desc_el)
ps_funcs.press_enter()