#！ /usr/bin/python3

from antlr4 import *
import json
from expr import *
        

if __name__ is not None and "." in __name__:
    from .MatlabParser import MatlabParser
    from .MatlabVisitor import MatlabVisitor
else:
    from MatlabParser import MatlabParser
    from MatlabVisitor import MatlabVisitor


class Matlab2CVisitor(MatlabVisitor):
    def __init__(self, log:bool = False):
        self.all_var_type = dict()
        self.log = log
        self.route = list() 
        # return variable, must be pointer
        self.ret_var = list() 
        self.para_list = list() 
        self.global_list = list()
        self.func_name = str()
        
        self.__load_conf()
        
    
    def __load_conf(self):
        func_rtype_path = './mxx/create_semaphore_type.json'

        with open(func_rtype_path, 'r') as f:
            self.all_var_type = json.load(f)

    def visitFunction(self, ctx:MatlabParser.FunctionContext):
        self.route.append('Function')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.function_declare():
            func_declare = self.visitFunction_declare(ctx.function_declare())
            # print(ctx.function_declare())
        if ctx.statement():
            state = self.visitStatement(ctx.statement())
            # print(ctx.statement().getText())
        self.route.pop()

    def visitFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        self.route.append('Function_declare')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        # visit return_params 
        if ctx.returnparas():
            ret_var = self.visitReturnparas(ctx.returnparas())
            print('ret_val:', ret_var)
        # visit paralist
        if ctx.paralist():
            self.para_list = self.visitParalist(ctx.paralist())
            print('para_list:', self.para_list)
        # visit name
        if ctx.name():
            self.func_name = self.visitName(ctx.name())
            print('func_name:', self.func_name)
        
        self.route.pop()

    def visitName(self, ctx:MatlabParser.NameContext):
        self.route.append('Name')
        '''
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        '''
        if ctx.NAME():
            var = Var(name_=ctx.NAME().getText())
        self.route.pop()
        return NormalExpr('name', [var]) 

    def visitReturnparas(self, ctx:MatlabParser.ReturnparasContext):
        self.route.append('Returnparas')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        # print(len(ctx.return_name()))
        ret_var = list()

        for var in ctx.return_name():
            ret_var.append(Var(var.getText(), 
                            self.all_var_type[var.getText()]))
            print(var.getText())
        self.route.pop()
        return NormalExpr('returnparas', ret_var) 
    
    def visitReturn_name(self, ctx:MatlabParser.Return_nameContext):
        self.route.append('Returnparas')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        
        if ctx.NAME():
            var = Var(ctx.NAME().getText(), self.all_var_type[ctx.NAME().getText()])
            return NormalExpr('return_name', [var])
        

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
    
    def visitStatement(self, ctx:MatlabParser.StatementContext):
        self.route.append('Statement')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        
        if ctx.global_define_list():
            self.global_list = self.visitGlobal_define_list(ctx.global_define_list())
            print('global_list:', self.global_list)
        
        if ctx.com_statement():
            self.visitCom_statement(ctx.com_statement())
 
    def visitGlobal_define_list(self, ctx:MatlabParser.Global_define_listContext):
        self.route.append('Global_define_list')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
 
        global_name = list()
        for name in ctx.name():
            global_name.append(name.getText())

        self.route.pop()
        return global_name

    def visitCom_statement(self, ctx:MatlabParser.Com_statementContext):
        self.route.append('Com_statement')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        for state in ctx:
            if state.assign_state():
                self.visitAssign_state(state.assign_state())

        self.route.pop()

    def visitAssign_state(self, ctx:MatlabParser.Assign_stateContext):
        self.route.append('Assign_state')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        expr0 = self.visit(ctx.expr(0))
        expr1 = self.visit(ctx.expr(1))
        # print('###', expr0, '=', expr1)
 
        self.route.pop()

    def visitFunction_call(self, ctx:MatlabParser.Function_callContext):
        self.route.append('Function_call')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        self.route.pop()

