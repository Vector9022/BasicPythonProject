import threading
import UIMain

ui = None

class Hello:
    def __init__(self):
        print("Class initialized. Hello!\n")

        self.gb = "Goodbye!"

def Main():
    app = Hello()

    ui.signals.settooltip.emit("Hello from thread!")
    
    print(app.gb)

if __name__ == "__main__":
    ui = UIMain.App()
    threading.Thread(target=Main, daemon=True).start()
    ui.Run()