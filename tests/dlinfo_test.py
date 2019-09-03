import ctypes
import os

import pytest

from dlinfo import DLInfo


@pytest.mark.parametrize('lib_name', [
    'c',
    'dl',
])
def test_dlinfo_path(lib_name):
    lib_filename = ctypes.util.find_library(lib_name)
    lib = ctypes.cdll.LoadLibrary(lib_filename)
    dlinfo = DLInfo(lib)
    assert os.path.exists(dlinfo.path)
    assert os.path.isabs(dlinfo.path)
    assert lib_filename == os.path.basename(dlinfo.path)
