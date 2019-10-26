from cx_Freeze import setup, Executable

build_exe_options = {"packages" : ["vlc", "tkinter"]}

setup(  name = "Radio",
        version = "0.0.1",
        description = "Online radio GUI",
        options = {"build_exe": build_exe_options},
        executables = [Executable("radio.py", base=None)])