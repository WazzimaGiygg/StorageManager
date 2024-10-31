import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_files():
    folder_path = filedialog.askdirectory()
    if folder_path:
        list_files(folder_path)

def list_files(folder):
    files = os.listdir(folder)
    files_list.delete(0, tk.END)  # Limpa a lista atual
    for file in files:
        files_list.insert(tk.END, file)

def open_file(event):
    selected_file = files_list.get(files_list.curselection())
    folder_path = filedialog.askdirectory()  # Escolha a pasta para abrir o arquivo
    full_path = os.path.join(folder_path, selected_file)
    if os.path.isfile(full_path):
        with open(full_path, 'r') as f:
            content = f.read()
            messagebox.showinfo("File Content", content)

# Configuração da interface
root = tk.Tk()
root.title("File Explorer")

frame = tk.Frame(root)
frame.pack(pady=20)

browse_button = tk.Button(frame, text="Browse Folder", command=browse_files)
browse_button.pack()

files_list = tk.Listbox(frame, width=50, height=15)
files_list.pack()

files_list.bind("<Double-Button-1>", open_file)

root.mainloop()