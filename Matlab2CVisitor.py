#！ /usr/bin/python3

from antlr4 import *
import json

if __name__ is not None and "." in __name__:
    from .MatlabParser import MatlabParser
    from .MatlabVisitor import MatlabVisitor
else:
    from MatlabParser import MatlabParser
    from MatlabVisitor import MatlabVisitor


class Matlab2CVisitor(MatlabVisitor):
    def __init__(self, log:bool = False):
        self.func_rtype = dict()
        self.log = log
        self.route = list() 
        # return variable, must be pointer
        self.ret_var = list() 
        self.para_list = list() 
        self.func_name = str()
        
        self.__load_conf()
        
    
    def __load_conf(self):
        func_rtype_path = './mxx/create_semaphore_type.json'

        with open(func_rtype_path, 'r') as f:
            self.func_rtype = json.load(f)

    def visitFunction(self, ctx:MatlabParser.FunctionContext):
        self.route.append('Function')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.function_declare():
            self.visitFunction_declare(ctx.function_declare())
            # print(ctx.function_declare())
        if ctx.statement():
            self.visitStatement(ctx.statement())
            # print(ctx.statement().getText())
        self.route.pop()

    def visitFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        self.route.append('Function_declare')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        # visit return_params 
        if ctx.returnparas():
            self.ret_var = self.visitReturnparas(ctx.returnparas())
            print(self.ret_var)
        # visit paralist
        if ctx.paralist():
            self.para_list = self.visitParalist(ctx.paralist())
            print(self.para_list)
        # visit name
        if ctx.name():
            self.func_name = self.visitName(ctx.name())
            print(self.func_name)
        
        self.route.pop()

    def visitName(self, ctx:MatlabParser.NameContext):
        self.route.append('Name')
        '''
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        '''
        name = str()
        if ctx.NAME():
            name = ctx.NAME()
        self.route.pop()
        return name

    def visitReturnparas(self, ctx:MatlabParser.ReturnparasContext):
        self.route.append('Returnparas')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        # print(len(ctx.return_name()))
        ret_var = list()
        for i in range(len(ctx.return_name())):
            ret_var.append(ctx.return_name(i).getText())
            # print(ctx.return_name(i).getText())
        self.route.pop()
        return ret_var

    def visitParalist(self, ctx:MatlabParser.ParalistContext):
        self.route.append('Paralist')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        
        # print(len(ctx.expr()))
        paralist = []
        for i in range(len(ctx.expr())):
            paralist.append(ctx.expr(i).getText())
            # print(ctx.expr(i).getText())
        self.route.pop()
        return paralist