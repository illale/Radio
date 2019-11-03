from cx_Freeze import setup, Executable

build_exe_options = {"packages" : ["vlc", "tkinter", "json", "requests", "time", "sys"]}

setup(  name = "Radio",
        version = "0.1.1",
        description = "Online radio GUI",
        options = {"build_exe": build_exe_options},
        executables = [Executable("radio.py", base=None)])
