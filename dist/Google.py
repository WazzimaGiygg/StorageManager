import webview

def abrir_google():
    # Cria uma janela com o site do Google
    webview.create_window('Google', 'https://www.google.com')

    # Inicia o navegador
    webview.start()

if __name__ == '__main__':
    abrir_google()