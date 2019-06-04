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

# base class for expr
class Expr(metaclass=ABCMeta):
    def __init__(self, name_=str(), var_list_=list()):
        self._name = name_ 
        self._var_list = var_list_ 
    
    def __repr__(self):
        return 'Expr({0._name!r}: {0._var_list!r})'.format(self)

    def __str__(self):
        return '({0._name!s}: {0._var_list!s})'.format(self)


    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self, _name):
        if not isinstance(_name, str):
            raise TypeError("Name expected a string")
        self._name = _name

    @property
    def VarList(self):
        return self._var_list

    @VarList.setter
    def VarList(self, varlist):
        if not isinstance(varlist, list):
            raise TypeError("VarList excepted a list")
        if len(varlist) > 0 and not isinstance(varlist[0], Var):
            raise TypeError("Varlist elem excepted Vars")
        self._var_list = varlist

    @abstractmethod
    def toCode(self):
        pass

class NormalExpr(Expr):
    def __init__(self, name_=str(), var_list_=list()):
        super().__init__(name_=name_, var_list_=var_list_)
    def toCode(self):
        return super().toCode()