#! /usr/bin/env python3
from _header import *
print ("test fn1:", shcolar.fg.brightGreen+fn1+shcolar.fg.reset)
print ("test fn2:", shcolar.fg.brightGreen+fn2+shcolar.fg.reset)
print ("test fnz:", shcolar.fg.brightGreen+fnz+shcolar.fg.reset)
print ("test fnzwn:", shcolar.fg.brightGreen+fnzwn+shcolar.fg.reset)
print ("test fnzwan:", shcolar.fg.brightGreen+fnzwan+shcolar.fg.reset)
exit()

def isZipFile (filename:str, reqFullConfidence:bool=True)->bool:
	m=re.match(rxfn, filename)
	return m is not None


def getNodeAttributes_lst (node:mdom.Node)->list:
	"""
	Get list of node attributes in form of tuples (name, value) like in DOM
	"""
	return node.attributes.items()
	
def printXML(node:mdom.Node, lvl:int=0, indent_per_lvl_int:int=2, max_lvl_int=1000, indent_char_str=" ", includeTopNode=True):
	xml_str = xml(**locals())
	print (xml_str if xml_str is not None else "@---")

def xml(node:mdom.Node, lvl:int=0, indent_per_lvl_int:int=2, max_lvl_int=1000, indent_char_str=" ", includeTopNode=True)->str:
	if lvl>=max_lvl_int:
		print ("@@@Exit by reaching limit")
		return ""
	indent_chars_n_int=lvl*indent_per_lvl_int
	data_str="???"
	close_data_str=None
	goDeep=False
	match node.nodeType:
		case node.ELEMENT_NODE:
			data_str="<"+node.tagName+" "+ps_funcs.getNodeAttrs_str(node)+">"
			close_data_str="</"+node.tagName+">"
			goDeep=True
		case node.TEXT_NODE:
			data_str="\""+node.nodeValue+"\""
		case _:
			data_str="@unknown node type "+str(node.nodeType)+" for node "+str(node)
	print (indent_char_str*indent_chars_n_int, data_str, sep="")
	if goDeep and len(node.childNodes)>0:
		for cn in node.childNodes:
			printXML(cn, lvl+1)
		if lvl==0:
			print ("#@@Exit because of end of top level node reached")
	print (close_data_str if close_data_str is not None else "", end="" if close_data_str is None else "\n")


mode=1

mode_name="unknown"
match mode:
	case 1:
		fn=fn1
		mode_name="simple"
	case 2:
		fn=fn2
		mode_name="mode_2"
	case 3:
		fn=fnm
		mode_name="modified"
	case 4:
		fn=fnz
		mode_name="zip"
	case _:
		fn=fn
		mode_name="fallback to simple due to unknown mode "+str(mode)
	
print ("Starting xmltest with mode '"+shcolar.fg.brightWhite+mode_name+shcolar.reset+"'")




doc=mdom.parse(fn)
root=doc.documentElement
body_lst=root.getElementsByTagName("body")
body_el=[el for el in body_lst if el.attributes.get("name") is None][0]
notes_el=[el for el in body_lst if el.attributes.get("name") is not None and el.attributes.get("name").value=="notes"][0]
desc_el=ps_funcs.getChildByTagName(root, "description")
titleinfo_el=ps_funcs.getChildByTagName(desc_el, "title-info")
annotation_el=ps_funcs.getChildByTagName(titleinfo_el, "annotation")
sequence_el=ps_funcs.getChildByTagName(titleinfo_el, "sequence")
printXML(desc_el)
ps_funcs.press_enter()