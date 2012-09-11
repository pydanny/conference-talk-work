==============
Opening stanza 
==============

.. parsed-literal::

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    
Also include:

.. parsed-literal::

    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    
 * http://www.codinghorror.com/blog/2008/07/spartan-programming.html
 * Minimalism isn't always the right choice, but it's rarely the wrong choice.
 * Don't do hard things. Do easy things.
 * Anytime you can excise lines of code, you are doing it right - but don't use that as an excuse to obfuscate.
 * Anytime you alias a class to a function to make calling it easier, then you should consider rethinking your need for a class.
 
Ideas:

 * Spartan programming techniques
 * Descriptive naming patterns
 * Good documentation patterns
 * Inheritance

.. code-block:: python

    import math
    class Circle(object):

        def __init__(self, radius):
            self.radius = radius
        
        def area(self):
            return self.radius ** 2 *math.pi
        
        def __repr__(self):
            return '{0} as area {1}'.format(
                self.__class__.__name__, self.area()
            )
        
    class Ring(Circle):

        def __init__(self, outer, inner):
            # Going up the chain. But especially with multiple inheritance, we risk not
            # properly understanding the inheritance chain
            super(Ring, self).__init__(outer)
            self.inner = inner

        def area(self):
            outer, inner = self.radius, self.inner
            return Circle(outer).area() - Circle(inner).area()
        
    class Ring2(Circle):

        def __init__(self, outer, inner):
            # This is more explicit than super because super can ding you on 
            #   Multiple Inheritance.
            # Super can call things outside your inheritance chain.
            # Explicit is better than implicit
            Circle.__init__(self, outer) 
            self.inner = inner
    
        def area(self):
            outer, inner = self.radius, self.inner
            return Circle(outer).area() - Circle(inner).area()
            
.. code-block:: python

    >> Circle(10)
    Circle as area 314.159265359
    >>> Ring(10, 5)
    235.619449019
    >>> Ring2(10, 5)
    235.619449019
    
.. code-block:: python

    def form_valid(self, form):
        verb_form_base = self.get_verb_form(self.request.POST.get("verb_slug", None))
        verb_form = verb_form_base(self.request.POST)
        if verb_form.is_valid():
            form.instance.verb_attributes = verb_form.cleaned_data
        return super(ActionUpdateView, self).form_valid(form)

    class ActionUpdateView(
                LoginRequiredMixin, # django-braces
                ActionBaseView, # inherits from AuthorizedForProtocolMixin
                AuthorizedforProtocolEditMixin, # Checks rights on edit views
                VerbBaseView, # Gets one of 200+ verb forms
                UpdateView): # django.views.generic.BaseView

        def form_valid(self, form):
            verb_form_base = self.get_verb_form(self.request.POST.get("verb_slug", None))
            verb_form = verb_form_base(self.request.POST)
            if verb_form.is_valid():
                form.instance.verb_attributes = verb_form.cleaned_data
            return super(ActionUpdateView, self).form_valid(form)
            return UpdateView.form_valid(self, form)
            
.. code-block:: python

    <class 'actions.views.ActionUpdateView'>
    <class 'braces.views.LoginRequiredMixin'>
    <class 'actions.views.ActionBaseView'>
    <class 'core.views.AuthorizedForProtocolMixin'>
    <class 'core.views.AuthorizedforProtocolEditMixin'>
    <class 'verbs.views.VerbBaseView'>
    <class 'django.views.generic.edit.UpdateView'>
    <class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>
    <class 'django.views.generic.base.TemplateResponseMixin'>
    <class 'django.views.generic.edit.BaseUpdateView'>
    <class 'django.views.generic.edit.ModelFormMixin'>
    <class 'django.views.generic.edit.FormMixin'>
    <class 'django.views.generic.detail.SingleObjectMixin'>
    <class 'django.views.generic.edit.ProcessFormView'>
    <class 'django.views.generic.base.View'>
    <type 'object'>
    
.. code-block:: python

    for x in [x for x in ActionUpdateView.mro() if hasattr(x, "form_valid")]:
        print x