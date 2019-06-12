#! /usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Var(object):
    def __init__(self, name_=str(), type_=str()):
        self._name = name_ 
        self._type = type_ 
    
    def __repr__(self):
        return 'Var({0._name!r}: {0._type!r})'.format(self)

    def __str__(self):
        return '({0._name!s}: {0._type!s})'.format(self)

    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name expected a string")
        self._name = name
    
    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, type_):
        if not isinstance(type_, str):
            raise TypeError("Type excepted a string")
        self._type = type_ 

class Expr():
    def __init__(self, type_=str(), name_=str(), deps_=list()):
        self._name = name_
        self._type = type_
        self._deps = deps_
        self._dep_str = str()

        # format
        self._indent_str = ' ' * 4
        # self._indent = '\t'
        self.indent_level = 0
        self.sub_expr = True 
        self._indent_prefix = str()
        self._end = ''

    def __repr__(self):
        self._dep2str()
        if len(self._name) != 0 and len(self._deps) != 0:
            return '<type:{0._type}, name:{0._name}, deps:{0._dep_str}>'.format(self)
        if len(self._deps) != 0 and len(self._name) == 0:
            return '<type:{0._type}, deps:{0._dep_str}>'.format(self)
        if len(self._deps) == 0 and len(self._name) != 0:
            return '<type:{0._type}, name:{0._name}>'.format(self)
        return '<type:{0._type}>'.format(self)

    def __str__(self):
        return self.__repr__()


    def _dep2str(self):
        # self._dep_str = ','.join(self._deps)
        self._dep_str = str(self._deps)

    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self, _name):
        if not isinstance(_name, str):
            raise TypeError("Name expected a string")
        self._name = _name
   
    @property
    def Deps(self):
        return self._deps

    @Deps.setter
    def Deps(self, deps_):
        self._deps = deps_

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, type_):
        if not isinstance(type_, str):
            raise TypeError("Type excepted a string")
        self._type = type_ 
    
    def toStr(self):
        return 'Expr'
   
# digit, truth_value, nameExpr, function call, 
class NormalExpr(Expr):
    def __init__(self, type_=str(), name_=str(), var_list_=list(), deps_=list()):
        super().__init__(name_=name_, type_=type_, deps_=deps_)
        self.var_list = var_list_
    
    def toStr():
        '''
        very complex
        ''' 
        pass

class FunctionExpr(Expr):
    def __init__(self, func_declar_=Expr("functoin"), 
                    state_=Expr("statement")):
        super().__init__(type_='functon', deps_=[func_declar_, state_])

    def toStr(self):
        if not self.sub_expr:
            self._indent_prefix = self.indent_level + self._indent_str
        '''
        very complex
        ''' 

class AssignExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr()):
        super().__init__(type_='assign_state', deps_=[left_, right_])

    def toStr(self):
        left_str = self.Deps[0].toStr()
        right_str = self.Deps[1].toStr()
        if not self.sub_expr:
            self._indent_prefix = self._indent_str * self.indent_level
            self._end = '\n'
        return self._indent_prefix + left_str + ' = ' + right_str + self._end

class UnaryExpr(Expr):
    def __init__(self, unary_opr_=str(), expr_=Expr()):
        super().__init__(type_='unary_operaExpr', deps_=[unary_opr_, expr_])

    def toStr(self):
        unary_str = self.Deps[0]
        expr_ = self.Deps[1]
        assert isinstance(unary_str, str), 'unary opr need to be str type'
        assert unary_str == '-' or unary_str == '~'
        if unary_str == '~':
            unary_str = '!'

        if not self.sub_expr:
            self._indent_prefix = self._indent_str * self.indent_level
            self._end = '\n'
        return self._indent_prefix + unary_str + expr_.toStr() + self._end
        
class BinaryExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr(), opr_=str()):
        super().__init__(type_='binaryExpr', name_=opr_, deps_=[left_, right_])
        self._opr = opr_
    
    def toStr(self):
        assert len(self.Deps) == 2
        left_str = self.Deps[0].toStr()
        right_str = self.Deps[1].toStr()

        if not self.sub_expr:
            self._end = '\n'
            self._indent_prefix = self._indent_str * self.indent_level

        opr_str = self._opr
        if opr_str == '~=':
            opr_str = '!='

        return left_str + ' ' + opr_str + ' ' + right_str + self._end

class FunctionCallExpr(Expr):
    def __init__(self, name_=Expr(), paralist_=Expr()):
        super().__init__(type_='function_call', deps_=[name_, paralist_])
    
    def toStr(self):
        assert(len(self.Deps) == 2)
        func_name = self.Deps[0].toStr()
        paralist = self.Deps[1].toStr()
        if not self.sub_expr:
            self._indent_prefix = self._indent_str * self.indent_level
            self._end = '\n'
                
        return self._indent_prefix + func_name + '(' + paralist + ')' + self._end


class ParentsExpr(Expr):
    def __init__(self, expr_=Expr()):
        super().__init__(type_='parentsExpr', deps_=expr_)

    def toStr(self):
        expr_str = self.Deps[0].toStr()
        if not self.sub_expr:
            self._indent_prefix = self._indent_str * self.indent_level
            self._end = '\n'
        
        return self._indent_prefix + '(' + expr_str + ')' + self._end

class WhileExpr(Expr):
    def __init__(self, cond_=Expr(), com_=Expr()):
        super().__init__(type_='while_state', deps_=[cond_, com_])

    def toStr():
        pass

class ElseIfExpr(Expr):
    def __init__(self, cond_=Expr(), com_=Expr()):
       super().__init__(type_='elseif_state', deps_=[cond_, com_])
    
    def toStr():
        pass

class ElseExpr(Expr):
    def __init__(self, com_=Expr()):
        super().__init__(type_='else_state', deps_=[com_])

    def toStr():
        pass


class IfExpr(Expr):
    def __init__(self, expr_=Expr(), com_=Expr(), elseif_=Expr(), else_=Expr()):
        super().__init__(type_='if_state', deps_=[expr_, com_, elseif_, else_])

    def toStr():
        pass