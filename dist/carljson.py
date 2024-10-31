import tkinter as tk
from tkinter import filedialog, messagebox, Frame, Text, Scrollbar
import json
from Crypto.Cipher import AES
import base64
import os

class JSONViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de JSON em Múltiplas Abas")

        self.container = tk.Frame(root)
        self.container.pack(pady=15)

        self.json_file_label = tk.Label(self.container, text="Selecione um arquivo JSON:")
        self.json_file_label.pack()

        self.json_file_entry = tk.Entry(self.container, width=50)
        self.json_file_entry.pack()

        self.json_file_button = tk.Button(self.container, text="Selecionar", command=self.select_file)
        self.json_file_button.pack()

        self.password_label = tk.Label(self.container, text="Senha para decriptografia:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.container, show="*", width=50)
        self.password_entry.pack()

        self.import_button = tk.Button(self.container, text="Importar JSON", command=self.import_json)
        self.import_button.pack(pady=10)

        self.tab_frame = tk.Frame(root)
        self.tab_frame.pack(pady=10)

        self.tabs = {}
        self.current_tab = None

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            self.json_file_entry.delete(0, tk.END)
            self.json_file_entry.insert(0, file_path)

    def import_json(self):
        file_path = self.json_file_entry.get()
        password = self.password_entry.get()

        if not file_path or not password:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo e insira a senha.")
            return

        try:
            with open(file_path, 'r') as file:
                encrypted_data = file.read()
                decrypted_data = self.decrypt_data(encrypted_data, password)
                parsed_data = json.loads(decrypted_data)

                self.create_tabs(parsed_data)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao importar o JSON: {e}")

    def decrypt_data(self, encrypted_data, password):
        try:
            encrypted_data = base64.b64decode(encrypted_data)
            cipher = AES.new(password.encode('utf-8'), AES.MODE_EAX, nonce=encrypted_data[:16])
            decrypted = cipher.decrypt(encrypted_data[16:])
            return decrypted.decode('utf-8')
        except Exception as e:
            raise ValueError("Erro ao decriptografar o arquivo. Verifique a senha ou o formato.")

    def create_tabs(self, parsed_data):
        for key in parsed_data:
            self.add_tab(parsed_data[key], key)

    def add_tab(self, content, tab_name):
        frame = Frame(self.tab_frame)
        frame.pack(fill="both", expand=True)

        text_area = Text(frame)
        text_area.insert(tk.END, json.dumps(content, indent=4))
        text_area.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scrollbar.set)

        tab_button = tk.Button(self.container, text=tab_name, command=lambda: self.set_active_tab(frame))
        tab_button.pack(side="left", padx=5)

        self.tabs[tab_name] = frame

        if not self.current_tab:
            self.set_active_tab(frame)

    def set_active_tab(self, frame):
        if self.current_tab:
            self.current_tab.pack_forget()
        frame.pack(fill="both", expand=True)
        self.current_tab = frame

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONViewerApp(root)
    root.mainloop()
