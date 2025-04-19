"""
Intended to work with csv/tsv files. Mainly designed for copy/paste tsv's from Wiki
Unlike native `csv` modul includes few additional dialects and functuons to make dev easier
"""
import os, sys, re, csv

import ps_funcs, ps_shcolar


def dialect_print(dialect: csv.Dialect):
        """
        @ps Based on #src: https://wellsr.com/python/introduction-to-csv-dialects-with-the-python-csv-module/#Formatting
        Prints out all relevant formatting parameters of a dialect
        """
        print(
            "delimiter = %s\n"
            "doublequote = %s\n"
            "escapechar = %s\n"
            "lineterminator = %s\n"
            "quotechar = %s\n"
            "skipinitialspace = %s\n" % (
                repr(dialect.delimiter), dialect.doublequote, dialect.escapechar,
                repr(dialect.lineterminator), dialect.quotechar,
                dialect.skipinitialspace))


class wiki_copypaste_dialect (csv.Dialect):
	delimiter = '\t'
	doublequote = True
	escapechar = None
	lineterminator = '\n'
	quotechar = '"'
	quoting = csv.QUOTE_MINIMAL
	skipinitialspace = True
	strict = False
	
def register_dialects ():
	csv.register_dialect ('wiki_copypaste', wiki_copypaste_dialect)






register_dialects()