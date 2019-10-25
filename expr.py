#! /usr/bin/env python3

from abc import ABCMeta, abstractmethod
from copy import deepcopy

from conf import with_hcoding

class HierarchicalCoding(object):
    def __init__(self):
        self.stack = list()
        self.level = 0
        # self.addLevel()
        self._indent_str = ' ' * 4

    def pushLevel(self):
        self.level += 1
        self.stack.append(0)

    def popLevel(self):
        self.level -= 1
        self.stack.pop()

    def addLevel(self):
        self.stack[-1] += 1

    def toStr(self):
        return '.'.join(self.stack)
    
    def indentPrefix(self) :
        return self._indent_str * self.level

class Var(object):
    def __init__(self, name_=str(), type_=str(), new_=False):
        self._name = name_
        self._type = type_
        self._is_new = new_ 
    
    def __repr__(self):
        return 'Var({0._name!r}: {0._type!r})'.format(self)

    def __str__(self):
        return 'Var({0._name!s}: {0._type!s})'.format(self)

    def __eq__(self, other):
        return self.Name == other.Name

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

    def isPtr(self) -> bool:
        return self._type.endswith('*')

    def isNew(self) -> bool:
        return self._is_new

class Expr():
    def __init__(self, type_=str(), name_=str(), deps_=list(), vars_=list()):
        self._name = name_
        self._type = type_
        self._deps = deps_
        self._dep_str = str()
        self._vars = vars_

        # format
        self._indent_str = ' ' * 4
        # self._indent = '\t'
        self.indent_level = HierarchicalCoding() 
        self.sub_expr = True 
        self._indent_prefix = str()
        self._end = ''

        # merge dep vars
        self.mergeDepVars()
#        if (type_ == 'global_define_list'):
#            print(vars_, self._vars)

    def __repr__(self):
        self._dep2str()
        if len(self._name) != 0 and len(self._deps) != 0:
            return '<type:{0._type}, name:{0._name}, deps:{0._dep_str}>'\
                                                                .format(self)
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

    @property
    def Vars(self):
        return self._vars
    
    @Type.setter
    def Vars(self, vars_):
        if not isinstance(vars_, list):
            if len(vars_) != 0 and not isinstance(vars_[0], Var):
                raise TypeError('Vars excepted a varlist')
        self._vars = vars_

    # need to impl
    def toStr(self) -> str:
        return str() 

    def getIndentPrefix(self):
        if not self.sub_expr:
            self._indent_prefix = self.indent_level.indentPrefix()
            if with_hcoding:
                self._end = ' ' * 8 + '// '
                self._end += '.'.join(str(i) for i in self.indent_level.stack)
                self._end += '\n' 
            else:
                self._end = '\n'

    def mergeDepVars(self):

        if self.Type == 'name' or self.Type == 'digit':
            # print('nameVars:', self._vars)
            return

        '''
        if self.Type == 'nameExpr':
            namespaces = list()

            for dep in self.Deps:
                assert isinstance(dep, NormalExpr)
                namespaces.append(dep.Name)
            
            names = '::'.join(namespaces)
            type_ = self.Deps[-1]._vars[0].Type
            var_ = Var(name_=names, type_=type_)
            self._vars = [var_]
            return
        '''

        _vars = list()
        # print('#! deps:', self._deps)
        for dep in self._deps:
            if dep is None:
                continue
            # print('mergeing:', dep._vars)
            for var_ in dep._vars:
                if var_ not in _vars:
                    _vars.append(var_)
        
        # if len(_vars) > 0: print('mergeRes:', _vars)
        self._vars = self._vars + _vars

