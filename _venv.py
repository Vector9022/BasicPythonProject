import os
import sys
import subprocess
from pathlib import Path

PYTHON_VERSION = "3.12"
VENV_DIR = Path("venv")

# =========================
# БАЗОВЫЕ ФУНКЦИИ
# =========================
def GetPythonExecutable():
    try:
        result = subprocess.run(
            ["py", f"-{PYTHON_VERSION}", "-c", "import sys; print(sys.executable)"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        print(f"Не удалось найти Python {PYTHON_VERSION}, используется \"{sys.executable}\".")
        return sys.executable

def GetVenvPython():
    return VENV_DIR / "Scripts" / "python.exe"

def BuildEnv():
    env = os.environ.copy()
    env["VIRTUAL_ENV"] = str(VENV_DIR.resolve())

    # PATH
    env["PATH"] = str((VENV_DIR / "Scripts").resolve()) + os.pathsep + env["PATH"]

    # PYTHONPATH
    cwd = str(Path.cwd())
    env["PYTHONPATH"] = cwd + os.pathsep + env.get("PYTHONPATH", "")

    return env

def EnsureVenv():
    if not VENV_DIR.exists():
        print("Создание виртуального окружения...")
        pythonExe = GetPythonExecutable()
        subprocess.check_call([pythonExe, "-m", "venv", str(VENV_DIR)])
        return True
    else:
        return False

def InstallRequirements():
    venvPython = GetVenvPython()
    reqFile = Path("requirements.txt")

    if reqFile.exists():
        print("Установка зависимостей...")
        subprocess.check_call([str(venvPython), "-m", "pip", "install", "-r", str(reqFile)])

def FreezeRequirements():
    venvPython = GetVenvPython()
    env = BuildEnv()

    with open("requirements.txt", "w", encoding="utf-8") as f:
        subprocess.call(
            [str(venvPython), "-m", "pip", "freeze"],
            stdout=f,
            env=env
        )

def RunInVenv(args):
    venvPython = GetVenvPython()
    env = BuildEnv()

    subprocess.call([str(venvPython), *args], env=env)

def OpenCmd():
    env = BuildEnv()
    print("Запуск CMD с виртуальным окружением...")
    subprocess.call("cmd.exe", env=env)

# =========================
# MAIN (как скрипт)
# =========================
def main():
    new = EnsureVenv()
    if new:
        InstallRequirements()

    OpenCmd()

if __name__ == "__main__":
    main()