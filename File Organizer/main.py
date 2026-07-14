import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_folder

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def organize_files():
    if folder_path.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return
    try:
        moved, summary = organize_folder(folder_path.get())
        report = "Organization Completed!\n\n"
        for category, count in summary.items():
            report += f"{category}: {count}\n"
        report += f"\nTotal Files Moved: {moved}"
        messagebox.showinfo(
            "Success",
            report
        )
    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e))

root = tk.Tk()
root.title("File Organizer")
root.geometry("600x220")
root.resizable(False, False)
title = tk.Label(
    root,
    text="Automatic File Organizer",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)
folder_path = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=folder_path,
    width=60
)
entry.pack(pady=5)
browse_btn = tk.Button(
    root,
    text="Browse Folder",
    command=browse_folder,
    width=20
)
browse_btn.pack(pady=5)
organize_btn = tk.Button(
    root,
    text="Organize Files",
    command=organize_files,
    width=20,
    bg="#4CAF50",
    fg="white"
)
organize_btn.pack(pady=15)
root.mainloop()