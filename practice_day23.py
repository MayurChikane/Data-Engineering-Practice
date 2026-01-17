print("------------------------- Practice Day 23 ------------------------")

# mini project day 7
# crazy alert app
import tkinter as tk
import tkinter.messagebox
import random
class CrazyAlertApp:
    def __init__(self, master):
        self.master = master
        master.title("Crazy Alert App")

        self.label = tk.Label(master, text="Click the button for a crazy alert!")
        self.label.pack()

        self.alert_button = tk.Button(master, text="Show Alert", command=self.show_crazy_alert)
        self.alert_button.pack()

    def show_crazy_alert(self):
        messages = [
            "Alert! Something crazy happened!",
            "Warning! This is a wild alert!",
            "Caution! Crazy things are happening!",
            "Heads up! A crazy alert is here!"
        ]
        alert_message = random.choice(messages)
        tkinter.messagebox.showinfo("Crazy Alert", alert_message)
# Example usage
root = tk.Tk()
app = CrazyAlertApp(root)
root.mainloop()

print("------------------------ End of Practice Day 23 ------------------------")