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
   
    def __repr__(self):
        return '({0._type!r}: {0._name!r} | {0._dep_str!r})'.format(self)

    def __str__(self):
        return '({0._type!s}: {0._name!s} | {0._dep_str!s})'.format(self)

    def _dep2str(self):
        self._dep_str = ','.join(self._deps)

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
   
# digit, truth_value, nameExpr, function call, 
class NormalExpr(Expr):
    def __init__(self, type_=str(), name_=str(), var_list_=list(), deps_=list()):
        super().__init__(name_=name_, type_=type_, deps_=deps_)
        self.var_list = var_list_
    
    def toStr():
        pass

class FunctionExpr(Expr):
    def __init__(self, func_declar_=Expr("functoin"), 
                    state_=Expr("statement")):
        super().__init__('functon')
        self.func_declar = func_declar_
        self.states = state_

    def toStr():
        pass

class AssignExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr()):
        super().__init__(type_='assign_state', deps_=[left_, right_])
    
    def __repr__(self):
        return 'AssignExpr({0.Type!r}:{0.Name!r} | {0.Deps!r})'.format(self)

    def __str__(self):
        return 'AssignExpr({0.Type!s}:{0.Name!s} | {0.Deps!s})'.format(self)

   
    def toStr():
        pass

class UnaryExpr(Expr):
    def __init__(self, unary_opr_=str(), expr_=Expr()):
        super().__init__(type_='unary_operaExpr', deps_=[expr_])
        self._unary_opr = unary_opr_

    def toStr():
        pass

class BinaryExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr(), opr_=str()):
        super().__init__(type_='binaryExpr', name_=opr_, deps_=[left_, right_])
        self._opr = opr_
    
    def __repr__(self):
        return 'BinaryExpr({0.Name!r}:{0.Type!r} | {0.Deps!r})'.format(self)

    def __str__(self):
        return 'BinaryExpr({0.Name!s}:{0.Type!s} | {0.Deps!s})'.format(self)

    def toStr():
        pass

class FunctionCallExpr(Expr):
    def __init__(self, name_=Expr(), paralist_=Expr()):
        super().__init__(type_='function_call', deps_=[name_, paralist_])
    
    def __repr__(self):
        return 'FunctionCallExpr({0.Name!r}:{0.Deps!r})'.format(self)

    def __str__(self):
        return 'FunctionCallExpr({0.Name!s}:{0.Deps!s})'.format(self)


    def toStr():
        pass

class ParentsExpr(Expr):
    def __init__(self, expr_=Expr()):
        super().__init__(type_='parentsExpr', deps_=expr_)

    def toStr():
        pass

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