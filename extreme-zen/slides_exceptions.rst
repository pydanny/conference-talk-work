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
            
a.k.a. - What am I thinking?!?
        
This might be better:

.. code-block:: python

    class PackageUpdaterException(Exception):
        def __init__(self, message, title):
            log_message = "For {title}, {error_type}: {message}".format(
                title=title,
                error_type=type(message),
                message=message
            )
            logging.error(log_message)
        
    for package in Package.objects.all():
        try:
            package.fetch_metadata()
            package.fetch_commits()
        except Exception, e:
            raise PackageUpdaterException(e)
            
    # email me the log file later