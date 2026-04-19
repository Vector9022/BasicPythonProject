import localLib.RAA as RAA; RAA.RunAsAdmin()
from _venv import EnsureVenv, RunInVenv, FreezeRequirements

EnsureVenv()

print('[INFO] Доступные команды: install | uninstall | upgrade')

while True:
    try:
        action = input("\npip ").strip()
        if not action:
            continue

        parts = action.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "upgrade":
            RunInVenv(["-m", "pip", "install", "--upgrade", arg])
        elif cmd in ("install", "uninstall"):
            RunInVenv(["-m", "pip", cmd, arg])
        else:
            continue

        FreezeRequirements()

    except KeyboardInterrupt:
        break

input("\nНажмите Enter для выхода...")