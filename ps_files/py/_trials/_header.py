import xml.dom.minidom as mdom
import zipfile, re
import ps_funcs, ps_zip, shcolar

fn1 = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.fb2"

fn2 = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_2.fb2"
fnm = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_mod.fb2"
fnz = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.zip"
winfnzwn = "c:/books/fb2.zip:#0"
fnzwn = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2.zip:#0"
fnzwan = "/data/data/com.termux/files/home/dev/_data/files4tests/fb2_an.zip:fb2_an.fb2"

rxfn="(?P<fn>.+)(?P<ext>\\.zip|\\.fb2)(:(#(?P<nmb>\\d+))|(?P<arcfn>[^#]+))?$"
fn_lst=[fn1, fn2, fnm, fnz, winfnzwn, fnzwn, fnzwan, ]
fn_names_lst=["fn1", "fn2", "fnm", "fnz", "winfnzwn", "fnzwn", "fnzwan",]
fn_dict={n: globals()[n] for n in fn_names_lst}
