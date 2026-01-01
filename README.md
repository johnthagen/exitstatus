# exitstatus — POSIX exit status definitions

[![GitHub Actions][github-actions-badge]](https://github.com/johnthagen/exitstatus/actions)
[![Codecov](https://codecov.io/github/johnthagen/exitstatus/coverage.svg)](https://codecov.io/github/johnthagen/exitstatus/)
[![PyPI version](https://img.shields.io/pypi/v/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)
[![PyPI status](https://img.shields.io/pypi/status/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)

[github-actions-badge]: https://github.com/johnthagen/exitstatus/actions/workflows/ci.yml/badge.svg

`exitstatus` provides expressive, portable definitions for the
[standard POSIX exit codes](https://www.gnu.org/software/libc/manual/html_node/Exit-Status.html).
While Python does provide some Unix-specific exit status codes in the
[`os` module](https://docs.python.org/3/library/os.html#os._exit), they are not portable to
all platforms and are missing the generic failure case.

## Installation

You can install, upgrade, and uninstall `exitstatus` with these commands:

```bash
pip install exitstatus
pip install --upgrade exitstatus
pip uninstall exitstatus
```

## Usage

Exit status codes are defined in a simple to use
[`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum).

```python
import sys
from exitstatus import ExitStatus

sys.exit(ExitStatus.success)
```
