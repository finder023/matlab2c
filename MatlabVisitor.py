# Generated from Matlab.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MatlabParser import MatlabParser
else:
    from MatlabParser import MatlabParser

# This class defines a complete generic visitor for a parse tree produced by MatlabParser.

class MatlabVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatlabParser#function.
    def visitFunction(self, ctx:MatlabParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#function_declare.
    def visitFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#returnparas.
    def visitReturnparas(self, ctx:MatlabParser.ReturnparasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#leftbracket.
    def visitLeftbracket(self, ctx:MatlabParser.LeftbracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#rightbracket.
    def visitRightbracket(self, ctx:MatlabParser.RightbracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#return_name.
    def visitReturn_name(self, ctx:MatlabParser.Return_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#name.
    def visitName(self, ctx:MatlabParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#definemark.
    def visitDefinemark(self, ctx:MatlabParser.DefinemarkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#typedef.
    def visitTypedef(self, ctx:MatlabParser.TypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#ruledef.
    def visitRuledef(self, ctx:MatlabParser.RuledefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#nameplus.
    def visitNameplus(self, ctx:MatlabParser.NameplusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#cate.
    def visitCate(self, ctx:MatlabParser.CateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#digit.
    def visitDigit(self, ctx:MatlabParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#null_assign.
    def visitNull_assign(self, ctx:MatlabParser.Null_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#strExpr.
    def visitStrExpr(self, ctx:MatlabParser.StrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#funcallExpr.
    def visitFuncallExpr(self, ctx:MatlabParser.FuncallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#nullExpr.
    def visitNullExpr(self, ctx:MatlabParser.NullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#regExpr.
    def visitRegExpr(self, ctx:MatlabParser.RegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#elemExpr.
    def visitElemExpr(self, ctx:MatlabParser.ElemExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#binaryExpr.
    def visitBinaryExpr(self, ctx:MatlabParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#parensExpr.
    def visitParensExpr(self, ctx:MatlabParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#digitExpr.
    def visitDigitExpr(self, ctx:MatlabParser.DigitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#unary_operaExpr.
    def visitUnary_operaExpr(self, ctx:MatlabParser.Unary_operaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#truthExpr.
    def visitTruthExpr(self, ctx:MatlabParser.TruthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#nameExpr.
    def visitNameExpr(self, ctx:MatlabParser.NameExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#binary_operation.
    def visitBinary_operation(self, ctx:MatlabParser.Binary_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#unary_operation.
    def visitUnary_operation(self, ctx:MatlabParser.Unary_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#truth_value.
    def visitTruth_value(self, ctx:MatlabParser.Truth_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#location_name.
    def visitLocation_name(self, ctx:MatlabParser.Location_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#location.
    def visitLocation(self, ctx:MatlabParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#element.
    def visitElement(self, ctx:MatlabParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#paralist.
    def visitParalist(self, ctx:MatlabParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#statement.
    def visitStatement(self, ctx:MatlabParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#global_define_list.
    def visitGlobal_define_list(self, ctx:MatlabParser.Global_define_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#com_statement.
    def visitCom_statement(self, ctx:MatlabParser.Com_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#assign_state.
    def visitAssign_state(self, ctx:MatlabParser.Assign_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#function_call.
    def visitFunction_call(self, ctx:MatlabParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#return_state.
    def visitReturn_state(self, ctx:MatlabParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#while_state.
    def visitWhile_state(self, ctx:MatlabParser.While_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#if_state.
    def visitIf_state(self, ctx:MatlabParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#elseif_state.
    def visitElseif_state(self, ctx:MatlabParser.Elseif_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#else_state.
    def visitElse_state(self, ctx:MatlabParser.Else_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#break_state.
    def visitBreak_state(self, ctx:MatlabParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#continue_state.
    def visitContinue_state(self, ctx:MatlabParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#element_insert_state.
    def visitElement_insert_state(self, ctx:MatlabParser.Element_insert_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#element_delete_state.
    def visitElement_delete_state(self, ctx:MatlabParser.Element_delete_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#element_ismember_set.
    def visitElement_ismember_set(self, ctx:MatlabParser.Element_ismember_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatlabParser#element_take.
    def visitElement_take(self, ctx:MatlabParser.Element_takeContext):
        return self.visitChildren(ctx)



del MatlabParser