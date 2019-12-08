import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["vlc", "tkinter", "json", "requests", "time", "sys"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Padio",
        version = "0.1.0",
        description = "Online radio GUI",
        options = {"build_exe": build_exe_options},
        executables = [Executable("radio.py", base=base)])
