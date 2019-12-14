``exitstatus`` - POSIX exit status definitions
==============================================

.. image:: https://travis-ci.org/johnthagen/exitstatus.svg
    :target: https://travis-ci.org/johnthagen/exitstatus/

.. image:: https://codeclimate.com/github/johnthagen/exitstatus/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/exitstatus/

.. image:: https://codeclimate.com/github/johnthagen/exitstatus/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/exitstatus/

.. image:: https://codecov.io/github/johnthagen/exitstatus/coverage.svg
    :target: https://codecov.io/github/johnthagen/exitstatus/

.. image:: https://img.shields.io/pypi/v/exitstatus.svg
    :target: https://pypi.python.org/pypi/exitstatus/

.. image:: https://img.shields.io/pypi/status/exitstatus.svg
    :target: https://pypi.python.org/pypi/exitstatus/

.. image:: https://img.shields.io/pypi/pyversions/exitstatus.svg
    :target: https://pypi.python.org/pypi/exitstatus/

``exitstatus`` provides expressive, portable definitions for the
`standard POSIX exit codes <https://www.gnu.org/software/libc/manual/html_node/Exit-Status.html>`__.
While Python does provide some Unix-specific exit status codes in the
`os module <https://docs.python.org/3/library/os.html#os._exit>`__, they are not portable to
all platforms and are missing the generic failure case.


Installation
------------

You can install, upgrade, and uninstall ``exitstatus`` with these commands:

.. code:: shell-session

    $ pip install exitstatus
    $ pip install --upgrade exitstatus
    $ pip uninstall exitstatus

On Python 3.4+, the standard library
`enum <https://docs.python.org/3/library/enum.html>`__ is used, on older versions
`enum34 <https://pypi.python.org/pypi/enum34>`__ is installed as a dependency.

Usage
-----

Exit status codes are defined in a simple to use
`IntEnum <https://docs.python.org/3/library/enum.html#enum.IntEnum>`__.

.. code:: python

    import sys
    from exitstatus import ExitStatus

    sys.exit(ExitStatus.success)

Releases
--------

1.4.0 2019-12-14
^^^^^^^^^^^^^^^^

- Drop Python 3.4 and support Python 3.8.
- Include license file.

1.3.0 - 2018-07-09
^^^^^^^^^^^^^^^^^^

Drop Python 3.3 and support Python 3.7.

1.2.0 - 2016-12-31
^^^^^^^^^^^^^^^^^^

Support Python 3.6.

1.1.0 - 2016-10-11
^^^^^^^^^^^^^^^^^^

Add docstrings and simplify checking for ``enum34`` dependency need.

1.0.0 - 2016-06-10
^^^^^^^^^^^^^^^^^^

Initial release.