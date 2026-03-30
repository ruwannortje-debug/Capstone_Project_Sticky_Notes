Project Modules
===============

This section documents the main modules that power the Sticky Notes
application.

notes.models
------------

The ``notes.models`` module defines the database structure for the application.
It currently contains the ``Note`` model, which stores a note title, note
content, and the creation timestamp.

.. automodule:: notes.models
   :members:
   :undoc-members:
   :show-inheritance:

notes.forms
-----------

The ``notes.forms`` module contains the ``NoteForm`` model form used to create
and update notes through the web interface.

.. automodule:: notes.forms
   :members:
   :undoc-members:
   :show-inheritance:

notes.views
-----------

The ``notes.views`` module contains the function-based views responsible for
listing notes, showing note details, creating notes, updating notes, and
deleting notes.

.. automodule:: notes.views
   :members:
   :undoc-members:
   :show-inheritance:

notes.urls
----------

The ``notes.urls`` module maps incoming requests to the appropriate view
functions.

.. automodule:: notes.urls
   :members:
   :undoc-members:
   :show-inheritance:

sticky_notes.settings
---------------------

The ``sticky_notes.settings`` module defines the Django project configuration,
including installed apps, middleware, templates, static files, and database
settings.

.. automodule:: sticky_notes.settings
   :members:
   :undoc-members:
   :show-inheritance:
