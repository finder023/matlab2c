#！ /usr/bin/python3

from antlr4 import *
import json
from expr import *
from copy import copy

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
        self.func_name = str()
        self.indent_level = HierarchicalCoding()
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
            '''
            function declare toStr pass!
            print('func_declare: ', func_declare)
            print(func_declare.toStr())
            '''

        if ctx.statement():
            state = self.visitStatement(ctx.statement())
            # print(state.toStr())
        self.route.pop()

        # visit tree started node
        return FunctionExpr(func_declar_=func_declare, state_=state, 
                    subexpr_=False, indent_=HierarchicalCoding())


    def visitFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        self.route.append('Function_declare')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        # visit return_params 
        if ctx.returnparas():
            ret_var = self.visitReturnparas(ctx.returnparas())
            # print('ret_val:', ret_var)
        # visit paralist
        if ctx.paralist():
            self.para_list = self.visitParalist(ctx.paralist())
            # print('para_list:', self.para_list)
        # visit name
        if ctx.name():
            self.func_name = self.visitName(ctx.name())
            # print('func_name:', self.func_name)
        
        self.route.pop()
        _expr = FunctionDeclareExpr(returnparas_=ret_var, name_=self.func_name,
                paralist_=self.para_list, subexpr_=False, 
                indent_=self.indent_level)
        self.indent_level.pushLevel()
        return _expr

    def visitName(self, ctx:MatlabParser.NameContext):
        self.route.append('Name')
        '''
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        '''
        if ctx.NAME():
            name_=ctx.NAME().getText()
        self.route.pop()
        return NormalExpr(type_='name', name_=name_, subexpr_=True) 

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
            # print(var.getText())
        self.route.pop()
        return NormalExpr(type_='returnparas', var_list_=ret_var, subexpr_=True) 
    
    def visitReturn_name(self, ctx:MatlabParser.Return_nameContext):
        self.route.append('ReturnName')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        
        if ctx.NAME():
            var = Var(ctx.NAME().getText(), self.all_var_type[ctx.NAME().getText()])
            return NormalExpr(type_='return_name', deps_=[var], subexpr_=True)
        

    def visitParalist(self, ctx:MatlabParser.ParalistContext):
        self.route.append('Paralist')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        
        # print(len(ctx.expr()))
        varlist = list()
        for _expr in ctx.expr():
            varlist.append(Var(_expr.getText(), self.all_var_type[_expr.getText()]))
        self.route.pop()
        return NormalExpr(type_='paralist', var_list_=varlist, subexpr_=True) 
    
    def visitStatement(self, ctx:MatlabParser.StatementContext):
        self.route.append('Statement')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        global_list = NormalExpr() 
        if ctx.global_define_list():
            global_list = self.visitGlobal_define_list(ctx.global_define_list())
            # print('global_list:', global_list)

        com_state = NormalExpr()
        if ctx.com_statement():
            com_state = self.visitCom_statement(ctx.com_statement())
        
        return NormalExpr(type_='statement', deps_=[global_list, com_state],
                            subexpr_=True)
 
    def visitGlobal_define_list(self, ctx:MatlabParser.Global_define_listContext):
        self.route.append('Global_define_list')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        global_name = list()
        for name in ctx.name():
            global_name.append(Var(name.getText(), self.all_var_type[name.getText()]))
        self.route.pop()

        self.indent_level.addLevel()
        _expr = NormalExpr(type_='global_define_list', var_list_=global_name, 
                    subexpr_=False, indent_=self.indent_level)
        return _expr

    def visitCom_statement(self, ctx:MatlabParser.Com_statementContext):
        self.route.append('Com_statement')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')
        expr_list = list()
        p = False 
        for state in ctx:
            if state.assign_state():
                expr_list.append(self.visitAssign_state(state.assign_state()))
                if p: print('###', expr_list[-1]) 
            if state.function_call():
                expr_list.append(self.visitFunction_call(state.function_call()))
                if p: print('###', expr_list[-1])
            if state.return_state():
                expr_list.append(self.visitReturn_state(state.return_state()))
                if p: print('###', 'return_state')
            if state.while_state():
                expr_list.append(self.visitWhile_state(state.while_state()))
                if p: print('### while_state')
            if state.if_state():
                expr_list.append(self.visitIf_state(state.if_state()))
                if p: print('###', expr_list[-1])
            
            if state.element_take():
                print('ElemTake')
                expr_list.append(self.visitElement_take(state.element_take()))

        self.route.pop()
        return NormalExpr(type_='com_statement', deps_=expr_list, 
                subexpr_=False, indent_=copy(self.indent_level))

    def visitAssign_state(self, ctx:MatlabParser.Assign_stateContext):
        self.route.append('Assign_state')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        assert (len(ctx.expr()) == 2)
        
        # print("assign: ", ctx.expr())

        self.indent_level.addLevel()

        expr_list = list()
        for assign_expr in ctx.expr():
            if isinstance(assign_expr, MatlabParser.NameExprContext):
                expr_list.append(self.visitNameExpr(assign_expr))
                assert expr_list[-1] is not None

            elif isinstance(assign_expr, MatlabParser.Unary_operaExprContext):
                expr_list.append(self.visitUnary_operaExpr(assign_expr))
                assert expr_list[-1] is not None
            
            elif isinstance(assign_expr, MatlabParser.BinaryExprContext):
                expr_list.append(self.visitBinaryExpr(assign_expr))
                assert expr_list[-1] is not None

            elif isinstance(assign_expr, MatlabParser.DigitExprContext):
                expr_list.append(self.visitDigitExpr(assign_expr))
                assert expr_list[-1] is not None

            elif isinstance(assign_expr, MatlabParser.TruthExprContext):
                expr_list.append(self.visitTruthExpr(assign_expr))
                assert expr_list[-1] is not None
            
            elif isinstance(assign_expr, MatlabParser.RegExprContext):
                expr_list.append(self.visitRegExpr(assign_expr))
                assert expr_list[-1] is not None
            
            elif isinstance(assign_expr, MatlabParser.FuncallExprContext):
                func_expr = self.visitFuncallExpr(assign_expr)
                func_expr.sub_expr = True
                expr_list.append(func_expr)
                assert expr_list[-1] is not None

            elif isinstance(assign_expr, MatlabParser.ElemExprContext):
                expr_list.append(self.visitElemExpr(assign_expr))
                assert expr_list[-1] is not None
            
            elif isinstance(assign_expr, MatlabParser.NullExprContext):
                expr_list.append(self.visitNullExpr(assign_expr))
                assert expr_list[-1] is not None
            
            elif isinstance(assign_expr, MatlabParser.StrExprContext):
                expr_list.append(self.visitStrExpr(assign_expr))
                assert expr_list[-1] is not None

            else:
                raise TypeError("Assign not supported type:", assign_expr)

        self.route.pop()
        return AssignExpr(left_=expr_list[0], right_=expr_list[1], 
                subexpr_=False, indent_=copy(self.indent_level))

    def visitFunction_call(self, ctx:MatlabParser.Function_callContext):
        self.route.append('Function_call')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.name():
            name = self.visitName(ctx.name())

        if ctx.paralist():
            para_list = self.visitParalist(ctx.paralist())

        self.route.pop()
        return FunctionCallExpr(name_=name, paralist_=para_list, 
                    subexpr_=True)

    # Visit a parse tree produced by MatlabParser#binaryExpr.
    def visitBinaryExpr(self, ctx:MatlabParser.BinaryExprContext):
        self.route.append('BinaryExpr')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.binary_operation():
            opr = ctx.binary_operation().getText()

        assert len(ctx.expr()) == 2
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        self.route.pop()
        return BinaryExpr(left_=left, right_=right, opr_=opr)

    # Visit a parse tree produced by MatlabParser#parensExpr.
    def visitParensExpr(self, ctx:MatlabParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#digitExpr.
    def visitDigitExpr(self, ctx:MatlabParser.DigitExprContext):
        if ctx.digit():
            digit_ = ctx.digit().getText()
        
        return NormalExpr(type_='digit', name_=digit_)

    # Visit a parse tree produced by MatlabParser#unary_operaExpr.
    def visitUnary_operaExpr(self, ctx:MatlabParser.Unary_operaExprContext):
        self.route.append('Unary_operaExpr')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.unary_operation():
            opr = ctx.unary_operation().getText()

        assert len(ctx.expr()) == 1
        _expr = self.visit(ctx.expr(0))
        self.route.pop()

        return UnaryExpr(unary_expr_=opr, expr_=_expr)

    # Visit a parse tree produced by MatlabParser#return_state.
    def visitReturn_state(self, ctx:MatlabParser.Return_stateContext):
        return NormalExpr(type_='return_state', subexpr_=False, 
                    indent_=copy(self.indent_level)) 
    
    # Visit a parse tree produced by MatlabParser#nameExpr.
    def visitNameExpr(self, ctx:MatlabParser.NameExprContext):
        name_list = list()
        for name in ctx.name():
            name_list.append(self.visitName(name))
        
        return NormalExpr(type_='nameExpr', name_='.', deps_=name_list)

    # Visit a parse tree produced by MatlabParser#while_state.
    def visitWhile_state(self, ctx:MatlabParser.While_stateContext):
        self.route.append('While_state')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        if ctx.expr():
            _cond = self.visit(ctx.expr())
        
        if ctx.com_statement():
            self.indent_level.pushLevel()
            _com = self.visitCom_statement(ctx.com_statement())
            self.indent_level.popLevel()

        self.route.pop()
        expr_ = WhileExpr(cond_=_cond, com_=_com, indent_=self.indent_level)
        return expr_


    # Visit a parse tree produced by MatlabParser#if_state.
    def visitIf_state(self, ctx:MatlabParser.If_stateContext):
        self.route.append('If_state')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        assert ctx.expr()
        if_cond_ = self.visit(ctx.expr())
        # print('if_cond_:', if_cond_) 
        if_state = list()
        if ctx.com_statement():
            self.indent_level.pushLevel()
            if_state = self.visitCom_statement(ctx.com_statement())
            self.indent_level.popLevel()
            # print('if_state', if_state) 
        elseif_state = None 
        if ctx.elseif_state():
            elseif_state = self.visitElseif_state(ctx.elseif_state())

        else_state = None 
        if ctx.else_state():
            self.indent_level.pushLevel()
            else_state = self.visitElse_state(ctx.else_state())
            self.indent_level.popLevel()
        self.route.pop()
        print('if out indent level:', self.indent_level.level)
        expr_ = IfExpr(expr_=if_cond_, com_=if_state, elseif_=elseif_state, 
                        else_=else_state, indent_=copy(self.indent_level), 
                        subexpr_=False) 
        return expr_

    # Visit a parse tree produced by MatlabParser#elseif_state.
    def visitElseif_state(self, ctx:MatlabParser.Elseif_stateContext):
        assert ctx.expr()
        elseif_cond_ = self.visit(ctx.expr())
        elseif_state_ = list()
        if ctx.com_statement():
            self.indent_level.pushLevel()
            elseif_state = self.visitCom_statement(ctx.com_statement())
            self.indent_level.popLevel()

        return ElseIfExpr(cond_=elseif_cond_, com_=elseif_state_)

    # Visit a parse tree produced by MatlabParser#else_state.
    def visitElse_state(self, ctx:MatlabParser.Else_stateContext):
        if ctx.com_statement():
            self.indent_level.pushLevel()
            else_state_ = self.visitCom_statement(ctx.com_statement())
            self.indent_level.popLevel()

        return ElseExpr(com_=else_state_)

    # Visit a parse tree produced by MatlabParser#break_state.
    def visitBreak_state(self, ctx:MatlabParser.Break_stateContext):
        return NormalExpr(type_='break_state', subexpr_=False,
                    indent_=copy(self.indent_level))

    # Visit a parse tree produced by MatlabParser#continue_state.
    def visitContinue_state(self, ctx:MatlabParser.Continue_stateContext):
        return NormalExpr(type_='continue_state', subexpr_=False,
                    indent_=copy(self.indent_level))

    # Visit a parse tree produced by MatlabParser#nullExpr.
    def visitNullExpr(self, ctx:MatlabParser.NullExprContext):
        return NormalExpr(type_='nullExpr') 

    # Visit a parse tree produced by MatlabParser#element_take.
    def visitElement(self, ctx:MatlabParser.Element_takeContext):
        self.route.append('ElementExpr')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        name_, location_ = None, None
        if ctx.name():
            name_ = self.visitName(ctx.name())

        if ctx.location():
            location_ = self.visitLocation(ctx.location())
         
        self.route.pop()
        return ElementExpr(name_=name_, location_=location_)


    # Visit a parse tree produced by MatlabParser#location_name.
    def visitLocation_name(self, ctx:MatlabParser.Location_nameContext):
        if ctx.COLON():
            return NormalExpr(type_='location_name', name_=':')
        
        if ctx.expr():
            return self.visit(ctx.expr())


    # Visit a parse tree produced by MatlabParser#location.
    def visitLocation(self, ctx:MatlabParser.LocationContext):
        self.route.append('LocationExpr')
        if self.log:
            print('->'.join(self.route))
            print('visit', self.route[-1], ':')

        location_name_list = list() 
        for loc in ctx.location_name():
            location_name_list.append(self.visitLocation_name(loc))

        return NormalExpr(type_='location', deps_=location_name_list)