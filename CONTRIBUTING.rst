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

To set up the project for development, you need:

- PhantomJS or Firefox installed in the ``PATH`` as ``phantomjs`` or
  ``firefox``, respectively.
- The ``DJANGO_SETTINGS_MODULE`` exported as
  ``healthmonitor.settings``.
- Then, run ``make setup`` to install and prepare the environment.

Afterwards, you could be able to do ``make done`` to run both feature
and unit tests. If this fails, your contribution won't be accepted.
