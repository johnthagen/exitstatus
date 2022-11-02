``exitstatus`` - POSIX exit status definitions
==============================================

.. image:: https://github.com/johnthagen/exitstatus/workflows/python/badge.svg
    :target: https://github.com/johnthagen/exitstatus/actions

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

2.3.0 2022-11-02
^^^^^^^^^^^^^^^^

- Add ``py.typed`` file to package to support Mypy type checking.
- Refactor the project into an installable package rather than an installable module.
- Drop support for Python 3.7

2.2.0 2021-11-06
^^^^^^^^^^^^^^^^

- Support Python 3.10 and drop 3.6.

2.1.0 2020-12-27
^^^^^^^^^^^^^^^^

- Drop Python 3.5 and support Python 3.9.
- Switch to GitHub Actions for CI.

2.0.1 2020-04-26
^^^^^^^^^^^^^^^^

- Update LICENSE file.

2.0.0 2020-03-29
^^^^^^^^^^^^^^^^

- Drop Python 2.7 support.

1.4.1 2020-03-29
^^^^^^^^^^^^^^^^

- Add ``python_requires`` field to ``setup.py``.

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
