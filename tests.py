import sys
import unittest

from exitstatus import ExitStatus


class ExitStatusTestCase(unittest.TestCase):
    def test_equality(self) -> None:
        self.assertEqual(ExitStatus.success, 0)
        self.assertEqual(ExitStatus.failure, 1)

    def test_value(self) -> None:
        self.assertEqual(ExitStatus.success.value, 0)
        self.assertEqual(ExitStatus.failure.value, 1)

    def test_identity(self) -> None:
        self.assertIs(ExitStatus.success, ExitStatus.success)
        self.assertIsNot(ExitStatus.success, ExitStatus.failure)

    def test_sys_exit(self) -> None:
        with self.assertRaises(SystemExit):
            sys.exit(ExitStatus.success)

    def test_exit(self) -> None:
        with self.assertRaises(SystemExit):
            exit(ExitStatus.success)
