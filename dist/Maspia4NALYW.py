import os
import socket
import threading
import webbrowser
import http.server
import socketserver
import logging
import subprocess
import py_compile
import tkinter as tk
from tkinter import filedialog, messagebox

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para encontrar uma porta livre automaticamente
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

# Função para obter o melhor host disponível
def get_best_host():
    try:
        return socket.gethostbyname("localhost")
    except socket.error:
        return "127.0.0.1"

# Classe para gerenciar o servidor HTTP
class ServerManager:
    def __init__(self):
        self.port = find_free_port()
        self.host = get_best_host()
        self.httpd = None
        self.server_thread = None

    def start_server(self):
        handler = http.server.SimpleHTTPRequestHandler

        class LoggingHandler(handler):
            def do_GET(self):
                logging.info(f"Request: {self.path}")
                super().do_GET()

        try:
            self.httpd = socketserver.TCPServer((self.host, self.port), LoggingHandler)
            logging.info(f"Servidor rodando em http://{self.host}:{self.port}")
            self.server_thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
            self.server_thread.start()
        except OSError as e:
            logging.error(f"Erro ao iniciar o servidor: {e}")

    def stop_server(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            logging.info("Servidor encerrado.")

# Funções principais
def calc():
    logging.info("Calculadora aberta...")

def restart_hosts():
    try:
        subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "disable"], check=True)
        subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "enable"], check=True)
        logging.info("Hosts reiniciados com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao reiniciar os hosts: {e}")

