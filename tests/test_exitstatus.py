import sys

import pytest

from exitstatus import ExitStatus


def test_equality() -> None:
    assert ExitStatus.success == 0
    assert ExitStatus.failure == 1


def test_value() -> None:
    assert ExitStatus.success.value == 0
    assert ExitStatus.failure.value == 1


def test_identity() -> None:
    assert ExitStatus.success is ExitStatus.success
    assert ExitStatus.success is not ExitStatus.failure


def test_sys_exit() -> None:
    with pytest.raises(SystemExit):
        sys.exit(ExitStatus.success)


def test_exit() -> None:
    with pytest.raises(SystemExit):
        exit(ExitStatus.success)
