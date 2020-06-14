import shutil

from cx_Freeze import setup, Executable

includes = ["net_util", "cx_Freeze", "platform", "subprocess"]
excludes = ["tkinter", "test", "unittest", "pydoc", "http", 'multiprocessing.Pool']
packages = ["os", "platform", "net_util", "concurrent", "subprocess", "platform"]
build_exe_options = {"excludes": excludes, "optimize": 2}
mainScript = "main.py"
exeIcon = "icons/ping.ico"
exeName = "validation.exe"

base = None
# if sys.platform == "win32":
#     base = "Win32GUI"


exe = Executable(script=mainScript, base=base, icon=exeIcon, targetName=exeName)
shutil.rmtree('build', ignore_errors=True)

setup(name="validation",
      version="0.1",
      description="My Network util console application!",
      options={"build_exe": build_exe_options},
      executables=[exe])
