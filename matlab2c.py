#! /usr/bin/python3

from antlr4 import *
import sys
from antlr4.InputStream import InputStream
from MatlabLexer import MatlabLexer
from MatlabParser import MatlabParser
from Matlab2CVisitor import Matlab2CVisitor

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log', dest='log', action='store_true', help='whether print visitor info')
args = parser.parse_args()

from conf import mstar_path, mtype_path

def main():
    instream = FileStream(mstar_path)
    matlab_lexer = MatlabLexer(instream)
    token_stream = CommonTokenStream(matlab_lexer)
    matlab_parser = MatlabParser(token_stream)
    
    tree = matlab_parser.function()

    cvtor = Matlab2CVisitor(log=args.log, func_type_path=mtype_path)
    func_expr = cvtor.visit(tree)

    print(func_expr.toStr())

    if args.log:
        pass
if __name__ == '__main__':
    main()

