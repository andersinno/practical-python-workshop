# -*- coding: utf-8 -*-

import platform
import sys

major, minor, _ = platform.python_version_tuple()
if not (major == "3" and minor == "6"):
    print('Asennetun Pythonin versio on %s. Asenna 3.6.' % platform.python_version())
    sys.exit(1)

try:
    import exifread
    import requests
    print('Ympäristö OK!')

except ImportError:
    print('Vaadittuja paketteja ei löytynyt')
