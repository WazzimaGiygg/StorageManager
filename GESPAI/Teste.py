import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
from cryptography.fernet import Fernet
import base64

# Geração de chave para criptografia
def generate_key():
    return base64.urlsafe_b64encode(Fernet.generate_key()).decode()

class ProntuarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciamento de Prontuários Unificado")
        
        self.APP_VERSION = "Versão 0.0626"
        self.tabs = {}
        self.active_tab = 1
        self.next_tab_number = 1

        # Configuração da interface
        self.setup_ui()
        self.add_tab()  # Inicializa com uma aba

    def setup_ui(self):
        # Contêiner para abas
        self.tab_frame = tk.Frame(self.master)
        self.tab_frame.pack(fill=tk.X)

        self.add_tab_button = tk.Button(self.tab_frame, text="Adicionar Aba", command=self.add_tab)
        self.add_tab_button.pack(side=tk.LEFT)

        self.tab_buttons = {}

        # Contêiner do editor
        self.editor_frame = tk.Frame(self.master)
        self.editor_frame.pack(pady=10)

        self.tab_title = tk.Entry(self.editor_frame, width=50)
        self.tab_title.pack(pady=5)
        self.tab_title.insert(0, "Título da aba")
        self.tab_title.bind("<KeyRelease>", lambda e: self.update_tab_title())

        self.tab_description = tk.Text(self.editor_frame, width=50, height=10)
        self.tab_description.pack(pady=5)
        self.tab_description.insert(tk.END, "Descrição da aba")
        self.tab_description.bind("<KeyRelease>", lambda e: self.update_tab_description())

        self.item_title = tk.Entry(self.editor_frame, width=50)
        self.item_title.pack(pady=5)
        self.item_title.insert(0, "Título do item")

        self.item_content = tk.Text(self.editor_frame, width=50, height=5)
        self.item_content.pack(pady=5)
        self.item_content.insert(tk.END, "Conteúdo do item")

        self.add_item_button = tk.Button(self.editor_frame, text="Adicionar Item", command=self.add_item)
        self.add_item_button.pack(pady=5)

        self.listbox = tk.Listbox(self.editor_frame, width=50)
        self.listbox.pack(pady=5)

        self.buttons_frame = tk.Frame(self.editor_frame)
        self.buttons_frame.pack(pady=5)

        self.save_button = tk.Button(self.buttons_frame, text="Salvar", command=self.save)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.save_encrypted_button = tk.Button(self.buttons_frame, text="Salvar com Criptografia", command=self.save_encrypted)
        self.save_encrypted_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.buttons_frame, text="Carregar", command=self.load)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.load_encrypted_button = tk.Button(self.buttons_frame, text="Carregar com Criptografia", command=self.load_encrypted)
        self.load_encrypted_button.pack(side=tk.LEFT, padx=5)

        self.password_entry = tk.Entry(self.buttons_frame, show='*', width=25)
        self.password_entry.pack(side=tk.LEFT, padx=5)
        self.password_entry.insert(0, "Senha (se necessário)")

    def add_tab(self):
        self.tabs[self.next_tab_number] = {"title": '', "description": '', "items": []}
        self.active_tab = self.next_tab_number
        self.next_tab_number += 1
        self.update_tab_buttons()
        self.update_editor()

    def update_tab_buttons(self):
        for button in self.tab_buttons.values():
            button.destroy()
        self.tab_buttons.clear()

        for tab_number in self.tabs.keys():
            button = tk.Button(self.tab_frame, text=f"Aba {tab_number}", command=lambda n=tab_number: self.select_tab(n))
            button.pack(side=tk.LEFT)
            self.tab_buttons[tab_number] = button

    def select_tab(self, tab_number):
        self.active_tab = tab_number
        self.update_editor()

    def update_editor(self):
        current_tab = self.tabs[self.active_tab]
        self.tab_title.delete(0, tk.END)
        self.tab_title.insert(0, current_tab["title"])
        self.tab_description.delete(1.0, tk.END)
        self.tab_description.insert(tk.END, current_tab["description"])

        self.listbox.delete(0, tk.END)
        for item in current_tab["items"]:
            self.listbox.insert(tk.END, item["title"])

    def update_tab_title(self):
        self.tabs[self.active_tab]["title"] = self.tab_title.get()
        self.update_tab_buttons()

    def update_tab_description(self):
        self.tabs[self.active_tab]["description"] = self.tab_description.get("1.0", tk.END).strip()

    def add_item(self):
        title = self.item_title.get().strip()
        content = self.item_content.get("1.0", tk.END).strip()
        if title and content:
            self.tabs[self.active_tab]["items"].append({"title": title, "content": content})
            self.item_title.delete(0, tk.END)
            self.item_content.delete("1.0", tk.END)
            self.update_editor()
        else:
            messagebox.showwarning("Aviso", "Título e conteúdo não podem estar vazios.")

    def save(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w') as f:
                json.dump({"version": self.APP_VERSION, "data": self.tabs}, f)

    def save_encrypted(self):
        filename = filedialog.asksaveasfilename(defaultextension=".encrypted.json", filetypes=[("Encrypted files", "*.encrypted.json")])
        if filename:
            password = self.password_entry.get().encode()
            key = base64.urlsafe_b64encode(password.ljust(32)[:32])
            cipher = Fernet(key)
            json_data = json.dumps({"version": self.APP_VERSION, "data": self.tabs}).encode()
            encrypted_data = cipher.encrypt(json_data)

            with open(filename, 'wb') as f:
                f.write(encrypted_data)

    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'r') as f:
                result = json.load(f)
                if result["version"] != self.APP_VERSION:
                    messagebox.showerror("Erro", "A versão sendo carregada usa uma plataforma mais moderna. O documento não pode ser aberto.")
                    return
                self.tabs = result["data"]
                self.next_tab_number = max(self.tabs.keys()) + 1
                self.active_tab = list(self.tabs.keys())[0]
                self.update_tab_buttons()
                self.update_editor()

    def load_encrypted(self):
        filename = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.encrypted.json")])
        if filename:
            with open(filename, 'rb') as f:
                encrypted_data = f.read()
                password = self.password_entry.get().encode()
                key = base64.urlsafe_b64encode(password.ljust(32)[:32])
                cipher = Fernet(key)

                try:
                    decrypted_data = cipher.decrypt(encrypted_data)
                    result = json.loads(decrypted_data)
                    if result["version"] != self.APP_VERSION:
                        messagebox.showerror("Erro", "A versão sendo carregada usa uma plataforma mais moderna. O documento não pode ser aberto.")
                        return
                    self.tabs = result["data"]
                    self.next_tab_number = max(self.tabs.keys()) + 1
                    self.active_tab = list(self.tabs.keys())[0]
                    self.update_tab_buttons()
                    self.update_editor()
                except Exception:
                    messagebox.showerror("Erro", "Senha incorreta ou arquivo corrompido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProntuarioApp(root)
    root.mainloop()