def maspia():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visualizador de JSON em Múltiplas Abas</title>
        <style>
            body { font-family: 'Arial', sans-serif; background-color: #f4f4f4; padding: 0; margin: 0; height: 100vh; }
            .container { max-width: 100%; height: 100%; margin: auto; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); display: flex; flex-direction: column; }
            .tabs { display: flex; flex-wrap: wrap; margin-bottom: 10px; }
            .tab { padding: 10px; background: #ddd; margin: 5px; border-radius: 4px 4px 0 0; cursor: pointer; flex: 1; text-align: center; }
            .tab.active { background: white; border-bottom: 2px solid #4285F4; }
            iframe { width: 100%; height: 100%; border: none; margin-top: 0; border-radius: 4px; flex: 1; }
            input[type="file"], input[type="password"], button { width: 100%; margin: 10px 0; padding: 12px; font-size: 16px; }
            button { background-color: #4285F4; border: none; color: white; border-radius: 4px; cursor: pointer; }
            button:hover { background-color: #357ae8; }
        </style>
    </head>
    <body>
        <div class="container">
            <input type="file" id="jsonFile" accept=".json">
            <input type="password" id="encryptionPassword" placeholder="Senha para decriptografia">
            <button id="importButton">Importar JSON</button>
            <div class="tabs" id="tabs"></div>
            <div id="iframesContainer" style="flex: 1; display: flex; flex-direction: column;"></div>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
        <script>
            document.getElementById('importButton').onclick = function() {
                importJSON();
            };
            function importJSON() {
                const fileInput = document.getElementById('jsonFile');
                const password = document.getElementById('encryptionPassword').value;
                const file = fileInput.files[0];
                if (!file) {
                    alert('Por favor, selecione um arquivo JSON.');
                    return;
                }
                const reader = new FileReader();
                reader.onload = function(event) {
                    const encryptedData = event.target.result;
                    try {
                        const bytes = CryptoJS.AES.decrypt(encryptedData, password);
                        const jsonString = bytes.toString(CryptoJS.enc.Utf8);
                        const parsedData = JSON.parse(jsonString);
                        document.getElementById('jsonFile').style.display = 'none';
                        document.getElementById('encryptionPassword').style.display = 'none';
                        document.getElementById('importButton').style.display = 'none';
                        document.getElementById('tabs').innerHTML = '';
                        document.getElementById('iframesContainer').innerHTML = '';
                        for (const key in parsedData) {
                            if (parsedData.hasOwnProperty(key)) {
                                addTab(parsedData[key], key);
                            }
                        }
                    } catch (e) {
                        alert('Erro ao decriptografar o arquivo. Verifique a senha ou o formato do arquivo.');
                    }
                };
                reader.readAsText(file);
            }
            function addTab(htmlContent, tabName) {
                const tabButton = document.createElement('div');
                tabButton.className = 'tab';
                tabButton.innerText = tabName;
                tabButton.onclick = () => setActiveTab(tabName);
                document.getElementById('tabs').appendChild(tabButton);
                const iframe = document.createElement('iframe');
                iframe.id = tabName;
                iframe.srcdoc = htmlContent;
                document.getElementById('iframesContainer').appendChild(iframe);
                if (document.querySelectorAll('.tab').length === 1) {
                    tabButton.classList.add('active');
                    iframe.style.display = 'block';
                } else {
                    iframe.style.display = 'none';
                }
            }
            function setActiveTab(tabName) {
                const tabs = document.querySelectorAll('.tab');
                const iframes = document.querySelectorAll('iframe');
                tabs.forEach(tab => tab.classList.remove('active'));
                iframes.forEach(iframe => iframe.style.display = 'none');
                document.getElementById(tabName).style.display = 'block';
                const activeTab = Array.from(tabs).find(tab => tab.innerText === tabName);
                if (activeTab) {
                    activeTab.classList.add('active');
                }
            }
        </script>
    </body>
    </html>
    """
    base_dir = os.path.abspath('temp_html_maspia')
    os.makedirs(base_dir, exist_ok=True)
    html_file_path = os.path.join(base_dir, "index.html")
    with open(html_file_path, "w", encoding='utf-8') as f:
        f.write(html_content)

    host = "localhost"
    port = find_free_port()
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, directory=base_dir, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    try:
        with socketserver.TCPServer((host, port), CustomHandler) as httpd:
            logging.info(f"Servindo em: http://{host}:{port}/index.html")
            webbrowser.open(f"http://{host}:{port}/index.html")
            httpd.serve_forever()
    except Exception as e:
        logging.error(f"Erro ao iniciar o servidor: {e}")

def converterhtmlparajson():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gerador de JSON Criptografado</title>
        <style>
            body { font-family: 'Arial', sans-serif; background-color: #f1f1f1; padding: 20px; }
            .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); }
            input[type="file"], input[type="password"], button { width: 100%; margin: 10px 0; padding: 12px; font-size: 16px; }
            button { background-color: #4285F4; border: none; color: white; border-radius: 4px; cursor: pointer; }
            button:hover { background-color: #357ae8; }
        </style>
    </head>
    <body>
        <div class="container">
            <input type="file" id="jsonFile" accept=".json">
            <input type="password" id="encryptionPassword" placeholder="Senha para criptografia">
            <button id="exportButton">Exportar JSON</button>
        </div>
        <script>
            document.getElementById('exportButton').onclick = function() {
                exportJSON();
            };
            function exportJSON() {
                const fileInput = document.getElementById('jsonFile');
                const password = document.getElementById('encryptionPassword').value;
                const file = fileInput.files[0];
                if (!file) {
                    alert('Por favor, selecione um arquivo JSON.');
                    return;
                }
                const reader = new FileReader();
                reader.onload = function(event) {
                    const jsonData = event.target.result;
                    const encryptedData = CryptoJS.AES.encrypt(jsonData, password).toString();
                    const blob = new Blob([encryptedData], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'exported.json';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                };
                reader.readAsText(file);
            }
        </script>
    </body>
    </html>
    """
    base_dir = os.path.abspath('temp_html_maspia')
    os.makedirs(base_dir, exist_ok=True)
    html_file_path = os.path.join(base_dir, "converter.html")
    with open(html_file_path, "w", encoding='utf-8') as f:
        f.write(html_content)

    host = "localhost"
    port = find_free_port()
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, directory=base_dir, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    try:
        with socketserver.TCPServer((host, port), CustomHandler) as httpd:
            logging.info(f"Servindo em: http://{host}:{port}/converter.html")
            webbrowser.open(f"http://{host}:{port}/converter.html")
            httpd.serve_forever()
    except Exception as e:
        logging.error(f"Erro ao iniciar o servidor: {e}")

def import_and_compile():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo Python",
        filetypes=[("Python Files", "*.py")]
    )

    if file_path:
        try:
            # Compila o arquivo
            compiled_file = py_compile.compile(file_path, cfile=file_path + 'c')
            messagebox.showinfo("Sucesso", f"Arquivo compilado: {compiled_file}")

            # Executa o arquivo compilado
            subprocess.run(['python', compiled_file])  # Executa o arquivo compilado
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na compilação ou execução: {e}")
    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")

def main_menu():
    server_manager = ServerManager()
    server_manager.start_server()
    
    root = tk.Tk()
    root.title("Menu Principal")

    tk.Button(root, text="Acessar a Calculadora", command=calc).pack(pady=10)
    tk.Button(root, text="Abrir o Visualizador de JSON em Múltiplas Abas", command=maspia).pack(pady=10)
    tk.Button(root, text="Criar JSON Criptografado", command=converterhtmlparajson).pack(pady=10)
    tk.Button(root, text="Reiniciar Hosts", command=restart_hosts).pack(pady=10)
    tk.Button(root, text="Importar e Compilar Arquivo Python", command=import_and_compile).pack(pady=10)
    tk.Button(root, text="Sair", command=root.quit).pack(pady=10)

    root.mainloop()
    server_manager.stop_server()

if __name__ == "__main__":
    main_menu()
