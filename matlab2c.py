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

import time

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log', dest='log', action='store_true', 
    help='whether print visitor info')
args = parser.parse_args()

arinc_struct = dict()

from conf import mstar_dir, cvt_file, arinc_struct_conf_path, cpath, cvt_module

def convert_code(mstar_path: str, mtype_path: dict):
    instream = FileStream(mstar_path)
    matlab_lexer = MatlabLexer(instream)
    token_stream = CommonTokenStream(matlab_lexer)
    matlab_parser = MatlabParser(token_stream)


    tree = matlab_parser.function()

    cvtor = Matlab2CVisitor(log=args.log, func_type_=mtype_path,
        arinc_struct=arinc_struct)
    func_expr = cvtor.visit(tree)

    func_declare = func_expr.Deps[0]


    if args.log:
        pass
    
    return [func_declare.toStr(), func_expr.toStr()]


def generate_c_header(module_name : str, funcs : list) -> str:
    module_name = module_name.upper()

    res = str()
    res += '#ifndef __L_' + module_name + '_H\n'
    res += '#define __L_' + module_name + '_H\n'

    res += '\n'

    for func in funcs:
        res += func + ';\n\n'

    res += '\n' + '#endif\n'
    
    return res

def generate_c_body(module_name : str, body : list) -> str:
    module_name = module_name.lower()

    res = str()
    res += '#include < %s >\n' % module_name

    res += '\n'
    for bd in body:
        res += bd + '\n'

    return res


def main():
    ms_dir_list = os.listdir(mstar_dir)
    cur_path = os.path.abspath(mstar_dir)
    c_dir = os.path.abspath(cpath)

    # load arinc_struct
    with open(arinc_struct_conf_path, 'r') as f:
        global arinc_struct
        arinc_struct = json.load(f)
    
    for path in ms_dir_list:
        if path.endswith('.json'):
            continue
        
        if path not in cvt_module:
            continue
        
        module_name = path
        module_path = os.path.join(cur_path, path)
        file_list = os.listdir(module_path)

        module_c_file = os.path.join(c_dir, module_name)
        module_h_file = module_c_file
        module_c_file += '.c'
        module_h_file += '.h'

        mcf = open(module_c_file, 'w')
        mhf = open(module_h_file, 'w')

        module_conf = dict() 
        # load module type conf fn
        for fn in file_list:
            if fn.endswith('.json'):
                mc_path = os.path.join(module_path, fn)
                with open(mc_path, 'r') as f:
                    module_conf = json.load(f)
            
        print('converting', module_name, '...')

        header_func_declare = list()
        module_func_body = list()

        for fn in file_list:
            if fn.endswith('.json'):
                continue
            
            fn = fn.strip('.m')
            lfn = fn.lower()

            if lfn not in cvt_file:
                print('!!! not in', lfn)
                continue
            
            if lfn not in module_conf:
                print(lfn)
                print(module_conf)
                assert lfn in module_conf
            
            func_type = module_conf[lfn]
            
            mfn = os.path.join(module_path, fn + '.m')
            # print(mfn)
            ticks = time.time()
            cvt_res = convert_code(mfn, func_type)
            cost_time = time.time() - ticks
            print('\t%s -> %.2f ms' % (fn, cost_time * 1000))
            # print('\t', fn,'->',cost_time * 1000, 'ms')
            
            module_func_body.append(cvt_res[1])
            header_func_declare.append(cvt_res[0])

        mhf.write(generate_c_header(module_name, header_func_declare))
        mcf.write(generate_c_body(module_name, module_func_body))

        mhf.close()
        mcf.close()
            

    
if __name__ == '__main__':
    main()

