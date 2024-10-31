import json
import os
import base64
import hashlib
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from tkinterhtml import HtmlFrame  # Importando o HtmlFrame para visualização de HTML
from cryptography.fernet import Fernet

# Função para gerar uma chave de criptografia baseada em uma senha
def gerar_chave(senha):
    return base64.urlsafe_b64encode(hashlib.sha256(senha.encode()).digest())

# Função para criptografar dados
def criptografar_dados(dados, senha):
    chave = gerar_chave(senha)
    f = Fernet(chave)
    dados_json = json.dumps(dados).encode()
    return f.encrypt(dados_json)

# Função para descriptografar dados
def descriptografar_dados(dados_encriptados, senha):
    chave = gerar_chave(senha)
    f = Fernet(chave)
    dados_json = f.decrypt(dados_encriptados)
    return json.loads(dados_json)

# Função para criar um novo perfil
def criar_perfil():
    perfil = {
        "nomeCompleto": simpledialog.askstring("Nome Completo", "Insira seu nome completo:"),
        "dataNascimento": simpledialog.askstring("Data de Nascimento", "Insira sua data de nascimento (YYYY-MM-DD):"),
        "apelidoLogin": simpledialog.askstring("Apelido de Login", "Insira um apelido de login:"),
        "telefone": simpledialog.askstring("Telefone", "Insira seu telefone (DDI + DDD + telefone):"),
        "senha": simpledialog.askstring("Senha", "Insira sua senha:", show='*'),
        "subsenha": simpledialog.askstring("Subsenha", "Insira sua subsenha (somente números):"),
        "cpfVinculado": simpledialog.askstring("C.P.F Vinculado", "Insira seu CPF:")
    }
    
    chave = gerar_chave("L20053F")
    dados_encriptados = criptografar_dados(perfil, "L20053F")
    
    with open(f"{perfil['apelidoLogin']}.json", "wb") as f:
        f.write(dados_encriptados)
    
    with open(f"{perfil['apelidoLogin']}_key.key", "wb") as f:
        f.write(chave)

    messagebox.showinfo("Sucesso", "Perfil criado com sucesso!")

# Função para login e carregar perfil
def login():
    apelido = simpledialog.askstring("Login", "Insira seu apelido de login:")
    senha = simpledialog.askstring("Senha", "Insira sua senha:", show='*')
    
    try:
        with open(f"{apelido}.json", "rb") as f:
            dados_encriptados = f.read()
        
        perfil = descriptografar_dados(dados_encriptados, "L20053F")
        
        if perfil['senha'] == senha:
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Erro", "Senha incorreta.")
    
    except FileNotFoundError:
        messagebox.showerror("Erro", "Perfil não encontrado.")

# Função para ativar o modo admin
def ativar_modo_admin():
    senha_admin = simpledialog.askstring("Modo Admin", "Insira a senha do administrador:", show='*')
    if senha_admin == "L20053F":
        messagebox.showinfo("Sucesso", "Modo admin ativado!")
        aplicativo_menu.entryconfig("Criar Novo Perfil", state="normal")
        aplicativo_menu.entryconfig("Gravar Aplicativo", state="normal")  # Habilita o menu Gravar Aplicativo
        aplicativo_menu.entryconfig("Executar Aplicativo", state="normal")  # Habilita o menu Executar Aplicativo
        opcoes_menu.entryconfig("Compilar HTML", state="normal")  # Habilita o menu Compilar HTML
    else:
        messagebox.showerror("Erro", "Senha incorreta.")

# Função para gravar um novo aplicativo
def gravar_aplicativo():
    nome_aplicativo = simpledialog.askstring("Gravar Aplicativo", "Insira o nome do aplicativo (.py):")
    if not nome_aplicativo.endswith(".py"):
        nome_aplicativo += ".py"
    
    codigo_fonte = simpledialog.askstring("Código Fonte", "Insira o código fonte do aplicativo:")
    dados_encriptados = criptografar_dados(codigo_fonte, "L20053F")
    
    with open(nome_aplicativo, "wb") as f:
        f.write(dados_encriptados)

    messagebox.showinfo("Sucesso", "Aplicativo gravado com sucesso!")

