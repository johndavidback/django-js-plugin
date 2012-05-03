django-js-plugin
================

A demonstration on how to create a js widget with Django. This is the foundation of what could
be a widget similar to the FB Like button, or any other asynchronously loaded script.

The Basics
----------

If you take a look at the templates, you can see basically what happens.

We want to load a widget onto our page.  Easy.  The cool part about this is that using
render_to_string to load the widget, you could pass in all kinds of neat things into it
to make it dynamic or user oriented. We could tack an account number or something
like that onto the request for widget.js for a personal experience. 

It isn't fancy yet, but it offers the basis for a dynamic javascript widget.

Based on
--------
This article: http://alexmarandon.com/articles/web_widget_jquery/ by Alex Marandon