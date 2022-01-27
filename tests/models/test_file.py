from datetime import datetime
import os
from pathlib import Path
import pytz
from unittest import TestCase

from src.common.constants import CUSTOM_EXCEPTIONS
from src.errors.exceptions import NotAFileException
from src.models.File import File, _check_file_integrity

CURRENT_DIRECTORY, _ = os.path.split(Path(__file__))
TEST_FILE_DIRECTORY = Path(CURRENT_DIRECTORY).joinpath('..', 'static')

EASTERN_EUROPEAN_TIMEZONE = 'EET'


class FileTestCase(TestCase):
    file = File('test', TEST_FILE_DIRECTORY, 'txt')

    def test_size_in_bytes(self):
        expected_result = 60

        result = self.file.size_in_bytes()

        self.assertEqual(result, expected_result)

    def test_size_in_kilobytes(self):
        expected_result = 0.06

        result = self.file.size_in_kilobytes()

        self.assertEqual(result, expected_result)

    def test_size_in_megabytes(self):
        expected_result = 0.00006

        result = self.file.size_in_megabytes()

        self.assertEqual(result, expected_result)

    def test_size_in_gigabytes(self):
        expected_result = 0.00000006

        result = self.file.size_in_gigabytes()

        self.assertEqual(result, expected_result)

    def test_last_modification_no_timezone(self):
        expected_result = datetime(2022, 1, 26, 21, 58, 46, 14567)

        result = self.file.last_modification()

        self.assertEqual(result, expected_result)

    def test_last_modification_with_timezone(self):
        expected_result = datetime(2022, 1, 27, 2, 58, 46, 14567)

        result = self.file.last_modification(
            pytz.timezone(EASTERN_EUROPEAN_TIMEZONE)
        )

        self.assertEqual(result, expected_result)

    def test_check_file_integrity_success(self):
        expected_result = None

        result = _check_file_integrity(Path(self.file.full_path))

        self.assertEqual(result, expected_result)

    def test_check_file_integrity_failure(self):
        expected_result = NotAFileException(
            CUSTOM_EXCEPTIONS.MESSAGES.NOT_A_FILE_EXCEPTION
        )

        with self.assertRaises(NotAFileException) as nafe:
            _check_file_integrity(Path('/not_a_file'))

        raisen_exception = nafe.exception
        self.assertEqual(raisen_exception.name, expected_result.name)
        self.assertEqual(raisen_exception.message, expected_result.message)
