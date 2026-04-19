from pathlib import Path
from _venv import EnsureVenv, RunInVenv

MAIN_SCRIPT = Path("src") / "Main.py"

if not MAIN_SCRIPT.exists():
    print(f"Файл {MAIN_SCRIPT} не найден.")
    input("Нажмите Enter для выхода...")
    exit(1)

EnsureVenv()

# https://nuitka.net/user-documentation/user-manual.html
# Для имени: "--output-filename=MyProgram",
# Для иконки: "--windows-icon-from-ico=resources/terminalWhite.ico",
# Для PySide6: "--enable-plugin=pyside6",
# Отключает консоль: --windows-console-mode=disable",
cmd = [
    "-m", "nuitka",
    "--onefile",
    "--standalone",
    "--follow-imports",
    "--jobs=4",
    "--output-dir=compile",
    "--include-raw-dir=resources=resources",
    str(MAIN_SCRIPT)
]

RunInVenv(cmd)
input("\nНажмите Enter для выхода...")