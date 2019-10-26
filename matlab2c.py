#! /usr/bin/python3

from antlr4 import *
import sys
from antlr4.InputStream import InputStream
from MatlabLexer import MatlabLexer
from MatlabParser import MatlabParser
from Matlab2CVisitor import Matlab2CVisitor

import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log', dest='log', action='store_true', 
    help='whether print visitor info')
args = parser.parse_args()

arinc_struct = dict()

from conf import mstar_dir, cvt_file, arinc_struct_conf_path

def convert_code(mstar_path: str, mtype_path: dict):
    instream = FileStream(mstar_path)
    matlab_lexer = MatlabLexer(instream)
    token_stream = CommonTokenStream(matlab_lexer)
    matlab_parser = MatlabParser(token_stream)


    tree = matlab_parser.function()

    cvtor = Matlab2CVisitor(log=args.log, func_type_=mtype_path,
        arinc_struct=arinc_struct)
    func_expr = cvtor.visit(tree)

    print(func_expr.toStr())

    if args.log:
        pass
    

    
def main():
    ms_dir_list = os.listdir(mstar_dir)
    cur_path = os.path.abspath(mstar_dir)
    
    # load arinc_struct
    with open(arinc_struct_conf_path, 'r') as f:
        global arinc_struct
        arinc_struct = json.load(f)
    
    for path in ms_dir_list:
        if path.endswith('.json'):
            continue
        
        module_path = os.path.join(cur_path, path)
        file_list = os.listdir(module_path)
       
        module_conf = dict() 
        # load module type conf fn
        for fn in file_list:
            if fn.endswith('.json'):
                mc_path = os.path.join(module_path, fn)
                with open(mc_path, 'r') as f:
                    module_conf = json.load(f)
            
         
        for fn in file_list:
            if fn.endswith('.json'):
                continue
            
            fn = fn.strip('.m')
            lfn = fn.lower()

            if lfn not in cvt_file:
                continue
            
            assert lfn in module_conf
            func_type = module_conf[lfn]
            
            mfn = os.path.join(module_path, fn + '.m')
            # print(mfn)
             
            convert_code(mfn, func_type)
            

    
if __name__ == '__main__':
    main()

