################ Lispy: Scheme Interpreter in Python

## (c) Peter Norvig, 2010-14; See http://norvig.com/lispy.html

################ Types

from __future__ import division


Symbol = str
Number = (int, float)
List = list


def tokenize(chars):
    """
    Convert a string of characters into a list of tokens.
    """
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program):
    """
    Read a schema expression from a string
    """
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
    """
    Read an expression from a sequence of tokens.
    """
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')

    token = tokens.pop(0)

    if "(" == token:
        L = []
        while tokens[0] != ")":
            L.append(read_from_tokens(tokens))

        tokens.pop(0) # Pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    """
    Numbers become numbers, every other token is a symbol
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


class Env(dict):
    """
    An environment: a dict of {'var':val} pairs, with an outer Env
    """

    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var):
        """
        Find the innermost Env where var appears
        """
        return self if (var in self) else self.outer.find(var)

def standard_env():
    """
    An environment with some Schema standard procedures
    """
    import math, operator as op
    env = Env()
    env.update(vars(math)) #sin, cos, sqrt, pi, ...
    env.update({
        '+': op.add, '-': op.sub, '*': op.mul, '/': op.div,
        '>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '=': op.eq,
        'abs': abs,
        'append': op.add,
        'apply': apply,
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'eq?': op.is_,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'map': map,
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, Number),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env

global_env = standard_env()


def eval(x, env=global_env):
    """
    Evaluate an expression in an environment
    """
    if isinstance(x, Symbol):  #variable reference
        return env.find(x)[x]
    elif not isinstance(x, List): # constant literal
        return x
    elif x[0] == 'quote': #(quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if': # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':  #(define var exp)
        (_, var, exp) = x
        env[var] = eval(exp, env)
    elif x[0] == 'set!':  #(set! var exp)
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif x[0] == 'lambda': #(lambda (var...) body)
        (_, parms, body) = x
        return Procedure(parms, body, env)
    else:
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)

class Procedure:
    """
    A user-defined Scheme procedure
    """
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env

    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

def repl(prompt='lis.py> '):
    """
    A prompt-read-eval-print-loop
    """
    while True:
        val = eval(parse(raw_input(prompt)))
        if val is not None:
            print lispstr(val)

def lispstr(exp):
    """
    Convert a Python object back into a Scheme-readable string
    """
    if isinstance(exp, list):
        return "(" + ' '.join(map(lispstr, exp)) + ')'
    else:
        return str(exp)


program = "(begin (define r 10) (* pi (* r r)))"
print program
print "tokenize:", tokenize(program)
print "parse:", parse(program)

print "==================="
print "(define r 10)"
eval(parse("(define r 10)"))
print "(* pi (* r r))"
print eval(parse("(* pi (* r r))"))

print "==================="
print "(define circle-area (lambda (r) (* pi (* r r))))"
print "(circle-area 10)"
repl()

