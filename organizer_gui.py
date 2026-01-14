import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Store moved files for undo
move_history = []

# -------- ORGANIZE FILES FUNCTION --------
def organize_files():
    folder = folder_path.get()

    if not folder:
        messagebox.showwarning("Warning", "Please select a folder first!")
        return

    try:
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)

            if os.path.isdir(file_path):
                continue

            ext = os.path.splitext(file_name)[1].lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)

                    new_path = os.path.join(category_folder, file_name)
                    shutil.move(file_path, new_path)

                    move_history.append((new_path, file_path))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)

                new_path = os.path.join(other_folder, file_name)
                shutil.move(file_path, new_path)
                move_history.append((new_path, file_path))

        messagebox.showinfo("Success", "Files organized successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------- UNDO FUNCTION --------
def undo_files():
    if not move_history:
        messagebox.showinfo("Info", "Nothing to undo!")
        return

    try:
        while move_history:
            current, original = move_history.pop()
            shutil.move(current, original)

        messagebox.showinfo("Undo", "Undo completed successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------- SELECT FOLDER --------
def select_folder():
    selected = filedialog.askdirectory()
    folder_path.set(selected)


# -------- GUI SETUP --------
root = tk.Tk()
root.title("Automated File Organizer")
root.geometry("500x300")
root.resizable(False, False)

folder_path = tk.StringVar()

tk.Label(root, text="Automated File Organizer", font=("Arial", 16, "bold")).pack(pady=10)

tk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)

tk.Button(root, text="Select Folder", command=select_folder).pack(pady=5)

tk.Button(root, text="Organize Files", command=organize_files, bg="green", fg="white", width=20).pack(pady=10)

tk.Button(root, text="Undo Last Action", command=undo_files, bg="orange", width=20).pack(pady=5)

tk.Label(root, text="Python Automation Project", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
