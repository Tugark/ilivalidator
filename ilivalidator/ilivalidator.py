import platform
import json

from ctypes import *
from importlib_resources import files
from .settings import Settings
from typing import Optional

if platform.uname()[0] == "Windows":
    lib_name = "libilivalidator.dll"
elif platform.uname()[0] == "Linux":
    lib_name = "libilivalidator.so"
else:
    lib_name = "libilivalidator.dylib"

class Ilivalidator:
    @staticmethod
    def validate(data_file_names: list, settings: Optional[Settings] = None) -> bool:
        lib_path = files('ilivalidator.lib_ext').joinpath(lib_name)
        # str() seems to be necessary on windows: https://github.com/TimDettmers/bitsandbytes/issues/30
        dll = CDLL(str(lib_path))
        isolate = c_void_p()
        isolatethread = c_void_p()
        dll.graal_create_isolate(None, byref(isolate), byref(isolatethread))
        dll.ilivalidator.restype = bool

        data_file_names_string = ';'.join(data_file_names)

        # because we're inheriting from dict, the normal json.dumps() does not return the proper chunks, so we call it on __dict__ directly.
        if settings is None:
            settings_string = json.dumps({})
        else:
            settings_string = json.dumps(settings.__dict__)

        result = dll.ilivalidator(isolatethread, c_char_p(bytes(data_file_names_string, "utf8")), c_char_p(bytes(settings_string, "utf8")))
        return result
