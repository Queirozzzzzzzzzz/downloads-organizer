import os
import sys
import subprocess
import winreg as reg 

app_name = "main.py"

def get_app_path():
    path = os.path.dirname(os.path.realpath(__file__))  
    address = os.path.join(path, app_name) 

    return address

def get_runnable():
    py_executable = sys.executable
    app_path = get_app_path()
    runnable = f'"{py_executable}" "{app_path}"'

    return runnable
 
def add_to_registry():
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open,"downloads-organizer", 0, reg.REG_SZ, get_runnable())
    reg.CloseKey(open)

def run_app():
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    subprocess.Popen(["python", app_name], startupinfo=startupinfo, start_new_session=True)
 
if __name__=="__main__":
    add_to_registry()
    run_app()