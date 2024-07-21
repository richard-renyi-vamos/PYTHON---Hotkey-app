import tkinter as tk
from tkinter import messagebox
import keyboard

class HotkeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotkey App")

        self.hotkeys = {}

        self.label = tk.Label(root, text="Press a hotkey and type an action:")
        self.label.pack(pady=10)

        self.hotkey_entry = tk.Entry(root)
        self.hotkey_entry.pack(pady=5)
        
        self.action_entry = tk.Entry(root)
        self.action_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Hotkey", command=self.add_hotkey)
        self.add_button.pack(pady=10)

        self.hotkey_list = tk.Listbox(root, width=50)
        self.hotkey_list.pack(pady=10)

    def add_hotkey(self):
        hotkey = self.hotkey_entry.get()
        action = self.action_entry.get()

        if hotkey and action:
            self.hotkeys[hotkey] = action
            self.hotkey_list.insert(tk.END, f"{hotkey}: {action}")
            self.hotkey_entry.delete(0, tk.END)
            self.action_entry.delete(0, tk.END)
            
            keyboard.add_hotkey(hotkey, self.perform_action, args=(action,))
        else:
            messagebox.showwarning("Input Error", "Please enter both a hotkey and an action.")

    def perform_action(self, action):
        messagebox.showinfo("Hotkey Action", f"Performing action: {action}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotkeyApp(root)
    root.mainloop()
