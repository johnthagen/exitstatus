# exitstatus — POSIX exit status definitions

[![GitHub Actions][github-actions-badge]](https://github.com/johnthagen/exitstatus/actions)
[![uv][uv-badge]](https://github.com/astral-sh/uv)
[![Nox][nox-badge]](https://github.com/wntrblm/nox)
[![Ruff][ruff-badge]](https://github.com/astral-sh/ruff)
[![Type checked with mypy][mypy-badge]](https://mypy-lang.org/)
[![PyPI version](https://img.shields.io/pypi/v/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)
[![PyPI status](https://img.shields.io/pypi/status/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/exitstatus.svg)](https://pypi.python.org/pypi/exitstatus/)

[github-actions-badge]: https://github.com/johnthagen/exitstatus/actions/workflows/ci.yml/badge.svg
[uv-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
[nox-badge]: https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[mypy-badge]: https://www.mypy-lang.org/static/mypy_badge.svg

`exitstatus` provides expressive, portable definitions for the
[standard POSIX exit codes](https://www.gnu.org/software/libc/manual/html_node/Exit-Status.html).
While Python does provide some Unix-specific exit status codes in the
[`os` module](https://docs.python.org/3/library/os.html#os._exit), they are not portable to
all platforms and are missing the generic failure case.

## Installation

You can add `exitstatus` to your project with `uv` using:

```bash
uv add exitstatus
```

## Usage

Exit status codes are defined in a simple to use
[`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum).

```python
import sys
from exitstatus import ExitStatus

sys.exit(ExitStatus.success)
```
