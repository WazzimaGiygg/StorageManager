def criar_html(titulo, autor, capitulos):
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2 {{ color: #333; }}
        p {{ margin: 10px 0; }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <h2>Autor: {autor}</h2>
    {capitulos}
</body>
</html>
"""
    return html_content

def main():
    print("Digite o título do livro:")
    titulo = input("> ")
    print("Digite o nome do autor:")
    autor = input("> ")

    capitulos = ""
    while True:
        print("Digite o título do capítulo (ou 'sair' para finalizar):")
        titulo_capitulo = input("> ")
        if titulo_capitulo.lower() == 'sair':
            break
        
        print("Digite o conteúdo do capítulo:")
        conteudo_capitulo = input("> ")
        
        capitulos += f"<h2>{titulo_capitulo}</h2>\n<p>{conteudo_capitulo}</p>\n"

    html = criar_html(titulo, autor, capitulos)
    
    with open("livro.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("O livro foi criado com sucesso em 'livro.html'.")

if __name__ == "__main__":
    main()
