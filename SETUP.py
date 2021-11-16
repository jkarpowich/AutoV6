from cx_Freeze import setup, Executable

base = None    

executables = [Executable("AutoV5.py", base=base)]

packages = ["asyncio", "sys", "auraxium", "tkinter", "colorsys", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Auto V5",
    options = options,
    version = "1.0",
    description = 'Auto V5',
    executables = executables
)
