from pathlib import Path
from _venv import EnsureVenv, RunInVenv

MAIN_SCRIPT = Path("src") / "Main.py"

if not MAIN_SCRIPT.exists():
    print(f"Файл {MAIN_SCRIPT} не найден.")
    input("Нажмите Enter для выхода...")
    exit(1)

EnsureVenv()
RunInVenv([str(MAIN_SCRIPT)])
input("\nНажмите Enter для выхода...")