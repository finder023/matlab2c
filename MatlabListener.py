# Generated from Matlab.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MatlabParser import MatlabParser
else:
    from MatlabParser import MatlabParser

# This class defines a complete listener for a parse tree produced by MatlabParser.
class MatlabListener(ParseTreeListener):

    # Enter a parse tree produced by MatlabParser#function.
    def enterFunction(self, ctx:MatlabParser.FunctionContext):
        pass

    # Exit a parse tree produced by MatlabParser#function.
    def exitFunction(self, ctx:MatlabParser.FunctionContext):
        pass


    # Enter a parse tree produced by MatlabParser#function_declare.
    def enterFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        pass

    # Exit a parse tree produced by MatlabParser#function_declare.
    def exitFunction_declare(self, ctx:MatlabParser.Function_declareContext):
        pass


    # Enter a parse tree produced by MatlabParser#returnparas.
    def enterReturnparas(self, ctx:MatlabParser.ReturnparasContext):
        pass

    # Exit a parse tree produced by MatlabParser#returnparas.
    def exitReturnparas(self, ctx:MatlabParser.ReturnparasContext):
        pass


    # Enter a parse tree produced by MatlabParser#leftbracket.
    def enterLeftbracket(self, ctx:MatlabParser.LeftbracketContext):
        pass

    # Exit a parse tree produced by MatlabParser#leftbracket.
    def exitLeftbracket(self, ctx:MatlabParser.LeftbracketContext):
        pass


    # Enter a parse tree produced by MatlabParser#rightbracket.
    def enterRightbracket(self, ctx:MatlabParser.RightbracketContext):
        pass

    # Exit a parse tree produced by MatlabParser#rightbracket.
    def exitRightbracket(self, ctx:MatlabParser.RightbracketContext):
        pass


    # Enter a parse tree produced by MatlabParser#return_name.
    def enterReturn_name(self, ctx:MatlabParser.Return_nameContext):
        pass

    # Exit a parse tree produced by MatlabParser#return_name.
    def exitReturn_name(self, ctx:MatlabParser.Return_nameContext):
        pass


    # Enter a parse tree produced by MatlabParser#name.
    def enterName(self, ctx:MatlabParser.NameContext):
        pass

    # Exit a parse tree produced by MatlabParser#name.
    def exitName(self, ctx:MatlabParser.NameContext):
        pass


    # Enter a parse tree produced by MatlabParser#definemark.
    def enterDefinemark(self, ctx:MatlabParser.DefinemarkContext):
        pass

    # Exit a parse tree produced by MatlabParser#definemark.
    def exitDefinemark(self, ctx:MatlabParser.DefinemarkContext):
        pass


    # Enter a parse tree produced by MatlabParser#typedef.
    def enterTypedef(self, ctx:MatlabParser.TypedefContext):
        pass

    # Exit a parse tree produced by MatlabParser#typedef.
    def exitTypedef(self, ctx:MatlabParser.TypedefContext):
        pass


    # Enter a parse tree produced by MatlabParser#ruledef.
    def enterRuledef(self, ctx:MatlabParser.RuledefContext):
        pass

    # Exit a parse tree produced by MatlabParser#ruledef.
    def exitRuledef(self, ctx:MatlabParser.RuledefContext):
        pass


    # Enter a parse tree produced by MatlabParser#nameplus.
    def enterNameplus(self, ctx:MatlabParser.NameplusContext):
        pass

    # Exit a parse tree produced by MatlabParser#nameplus.
    def exitNameplus(self, ctx:MatlabParser.NameplusContext):
        pass


    # Enter a parse tree produced by MatlabParser#cate.
    def enterCate(self, ctx:MatlabParser.CateContext):
        pass

    # Exit a parse tree produced by MatlabParser#cate.
    def exitCate(self, ctx:MatlabParser.CateContext):
        pass


    # Enter a parse tree produced by MatlabParser#digit.
    def enterDigit(self, ctx:MatlabParser.DigitContext):
        pass

    # Exit a parse tree produced by MatlabParser#digit.
    def exitDigit(self, ctx:MatlabParser.DigitContext):
        pass


    # Enter a parse tree produced by MatlabParser#null_assign.
    def enterNull_assign(self, ctx:MatlabParser.Null_assignContext):
        pass

    # Exit a parse tree produced by MatlabParser#null_assign.
    def exitNull_assign(self, ctx:MatlabParser.Null_assignContext):
        pass


    # Enter a parse tree produced by MatlabParser#strExpr.
    def enterStrExpr(self, ctx:MatlabParser.StrExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#strExpr.
    def exitStrExpr(self, ctx:MatlabParser.StrExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#nullExpr.
    def enterNullExpr(self, ctx:MatlabParser.NullExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#nullExpr.
    def exitNullExpr(self, ctx:MatlabParser.NullExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#regExpr.
    def enterRegExpr(self, ctx:MatlabParser.RegExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#regExpr.
    def exitRegExpr(self, ctx:MatlabParser.RegExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#multiExpr.
    def enterMultiExpr(self, ctx:MatlabParser.MultiExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#multiExpr.
    def exitMultiExpr(self, ctx:MatlabParser.MultiExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#parensExpr.
    def enterParensExpr(self, ctx:MatlabParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#parensExpr.
    def exitParensExpr(self, ctx:MatlabParser.ParensExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#digitExpr.
    def enterDigitExpr(self, ctx:MatlabParser.DigitExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#digitExpr.
    def exitDigitExpr(self, ctx:MatlabParser.DigitExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#unary_operaExpr.
    def enterUnary_operaExpr(self, ctx:MatlabParser.Unary_operaExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#unary_operaExpr.
    def exitUnary_operaExpr(self, ctx:MatlabParser.Unary_operaExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#truthExpr.
    def enterTruthExpr(self, ctx:MatlabParser.TruthExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#truthExpr.
    def exitTruthExpr(self, ctx:MatlabParser.TruthExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#nameExpr.
    def enterNameExpr(self, ctx:MatlabParser.NameExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#nameExpr.
    def exitNameExpr(self, ctx:MatlabParser.NameExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#funcallExpr.
    def enterFuncallExpr(self, ctx:MatlabParser.FuncallExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#funcallExpr.
    def exitFuncallExpr(self, ctx:MatlabParser.FuncallExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#addExpr.
    def enterAddExpr(self, ctx:MatlabParser.AddExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#addExpr.
    def exitAddExpr(self, ctx:MatlabParser.AddExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#elemExpr.
    def enterElemExpr(self, ctx:MatlabParser.ElemExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#elemExpr.
    def exitElemExpr(self, ctx:MatlabParser.ElemExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#logicExpr.
    def enterLogicExpr(self, ctx:MatlabParser.LogicExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#logicExpr.
    def exitLogicExpr(self, ctx:MatlabParser.LogicExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#relatExpr.
    def enterRelatExpr(self, ctx:MatlabParser.RelatExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#relatExpr.
    def exitRelatExpr(self, ctx:MatlabParser.RelatExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#andorExpr.
    def enterAndorExpr(self, ctx:MatlabParser.AndorExprContext):
        pass

    # Exit a parse tree produced by MatlabParser#andorExpr.
    def exitAndorExpr(self, ctx:MatlabParser.AndorExprContext):
        pass


    # Enter a parse tree produced by MatlabParser#unary_operation.
    def enterUnary_operation(self, ctx:MatlabParser.Unary_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#unary_operation.
    def exitUnary_operation(self, ctx:MatlabParser.Unary_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#multiplicative_operation.
    def enterMultiplicative_operation(self, ctx:MatlabParser.Multiplicative_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#multiplicative_operation.
    def exitMultiplicative_operation(self, ctx:MatlabParser.Multiplicative_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#additive_operation.
    def enterAdditive_operation(self, ctx:MatlabParser.Additive_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#additive_operation.
    def exitAdditive_operation(self, ctx:MatlabParser.Additive_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#relational_operation.
    def enterRelational_operation(self, ctx:MatlabParser.Relational_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#relational_operation.
    def exitRelational_operation(self, ctx:MatlabParser.Relational_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#andor_operation.
    def enterAndor_operation(self, ctx:MatlabParser.Andor_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#andor_operation.
    def exitAndor_operation(self, ctx:MatlabParser.Andor_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#logical_operation.
    def enterLogical_operation(self, ctx:MatlabParser.Logical_operationContext):
        pass

    # Exit a parse tree produced by MatlabParser#logical_operation.
    def exitLogical_operation(self, ctx:MatlabParser.Logical_operationContext):
        pass


    # Enter a parse tree produced by MatlabParser#truth_value.
    def enterTruth_value(self, ctx:MatlabParser.Truth_valueContext):
        pass

    # Exit a parse tree produced by MatlabParser#truth_value.
    def exitTruth_value(self, ctx:MatlabParser.Truth_valueContext):
        pass


    # Enter a parse tree produced by MatlabParser#location_name.
    def enterLocation_name(self, ctx:MatlabParser.Location_nameContext):
        pass

    # Exit a parse tree produced by MatlabParser#location_name.
    def exitLocation_name(self, ctx:MatlabParser.Location_nameContext):
        pass


    # Enter a parse tree produced by MatlabParser#location.
    def enterLocation(self, ctx:MatlabParser.LocationContext):
        pass

    # Exit a parse tree produced by MatlabParser#location.
    def exitLocation(self, ctx:MatlabParser.LocationContext):
        pass


    # Enter a parse tree produced by MatlabParser#element.
    def enterElement(self, ctx:MatlabParser.ElementContext):
        pass

    # Exit a parse tree produced by MatlabParser#element.
    def exitElement(self, ctx:MatlabParser.ElementContext):
        pass


    # Enter a parse tree produced by MatlabParser#paralist.
    def enterParalist(self, ctx:MatlabParser.ParalistContext):
        pass

    # Exit a parse tree produced by MatlabParser#paralist.
    def exitParalist(self, ctx:MatlabParser.ParalistContext):
        pass


    # Enter a parse tree produced by MatlabParser#statement.
    def enterStatement(self, ctx:MatlabParser.StatementContext):
        pass

    # Exit a parse tree produced by MatlabParser#statement.
    def exitStatement(self, ctx:MatlabParser.StatementContext):
        pass


    # Enter a parse tree produced by MatlabParser#global_define_list.
    def enterGlobal_define_list(self, ctx:MatlabParser.Global_define_listContext):
        pass

    # Exit a parse tree produced by MatlabParser#global_define_list.
    def exitGlobal_define_list(self, ctx:MatlabParser.Global_define_listContext):
        pass


    # Enter a parse tree produced by MatlabParser#com_statement.
    def enterCom_statement(self, ctx:MatlabParser.Com_statementContext):
        pass

    # Exit a parse tree produced by MatlabParser#com_statement.
    def exitCom_statement(self, ctx:MatlabParser.Com_statementContext):
        pass


    # Enter a parse tree produced by MatlabParser#assign_state.
    def enterAssign_state(self, ctx:MatlabParser.Assign_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#assign_state.
    def exitAssign_state(self, ctx:MatlabParser.Assign_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#function_call.
    def enterFunction_call(self, ctx:MatlabParser.Function_callContext):
        pass

    # Exit a parse tree produced by MatlabParser#function_call.
    def exitFunction_call(self, ctx:MatlabParser.Function_callContext):
        pass


    # Enter a parse tree produced by MatlabParser#return_state.
    def enterReturn_state(self, ctx:MatlabParser.Return_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#return_state.
    def exitReturn_state(self, ctx:MatlabParser.Return_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#while_state.
    def enterWhile_state(self, ctx:MatlabParser.While_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#while_state.
    def exitWhile_state(self, ctx:MatlabParser.While_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#if_state.
    def enterIf_state(self, ctx:MatlabParser.If_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#if_state.
    def exitIf_state(self, ctx:MatlabParser.If_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#elseif_state.
    def enterElseif_state(self, ctx:MatlabParser.Elseif_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#elseif_state.
    def exitElseif_state(self, ctx:MatlabParser.Elseif_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#else_state.
    def enterElse_state(self, ctx:MatlabParser.Else_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#else_state.
    def exitElse_state(self, ctx:MatlabParser.Else_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#break_state.
    def enterBreak_state(self, ctx:MatlabParser.Break_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#break_state.
    def exitBreak_state(self, ctx:MatlabParser.Break_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#continue_state.
    def enterContinue_state(self, ctx:MatlabParser.Continue_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#continue_state.
    def exitContinue_state(self, ctx:MatlabParser.Continue_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#element_insert_state.
    def enterElement_insert_state(self, ctx:MatlabParser.Element_insert_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#element_insert_state.
    def exitElement_insert_state(self, ctx:MatlabParser.Element_insert_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#element_delete_state.
    def enterElement_delete_state(self, ctx:MatlabParser.Element_delete_stateContext):
        pass

    # Exit a parse tree produced by MatlabParser#element_delete_state.
    def exitElement_delete_state(self, ctx:MatlabParser.Element_delete_stateContext):
        pass


    # Enter a parse tree produced by MatlabParser#element_ismember_set.
    def enterElement_ismember_set(self, ctx:MatlabParser.Element_ismember_setContext):
        pass

    # Exit a parse tree produced by MatlabParser#element_ismember_set.
    def exitElement_ismember_set(self, ctx:MatlabParser.Element_ismember_setContext):
        pass


    # Enter a parse tree produced by MatlabParser#element_take.
    def enterElement_take(self, ctx:MatlabParser.Element_takeContext):
        pass

    # Exit a parse tree produced by MatlabParser#element_take.
    def exitElement_take(self, ctx:MatlabParser.Element_takeContext):
        pass


