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
parser.add_argument('-i', '--input', dest='input', required=True, help='input file')
args = parser.parse_args()


def main():
    instream = FileStream(args.input)
    matlab_lexer = MatlabLexer(instream)
    token_stream = CommonTokenStream(matlab_lexer)
    matlab_parser = MatlabParser(token_stream)
    
    tree = matlab_parser.function()

    cvtor = Matlab2CVisitor(log=args.log)
    cvtor.visit(tree) 
    if args.log:
        pass
if __name__ == '__main__':
    main()