# digit, truth_value, nameExpr, 
class NormalExpr(Expr):
    def __init__(self, type_=str(), name_=str(), vars_=list(), 
                 subexpr_=True, deps_=list(), indent_=HierarchicalCoding()):
        super().__init__(name_=name_, type_=type_, deps_=deps_, vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_
        #if type_ == 'global_define_list':
        #    print(self._vars)

    
    def toStr(self):
        # for empty normalExpr
        if self.Type == '':
            return str()
        # name
        if self.Type == 'name':
            return self.Name
        
        elif self.Type == 'returnparas':
            return str()
        
        elif self.Type == 'return_name':
            return str() 

        # function call, function declare
        elif self.Type == 'paralist':
            code_list = list()
            for dep in self.Deps:
                code_list.append(dep.toStr())
            return ','.join(code_list) 

        elif self.Type == 'global_define_list':
            if len(self._vars) == 0:
                return str()

            global_var_list = list()
            for var in self._vars:
                global_var_list.append('extern ' + var.Type + ' ' + var.Name)
            if not self.sub_expr:
                self.getIndentPrefix()

            res = self._indent_prefix
            res += (';\n' + self._indent_prefix).join(global_var_list)
            return res + ';' + self._end
            
        elif self.Type == 'com_statement':
            if len(self.Deps) == 0:
                return str()

            # do not need call getIndentPrefix()
            com_state_list = list() 
            for dep in self.Deps:
                codes = dep.toStr()
                com_state_list.append(codes)

            return ''.join(com_state_list)
        
        elif self.Type == 'digit':
            return self.Name

        elif self.Type == 'return_state':
            if not self.sub_expr:
                self.getIndentPrefix()
            return self._indent_prefix + 'return;' + self._end
            
        elif self.Type == 'break_state':
            if not self.sub_expr:
                self.getIndentPrefix()
            return self._indent_prefix + 'break;' + self._end

        elif self.Type == 'continue_state':
            if not self.sub_expr:
                self.getIndentPrefix()
            return self._indent_prefix + 'continue;' + self._end

        elif self.Type == 'statement':
            if not self.sub_expr:
                self.getIndentPrefix()
            
            # global_define_list and com_statement
            assert len(self.Deps) == 2
            global_expr = self.Deps[0]
            statement_expr = self.Deps[1]

            global_str = global_expr.toStr()
            # print("Gloabal_str:\n", global_str)
            statement_str = statement_expr.toStr()

            res = global_str + '\n'
            res += statement_str
            return res
        
        # this is important, nameExpr
        elif self.Type == 'nameExpr':
            if not self.sub_expr:
                self.getIndentPrefix()

            # unlikely
            if len(self.Deps) == 0:
                return str()

            var_list = list()
            for dep in self.Deps:
                assert len(dep._vars) == 1
                var_list.append(dep._vars[0])

            res = str()
            # new_var, need define
            if len(var_list) == 1 and var_list[0].isNew():
                var = var_list[0]
                res += var.Type + ' '

            for var in var_list:
                res += var.Name
                if var.isPtr():
                    if var != var_list[-1]:
                        res += '->'
                else:
                    if var != var_list[-1]:
                        res += '.'

            return self._indent_prefix + res + self._end 

        elif self.Type == 'nullExpr':
            return 'NULL' 

        else:
            raise TypeError('not support normal expr type:', self.Type)

# returnparas contains varlist
class FunctionDeclareExpr(Expr):
    def __init__(self, returnparas_=Expr(), name_=Expr(), paralist_=Expr(), 
                    subexpr_=False, indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='function_declare', vars_=vars_, 
                            deps_=[returnparas_, name_, paralist_])
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 3

        if not self.sub_expr:
            self.getIndentPrefix()

        returnparas_expr = self.Deps[0]
        name_expr = self.Deps[1]
        paralist_expr = self.Deps[2]

        # paralist_expr must be NormalExpr
        assert isinstance(paralist_expr, NormalExpr)
        assert isinstance(returnparas_expr, NormalExpr)

        return_varlist = returnparas_expr._vars
        para_varlist = paralist_expr._vars
        # print('para_varlist:', para_varlist)
        name_str = name_expr.toStr()

        c_para_list = list()

        for var in para_varlist:
            c_para_list.append(var.Type + ' ' + var.Name)

        for var in return_varlist:
            c_para_list.append(var.Type + ' ' + var.Name)

        para_str = ', '.join(c_para_list)

        res = 'void ' + name_str + '( '
        res += para_str + ')'
        return res

class FunctionExpr(Expr):
    def __init__(self, func_declar_=Expr("functoin"), state_=Expr("statement"), 
                subexpr_=False, indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='functon', deps_=[func_declar_, state_],
                            vars_=vars_)
        self.sub_expr = subexpr_ 
        self.indent_level =  indent_

    def toStr(self):
        assert len(self.Deps) == 2

        self.getIndentPrefix()

        func_expr = self.Deps[0]
        state_expr = self.Deps[1]

        func_str = func_expr.toStr()
        state_str = state_expr.toStr()

        res = self._indent_prefix + func_str + ' {\n\n'
        res += state_str + '}'
        return res + self._end + '\n'

class AssignExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr(), subexpr_=False,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='assign_state', deps_=[left_, right_],
                                vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 2
        # print('AssignExpr: ', self)

        lexpr = self.Deps[0]
        rexpr = self.Deps[1]
        
        if lexpr.Type == 'nameExpr':
            lvar = lexpr._vars[-1];
        
        elif lexpr.Type == 'functino_call':
            lvar = lexpr._vars[0]
        
        else:
            raise TypeError('not supported ltype in assign tostr,' , str(lexpr))
        
        if rexpr.Type == 'nameExpr':
            rvar = rexpr._vars[-1]
            
        elif rexpr.Type == 'function_call':
            rvar = rexpr._vars[0]
        
        else:
            raise TypeError('not supported rtype in assign tostr, ', str(rexpr))
        
        
        left_str = lexpr.toStr()
        right_str = rexpr.toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        lptrStar = str()
        rptrStar = str()

        if lvar.isPtr() and rvar.Type == 'marco':
            lptrStar = '*'
        elif lvar.isPtr() and not rvar.isPtr():
            lptrStar = '*'
        elif not lvar.isPtr() and rvar.isPtr():
            rptrStar = '*'

        
        res = self._indent_prefix + lptrStar + left_str + ' = '
        res += rptrStar + right_str + ';' + self._end
        return res

class UnaryExpr(Expr):
    def __init__(self, unary_opr_=str(), expr_=Expr(), subexpr_=True,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='unary_operaExpr', deps_=[unary_opr_, expr_],
                            vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        unary_str = self.Deps[0]
        expr_ = self.Deps[1]
        assert isinstance(unary_str, str), 'unary opr need to be str type'
        assert unary_str == '-' or unary_str == '~'
        if unary_str == '~':
            unary_str = '!'
        
        if not self.sub_expr:
            self.getIndentPrefix()

        return self._indent_prefix + unary_str + expr_.toStr() + self._end
        
class BinaryExpr(Expr):
    def __init__(self, left_=Expr(), right_=Expr(), opr_=str(), vars_=list()):
        super().__init__(type_='binaryExpr', name_=opr_, deps_=[left_, right_],
                            vars_=vars_)
        self._opr = opr_
    
    def toStr(self):
        assert len(self.Deps) == 2
        # print('BinaryExpr: ', self)
        left_str = self.Deps[0].toStr()
        right_str = self.Deps[1].toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        opr_str = self._opr
        if opr_str == '~=':
            opr_str = '!='

        return left_str + ' ' + opr_str + ' ' + right_str + self._end

#! functioncall可能是非独立的语句
class FunctionCallExpr(Expr):
    def __init__(self, name_=Expr(), paralist_=Expr(), subexpr_=True,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='function_call', deps_=[name_, paralist_],
                            vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_
        # print('functionCallVar:', self._vars)

    def toStr(self):
        assert(len(self.Deps) == 2)


        func_name_expr = self.Deps[0]
        paralist_expr = self.Deps[1]

        func_name, paralist_str = '', ''
        
        if func_name_expr is not None:
            func_name = func_name_expr.toStr() 

        # function call 
        if paralist_expr is not None:
            paralist_str = paralist_expr.toStr()    
            
        tail_ = str()
        if not self.sub_expr:
            self.getIndentPrefix()
            tail_ = ';'

        res = self._indent_prefix + func_name
        res += '(' + paralist_str + ')' + tail_ + self._end 

        return res


class ParentsExpr(Expr):
    def __init__(self, expr_=Expr(), subexpr_=True,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='parentsExpr', deps_=expr_, vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        expr_str = self.Deps[0].toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        return self._indent_prefix + '(' + expr_str + ')' + self._end

class WhileExpr(Expr):
    def __init__(self, cond_=Expr(), com_=Expr(), subexpr_=False,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='while_state', deps_=[cond_, com_], vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 2
        cond_expr = self.Deps[0]
        com_expr = self.Deps[1]
        
        cond_str, com_str = '', ''

        if cond_expr is not None:
            cond_str = cond_expr.toStr()
   
        if com_expr is not None:
            com_str = com_expr.toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        res = self._indent_prefix + 'while( ' + cond_str
        res += ') {\n' + com_str + self._indent_prefix + '}'
        return res + self._end + '\n'

class ElseIfExpr(Expr):
    def __init__(self, cond_=Expr(), com_=Expr(), subexpr_=False,
                    indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='elseif_state', deps_=[cond_, com_], vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 2

        cond_expr = self.Deps[0]
        com_expr = self.Deps[1]

        cond_str, com_str = '', ''

        if cond_expr is not None:
            cond_str = cond_expr.toStr()
        
        if com_str is not None:
            com_str = com_expr.toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        res = self._indent_prefix + 'else if ( ' + cond_str
        res += ') {\n' + com_str + self._indent_prefix + '}'
        return res + self._end + '\n'

class ElseExpr(Expr):
    def __init__(self, com_=Expr(), subexpr_=False,
            indent_=HierarchicalCoding(), vars_=list()):
        super().__init__(type_='else_state', deps_=[com_], vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 1
        com_expr = self.Deps[0]
        com_str = str()
        
        if com_expr is not None:
            com_str = com_expr.toStr()

        self.getIndentPrefix()
        
        res = self._indent_prefix + 'else {\n'
        res += com_str + self._indent_prefix + '}'
        return res + self._end + '\n'


class IfExpr(Expr):
    def __init__(self, expr_=Expr(), com_=Expr(), elseif_=Expr(), else_=Expr(),
                    subexpr_=False, indent_=HierarchicalCoding(), 
                    vars_=list()):
        super().__init__(type_='if_state', deps_=[expr_, com_, elseif_, else_],
                            vars_=vars_)
        self.sub_expr = subexpr_
        self.indent_level = indent_

    def toStr(self):
        assert len(self.Deps) == 4

        if_cond_expr = self.Deps[0]
        if_com_expr = self.Deps[1]
        elseif_expr = self.Deps[2]
        else_expr = self.Deps[3]

        if_cond_str, if_com_str, elseif_str, else_str = '', '', '', ''
        if if_cond_expr is not None:
            if_cond_str = if_cond_expr.toStr()

        if if_com_expr is not None:
            if_com_str = if_com_expr.toStr()

        if elseif_expr is not None:
            elseif_str = elseif_expr.toStr()

        if else_expr is not None:
            else_str = else_expr.toStr()
        
        if not self.sub_expr:
            self.getIndentPrefix()
        
        # print('if indent level:', self.indent_level.level)

        res = self._indent_prefix + 'if ( ' + if_cond_str
        res += ' ) {\n' + if_com_str + self._indent_prefix + '}'
        
        # NOTICE !!
        res += elseif_str
        res += else_str

        return res + self._end + '\n'

class ElementExpr(Expr):
    def __init__(self, name_=Expr(), location_=None, subexpr_=True,
                        vars_=list()):
        super().__init__(type_='element', deps_=[name_, location_],
                            vars_=vars_)
        self.sub_expr = subexpr_

    def toStr(self):
        assert len(self.Deps) == 2
        name_expr = self.Deps[0]
        location_expr = self.Deps[1]

        name_str, location_str = '', ''
        if name_expr is not None:
            name_str = name_expr.toStr()

        if location_expr is not None:
            assert isinstance(location_expr, NormalExpr)
            
            ##!! NOTICE
            assert len(location_expr.Deps) > 0
            loc_ = location_expr.Deps[0]
            location_str = loc_.toStr()

        if not self.sub_expr:
            self.getIndentPrefix()

        res = self._indent_prefix + name_str + '['
        res += location_str + ']'
        return res + self._end
