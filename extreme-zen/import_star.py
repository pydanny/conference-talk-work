import os
import re
import string


def compare(mod1, mod2):
    title = '\nComparing {0}, {1}:'.format(
            mod1.__name__,
            mod2.__name__
            )
    print(title)
    for x in dir(mod1):
        for y in dir(mod2):
            if x == y and not x.startswith('_'):
                print("* " + x)


compare(os, re)
compare(re, string)
compare(os, string)

#compare2 = lambda mod1, mod2: [x for x in dir(mod1) if x in dir(mod2) and not x.startswith('_')]



def compare_builtins(mod1):
    print("\nComparing {0} to builtins:".format(mod1.__name__))
    for x in dir(mod1):
        for y in dir(globals()['__builtins__']):
            if x == y and not x.startswith('_'):
                print("* GLOBAL: {0}".format(x))


compare_builtins(re)
compare_builtins(os)
