import sys
import ctypes
import subprocess

def IsAdmin() -> bool:
    """
    Проверяет запущен ли процесс с правами администратора.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except:
        return False

def RunAsAdmin():
    """
    Перезапускает текущий процесс с правами администратора.
    """
    if IsAdmin():
        return

    args = subprocess.list2cmdline(sys.argv)

    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        args,
        None,
        1
    )

    sys.exit()