# Função para executar um aplicativo
def executar_aplicativo():
    nome_aplicativo = simpledialog.askstring("Executar Aplicativo", "Insira o nome do aplicativo (.py):")
    
    try:
        with open(nome_aplicativo, "rb") as f:
            dados_encriptados = f.read()
        
        codigo_fonte = descriptografar_dados(dados_encriptados, "L20053F")

        # Executar o código fonte
        exec(codigo_fonte)
    
    except FileNotFoundError:
        messagebox.showerror("Erro", "Aplicativo não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o aplicativo: {str(e)}")

# Função para abrir o editor de texto
def abrir_editor():
    editor_window = tk.Toplevel(root)
    editor_window.title("Editor de Código Python")
    editor_window.geometry("600x400")

    # Criação do campo de texto
    texto = scrolledtext.ScrolledText(editor_window, wrap=tk.WORD)
    texto.pack(expand=True, fill='both')

    # Botões para salvar e executar
    btn_frame = tk.Frame(editor_window)
    btn_frame.pack(fill='x')

    btn_salvar = tk.Button(btn_frame, text="Salvar", command=lambda: salvar_codigo(texto.get("1.0", tk.END)))
    btn_salvar.pack(side='left', padx=5, pady=5)

    btn_executar = tk.Button(btn_frame, text="Executar", command=lambda: executar_codigo(texto.get("1.0", tk.END)))
    btn_executar.pack(side='right', padx=5, pady=5)

# Função para salvar o código em um arquivo
def salvar_codigo(codigo):
    nome_aplicativo = simpledialog.askstring("Salvar Aplicativo", "Insira o nome do aplicativo (.py):")
    if not nome_aplicativo.endswith(".py"):
        nome_aplicativo += ".py"
    
    dados_encriptados = criptografar_dados(codigo, "L20053F")
    
    with open(nome_aplicativo, "wb") as f:
        f.write(dados_encriptados)

    messagebox.showinfo("Sucesso", "Aplicativo salvo com sucesso!")

# Função para executar o código
def executar_codigo(codigo):
    try:
        exec(codigo)  # Executa o código Python fornecido
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o código: {str(e)}")

# Função para compilar e visualizar HTML
def compilar_html():
    html_codigo = simpledialog.askstring("Compilar HTML", "Insira seu código HTML:")
    
    # Validando o HTML
    if not validar_html(html_codigo):
        messagebox.showerror("Erro", "HTML inválido! Verifique o código.")
        return

    # Abrindo uma nova janela para exibir o HTML
    html_window = tk.Toplevel(root)
    html_window.title("Visualizador de HTML")
    html_window.geometry("800x600")

    # Criando um frame para renderizar HTML
    frame = HtmlFrame(html_window, horizontal_scrollbar="auto")
    frame.set_content(html_codigo)
    frame.pack(expand=True, fill='both')

# Função básica para validar HTML (pode ser melhorada)
def validar_html(html):
    # Implementação simples para verificar se o HTML tem uma tag <html>
    if "<html>" in html and "</html>" in html:
        return True
    return False

# Função principal da interface
def main():
    global root, aplicativo_menu, opcoes_menu  # Tornar root e menus globais
    root = tk.Tk()
    root.title("Sistema de Registro Universal")

    # Criando o menu
    menu_bar = tk.Menu(root)
    
    # Adicionando o menu Aplicativo
    aplicativo_menu = tk.Menu(menu_bar, tearoff=0)
    aplicativo_menu.add_command(label="Criar Novo Perfil", command=criar_perfil, state="disabled")
    aplicativo_menu.add_command(label="Login", command=login)
    aplicativo_menu.add_separator()
    aplicativo_menu.add_command(label="Gravar Aplicativo", command=gravar_aplicativo, state="disabled")
    aplicativo_menu.add_command(label="Executar Aplicativo", command=executar_aplicativo, state="disabled")
    aplicativo_menu.add_separator()
    menu_bar.add_cascade(label="Aplicativo", menu=aplicativo_menu)

    # Adicionando o menu Opções
    opcoes_menu = tk.Menu(menu_bar, tearoff=0)
    opcoes_menu.add_command(label="Novo Aplicativo", command=abrir_editor)
    opcoes_menu.add_command(label="Compilar HTML", command=compilar_html, state="disabled")  # Compilar HTML no menu Opções
    menu_bar.add_cascade(label="Opções", menu=opcoes_menu)

    root.config(menu=menu_bar)

    # Ativar modo admin com combinação de teclas
    root.bind('<Control-Alt-d>', lambda event: ativar_modo_admin())

    root.mainloop()

if __name__ == "__main__":
    main()
