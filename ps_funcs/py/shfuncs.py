"""
Module with functions related to shell functionality
like executing shell commands, return it,s results, error codes etc
"""
import os, sys, subprocess

def backtick (cmd: str, dir: str|None=None):
        """
Execute command in shell and return result like backtick in shell and PHP
:param cmd: command to execute
:type cmd: str
:returns: what command cmd sends to stdout (basically just output of command)
:rtype: str
        """
        cp=subprocess.run(cmd, shell=True, capture_output=True);

        ba=cp.stdout;
        res=ba.decode('utf-8');
        return res;
def system (cmd: str)->int:
        """
        Exec cmd and return exit code
        """
        return os.system(cmd)