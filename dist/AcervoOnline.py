import webview

def abrir_google():
    # Cria uma janela com o site do Google
    webview.create_window('Unifunec', 'http://186.225.145.106/sophia_web/')

    # Inicia o navegador
    webview.start()

if __name__ == '__main__':
    abrir_google()
    