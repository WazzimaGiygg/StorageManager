import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json
from cryptography.fernet import Fernet
import base64

def importar_dados():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not caminho_arquivo:
        return

    chave = chave_entry.get()
    if not chave:
        messagebox.showwarning("Aviso", "Por favor, insira uma chave para decriptografia.")
        return

    try:
        chave = chave.encode()
        cipher = Fernet(chave)

        with open(caminho_arquivo, 'rb') as f:
            encrypted_data = f.read()

        # Decripta os dados
        json_string = cipher.decrypt(encrypted_data).decode()
        parsed_data = json.loads(json_string)

        abas.delete(*abas.tabs())

        for titulo, conteudo in parsed_data.items():
            adicionar_aba(titulo, conteudo)

        json_file_button.pack_forget()
        chave_entry.pack_forget()
        import_button.pack_forget()

    except (ValueError, base64.binascii.Error) as e:
        messagebox.showerror("Erro", "Chave inválida ou erro no arquivo JSON.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao decriptografar o arquivo: {e}")

def adicionar_aba(titulo, conteudo):
    aba = ttk.Frame(abas)
    abas.add(aba, text=titulo)

    # Adiciona um Text widget para exibir o HTML
    html_text = tk.Text(aba, wrap=tk.WORD, height=20, width=50)
    html_text.insert(tk.END, conteudo)
    html_text.pack(pady=5, padx=10)

    # Botão para remover a aba
    botao_remover = tk.Button(aba, text="Remover Aba", command=lambda: abas.forget(aba))
    botao_remover.pack(pady=5)

def salvar_dados():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".json",
                                                    filetypes=[("JSON files", "*.json"),
                                                               ("All files", "*.*")])
    if caminho_arquivo:
        dados = {}
        for aba in abas.winfo_children():
            titulo = aba.tab(aba, "text")
            conteudo = aba.winfo_children()[0].get("1.0", tk.END).strip()
            if titulo and conteudo:
                dados[titulo] = conteudo

        try:
            chave = chave_entry.get()
            cipher = Fernet(chave.encode())
            json_string = json.dumps(dados).encode()
            encrypted_data = cipher.encrypt(json_string)

            with open(caminho_arquivo, 'wb') as f:
                f.write(encrypted_data)

            messagebox.showinfo("Salvar Dados", "Dados salvos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Visualizador de JSON em Múltiplas Abas")
janela.geometry("600x500")
janela.configure(bg='#f4f4f4')

abas = ttk.Notebook(janela)
abas.pack(pady=10, expand=True, fill='both')

json_file_button = tk.Button(janela, text="Selecionar Arquivo JSON", command=importar_dados)
json_file_button.pack(pady=5, padx=10, fill='x')

chave_entry = tk.Entry(janela, show="*", width=50)
chave_entry.pack(pady=5, padx=10)
chave_entry.insert(0, "Chave para decriptografia")

import_button = tk.Button(janela, text="Importar JSON", command=importar_dados)
import_button.pack(pady=5, padx=10, fill='x')

botao_salvar = tk.Button(janela, text="Salvar Dados", command=salvar_dados)
botao_salvar.pack(pady=5, padx=10, fill='x')

janela.mainloop()
