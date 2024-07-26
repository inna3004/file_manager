import unittest
import os.path
from pathlib import Path

from main_File_manager import print_file

path = Path('.')


def test_print_file(print_file):
    assert (print_file == 1)
