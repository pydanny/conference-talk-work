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

.. code-block:: python

    # The part for creating research lab actions
    # Lets us save a second form called 'Verb' to a JSON field within the Action 

    def form_valid(self, form):
        self.protocol = self.get_protocol()  # get the research protocol from the URL slug
        form.instance.step = self.get_step()  # get the protocol step from the URL slug
        verb_form_base = self.get_verb_form(self.request.POST.get("verb_slug", None)) # get the vern
        verb_form = verb_form_base(self.request.POST) # instantiate the verb
        if verb_form.is_valid():
            form.instance.verb_attributes = verb_form.cleaned_data # save the data
        return super(ActionCreateView, self).form_valid(form)
        
# Pretty straightforward. But it's ravioli or pirogies code.
        
.. code-block:: 

    class ActionCreateView(LoginRequiredMixin, # django-braces
                            ActionBaseView, # inherits from AuthorizedForProtocolMixin
                            AuthorizedforProtocolEditMixin, # Checks rights on edit views
                            VerbBaseView, # Gets one of 200+ verb forms
                            CreateView): # django.views.generic.BaseView

Several hundred lines of code.

* Could have done it in functional views more quickly.
* Functional view is probably easier to test
* *But* ``AuthorizedforProtocolEditMixin`` came after everything else.

