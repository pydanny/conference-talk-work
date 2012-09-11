=================================
Getting it done vs Technical Debt
=================================

.. parsed-literal::

    Now is better than never.
    Although never is often better than *right* now.
    Namespaces are one honking great idea -- let's do more of those!

 * Refactor Mercilessly
 * Do The Simplest Thing That Could Possibly Work
 * First law of programming http://www.c2.com/cgi/wiki?FirstLawOfProgramming
 
    Quality software takes the least amount of time to develop. If you have code that is simple as possible, tests that are complete and a design that fits just right, additions and changes happen in the fastest possible way because the impact is lowest. Consequently, if you hack something out, the more you hack the slower you go because the cost of addition or change grows with each line of code.
 
Getting it done
=================

 * Python empowers you with the ability to write code fast.
 * Which means you can paint yourself into a corner.
 * Or ignore critical components like docs and tests.

What you can't fail to document. Ever.
======================================

 * Version. In your docs and in the ``__version__`` variable.
 * Basic concepts for what the project does.
 * Installation and setup of your project. 
 * Unless your tool is extremely specific to an operating system, cover the big three:
 
    * Linux (choose popular flavors. People who use other flavors are smart enough to figure it out on their own)
    * Mac OS X
    * Latest decent version of Windows (Which means you can skip Vista)
    
Tools to generate Python tests quickly.
=============================================

* http://pythoscope.org/

Getting it done
===============

For any reasonable large set of code, if you import * your will likely be cementing it into the module, unable to be removed. This is because it is difficult to determine what items used in the code are coming from 'module', making it east to get to the point where you think you don't use the import any more but its extremely difficult to be sure.

.. code-block:: python

    import re
    import os
    from twisted.internet import protocol, reactor
    from django import forms

.. code-block:: python

    from re import *
    from os import *
    from twisted import *
    from django.forms import *
    
.. code-block:: python

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
                    
.. code-block:: python

    >>> import string
    >>> import re
    >>> import os
    
    >>> compare(os, re)
    Comparing os, re:
    * sys    
    * error

    >>> re.sys == os.sys
    True
    
    >>> re.error == os.error
    False

    >>> compare(re, string)
    * splint
    
                    
.. code-block:: python

    def compare_builtins(mod1):
        print("\nComparing {0} to builtins:".format(mod1.__name__))
        for x in dir(mod1):
            for y in dir(globals()['__builtins__']):
                if x == y and not x.startswith('_'):
                    print("* GLOBAL: {0}".format(x))

.. code-block:: python

    >>> compare_builtins(re)
    Comparing re to builtins:
    * GLOBAL: compile    
    >>> compare_builtins(os)
    Comparing os to builtins:
    * GLOBAL: open
    
.. parsed-literal::

    Help on built-in function open in module posix:

    open(...)
        open(filename, flag [, mode=0777]) -> fd
    
        Open a file (for low level IO).
        
.. parsed-literal::

    Help on built-in function open in module __builtin__:

    open(...)
        open(name[, mode[, buffering]]) -> file object
    
        Open a file using the file() type, returns a file object.  This is the
        preferred way to open a file.  See file.__doc__ for further information.