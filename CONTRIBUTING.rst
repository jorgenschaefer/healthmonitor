==================================
Contributing to the Health Monitor
==================================

To contribute, please open a pull request with the user story you wish
to implement. The commit message should note which user story (via
issue number) is being addressed by this commit. A user story is only
*done* when the conditions in the section *Definition of Done* are
met.

For smaller bugs, a user story is not necessary. Please explain the
nature of the bug in the pull request. While this does not require a
feature test, a unittest that tests for the specific bug is required.

Definition of Done
==================

A user story (or issue) is *done* when the following conditions are
met:

- There are no PEP8 errors.
- There is a feature test for the user story.
- The coverage of unittests is above 95%.
- All feature tests pass.
- All unit tests pass.

This also applies to pull requests.

Development Setup
=================

The healthmonitor package requires the following programs in your
``PATH``:

- ``pyvenv-3.4``
- ``phantomjs`` or ``firefox``
- ``npm``

Then run ``make devel``. This should set up a development environment,
including virtualenv.

Once you have made your changes, you should use ``make check`` to
check for the *definition of done* to be fulfilled. If this fails,
your contribution won't be accepted.
