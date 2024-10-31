import webview

def abrir_google():
    # Cria uma janela com o site do Google
    webview.create_window('Youtube', 'https://www.youtube.com')

    # Inicia o navegador
    webview.start()

if __name__ == '__main__':
    abrir_google()