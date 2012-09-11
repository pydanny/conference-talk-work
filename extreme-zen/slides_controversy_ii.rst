==============
Controversy II
==============

.. parsed-literal::

    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.

.. parsed-literal::

    You try to shoot yourself in the foot, only to realize there’s no need, since Guido thoughtfully shot you in the foot years ago.
    
    -- Nick Mathewson, comp.lang.python
    
Decorators make code looks pretty, but writing them maybe isn't zenful.
===========================================================================

**Is this obvious to the Dutch?**

A sample memoize decorator of the sort you find on the Internets:

.. code-block:: python

    def memoize(func):
        cache = {}

        def memoized(*args):
            # do something before invocation
            if args in cache:
                return cache[args]
            result = cache[args] = func(*args)
            return result

        return memoized
    
Decorating a function:

.. code-block:: python

    @memoize
    def allcaps(string):
        return string.upper()
        

    def multiplier(multiple):
        def decorator(function):
            def wrapper(*args, **kwargs):           
                return function(*args, **kwargs) * multiple
            return wrapper
        return decorator
        
    @multiplier(3)
    def allcaps(string):
        return string.upper()


Decorating with arguments:

.. code-block:: python

    def authorization(roles):
        def decorator(function):
            def wrapper(*args, **kwargs):
                rights = args[0].get('rights', ())
                for right in rights:
                    if right in roles:
                        return function(*args, **kwargs)
                raise Exception("You don't have the right!")
            return wrapper
        return decorator
    
    @authorization('admin')
    def do_admin_thing(user):
        # do something administrative
        return user
        
.. code-block:: python

    >>> admin_user = {'name':'Admin', 'rights':['admin',]}    
    >>> do_admin_thing(admin_user)
    >>> user = {'name':'User'}
    >>> do_admin_thing(user)
      File "<stdin>", line 8
        raise Exception('You don't have the right!')
                                 ^
    SyntaxError: invalid syntax
    
What am I forgetting?

Decorating with arguments:

.. code-block:: python

    import functools 
    def authorization(roles):
        def decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                rights = args[0].get('rights', ())
                for right in rights:
                    if right in roles:
                        return function(*args, **kwargs)
                raise Exception("You don't have the right!")
            return wrapper
            wrapper.__docstring__ = function.__docstring__
        return decorator
    
    @authorization('admin')
    def do_admin_thing(user):
        # do something administrative
        return user
        
Any implementation of closure is bound to be a bit confusing. Python's decorators are really nice once written, but the process of writing them is not obvious. 

This is the one way to write decorators? Is this really obvious to the Dutch? 

Let me show you the trail of logic... (arrow thingees here)

Given time, everyone is smart enough to figure this out. And the decorator syntax is really nice. Which leads me to the following:

* The rise of convention over configuration.

    * XML/CFG or naming conventions?
    * Django gives nice things based on PEP-8 (forms and admin)

* New APIs should reflect this:

    * Writing a hard-to-use API doesn't convince anyone anymore of your intelligence or prowess.
    * Job security via API obfuscation is a terrible thing to do to the humans around you.
    * Django/Pyramid/Flask/etc vs Zope
    * requests vs urllib/urllib2/httplib2