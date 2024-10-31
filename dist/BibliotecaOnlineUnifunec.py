import webview

def abrir_google():
    # Cria uma janela com o site do Google
    webview.create_window('Biblioteca Online Unifunec', 'https://dliportal.zbra.com.br/Login.aspx?key=FUNEC')

    # Inicia o navegador
    webview.start()

if __name__ == '__main__':
    abrir_google()

