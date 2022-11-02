"""Provides portable POSIX exit codes in the form of an IntEnum."""

import enum


@enum.unique
class ExitStatus(enum.IntEnum):
    """Portable definitions for the standard POSIX exit codes."""

    success = 0
    """Indicates successful program completion."""

    failure = 1
    """Indicates unsuccessful program completion in a general sense."""
