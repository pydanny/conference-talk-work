===========
Exceptions
===========

.. parsed-literal::

    Errors should never pass silently.
    Unless explicitly silenced.

.. epigraph::

    "Generic Exceptions are the devil." 
    
    -- Myself and most of the people reading this slide.
    
This is bad:

.. code-block:: python

    for package in Package.objects.all():
        try:
            package.fetch_metadata()
            package.fetch_commits()
        except socket_error, e:
            text += "\nFor '%s', threw a socket_error: %s" % (package.title, e)
            continue
        # snip many exceptions
        except Exception, e:
            text += "\nFor '%s', General Exception: %s" % (package.title, e)
            continue
            
    # email later
            
a.k.a. - What am I thinking?!? This is effectively what's happening

.. code-block:: python

    >>> try:
    ...     a = b
    ... except Exception as e:
    ...     print(e)
    ... 
    name 'b' is not defined
    
I'm getting the message type but not the error type. I'm losing data on my errors. If I just run the code in a prompt I get:

.. code-block:: python

    >>> a= b
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'b' is not defined

If I'm smart, I can get all the data:

.. code-block:: python

    >>> class CustomErrorHandler(Exception):
    ...     def __init__(self, error):
    ...             print(error)
    ... 
    >>> try:
    ...     a=b
    ... except Exception as e:
    ...     raise CustomErrorHandler(e)
    ... 
    name 'b' is not defined
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    __main__.CustomErrorHandler
        
This might be better:

.. code-block:: python

    class PackageUpdaterException(Exception):
        def __init__(self, error, title):
            log_message = "For {title}, {error_type}: {error}".format(
                title=title,
                error_type=type(error),
                message=error
            )
            logging.error(log_message)
            logging.exception() # This captures the whole traceback!!!
        
    for package in Package.objects.all():
        try:
            try:
                package.fetch_metadata()
                package.fetch_commits()
            except Exception, e:
                raise PackageUpdaterException(e, package.title)
        except PackageUpdaterException:
            continue
            
    # email me the log file later