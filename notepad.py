import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand="yes", fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.root.title(f"Notepad - {file_path}")

    def save_file(self):
        if not hasattr(self, 'file_path') or not self.file_path:
            self.save_as_file()
        else:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
            self.root.title(f"Notepad - {self.file_path}")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.file_path = file_path
            self.root.title(f"Notepad - {self.file_path}")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        return "break"


if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.geometry("800x600")
    root.mainloop()
