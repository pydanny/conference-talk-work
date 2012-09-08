===========
Controversy
===========

.. parsed-literal::

    Special cases aren't special enough to break the rules.
    Although practicality beats purity.

Django
======

A few areas that have made Django a pain point for some people:

* How Django handles configuration and installation
* Django and WSGI (solved)
* Class based views

Django isn't Model-View-Control compliant
-----------------------------------------

http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

It's being argued in and out of the Python that MVC is not really meant for the web. My own take on it is that what Django really cares about is separation of presentation from content. 


Django's handling of configuration and installation
---------------------------------------------------

Django's configuration and installation is intuitive to a lot of incoming developers. It's been argued that this makes it a bit harder for upstream developers on other projects, but I've yet to hear anything but undetailed anecdotes.

Django class based views
------------------------

Let's face it, Django's implementation of class based views is not as intuitive as other frameworks. Improved documentation and accessory libraries help, but CBVs remain a barrier of entry. While the simplest of views can be rendered via cut-and-paste coding, sophisticated techniques using CBVs are for experienced developers only. 

TODO: Two form Django CBV vs functional view goes here


Web2py
======

Web2py commonly uses implicit over explicit behavior. For example, in this module in the evote/models directory authored by Massimo di Pierro, the response object already exists:

.. code-block:: python

    # encoding: utf-8
    # https://github.com/mdipierro/evote/blob/master/models/menu.py    
    # this file is released under public domain and you can use without limitations

    response.title = 'Voting Service'
    response.subtitle = None

    ## read more at http://dev.w3.org/html5/markup/meta.name.html
    response.meta.author = 'Your Name <you@example.com>'
    response.meta.description = 'a cool new app'
    response.meta.keywords = 'web2py, python, framework'
    response.meta.generator = 'Web2py Web Framework'

    #snip more content

Web2py grossly violatesthe Zen of Python statement `Special cases aren't special enough to break the rules.` Yet the success of Web2py, especially in terms of it's ability to be taught quickly to beginners arguably proves that ` practicality beats purity.` 

On a side note, as someone who has worked very hard on numerous occasions to get the right Python and Django components installed on student machines, I can say that I'm rather jealous of how easily Web2py makes it for instructors and students to get things running fast.

Conclusion
==========

The Zen of Python is a set of guidelines. While it's good to be able to argue and discuss the points of the poem, we need to remember that it's a guideline that we are encouraged to follow, not a formal set of laws (unless the PSF votes it so).

