Sticky Notes Documentation
==========================

Welcome to the documentation for the Sticky Notes Django application. This guide
covers the project structure, setup requirements, and the main Python modules
used to create, display, update, and delete notes.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   modules

Project Summary
---------------

Sticky Notes is a lightweight Django web application that lets users manage
short notes in a clean interface. The application demonstrates the following:

* Django models for persistent note storage.
* Model forms for creating and editing notes.
* Function-based views for CRUD operations.
* URL routing for the notes workflow.
* Static styling and templates for a user-friendly interface.

How to Build the HTML Documentation
-----------------------------------

From the ``docs`` folder, run one of the following commands:

* Windows: ``make.bat html``
* Linux/macOS: ``make html``

The generated HTML output will be available in ``docs/build/html``.
