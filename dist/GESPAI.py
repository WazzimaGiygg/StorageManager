import json

class Projeto:
    def __init__(self):
        self.solucao = {}

    def adicionar_solucao(self, id_solucao, nome_solucao):
        self.solucao[id_solucao] = {
            'nome': nome_solucao,
            'regras': {}
        }
        print(f"Solução {id_solucao} com nome '{nome_solucao}' adicionada.")

    def adicionar_regra(self, id_solucao, id_regra, nome_regra):
        if id_solucao in self.solucao:
            self.solucao[id_solucao]['regras'][id_regra] = {
                'nome': nome_regra,
                'documentos': {}
            }
            print(f"Regra {id_regra} com nome '{nome_regra}' adicionada à solução {id_solucao}.")
        else:
            print("Solução não encontrada.")

    def adicionar_documento(self, id_solucao, id_regra, id_documento, nome_documento):
        if id_solucao in self.solucao and id_regra in self.solucao[id_solucao]['regras']:
            self.solucao[id_solucao]['regras'][id_regra]['documentos'][id_documento] = {
                'nome': nome_documento,
                'linhas': [],  # Inicializa a lista de linhas aqui
                'id_linha': 0  # Contador de ID de linha
            }
            print(f"Documento {id_documento} com nome '{nome_documento}' adicionado à regra {id_regra} da solução {id_solucao}.")
        else:
            print("Solução ou regra não encontrada.")

    def adicionar_linha(self, id_solucao, id_regra, id_documento):
        if id_solucao in self.solucao and id_regra in self.solucao[id_solucao]['regras']:
            if id_documento in self.solucao[id_solucao]['regras'][id_regra]['documentos']:
                doc_info = self.solucao[id_solucao]['regras'][id_regra]['documentos'][id_documento]
                linha = input("Digite os dados da linha (máximo 127 caracteres): ")
                if len(linha) <= 127:
                    id_linha = f"{doc_info['id_linha']:02d}"
                    doc_info['linhas'].append((id_linha, linha))
                    doc_info['id_linha'] += 1  # Incrementa o contador de ID de linha
                    print(f"Linha {id_linha} adicionada ao documento {id_documento} da regra {id_regra} da solução {id_solucao}.")
                else:
                    print("A linha deve ter no máximo 127 caracteres.")
            else:
                print("Documento não encontrado na regra.")
        else:
            print("Solução ou regra não encontrada.")

    def listar_dados_tabela(self):
        print("--- Tabela de Dados ---")
        print(f"{'Solução':<20} {'Regra':<20} {'Documento':<20} {'Linha':<2} {'Informação':<127}")
        for id_solucao, dados_solucao in self.solucao.items():
            for id_regra, dados_regra in dados_solucao['regras'].items():
                for id_documento, doc_info in dados_regra['documentos'].items():
                    for linha_info in doc_info['linhas']:
                        id_linha, linha = linha_info  # Corrigido para descompactar corretamente
                        print(f"{dados_solucao['nome']:<20} {dados_regra['nome']:<20} {doc_info['nome']:<20} {id_linha:<2} {linha:<127}")

    def listar_dados_separado(self):
        print("--- Dados Separados ---")
        for id_solucao, dados_solucao in self.solucao.items():
            print(f"Solução: {dados_solucao['nome']}")
            for id_regra, dados_regra in dados_solucao['regras'].items():
                print(f"  Regra: {dados_regra['nome']}")
                for id_documento, doc_info in dados_regra['documentos'].items():
                    print(f"    Documento: {doc_info['nome']}")
                    for id_linha, linha in doc_info['linhas']:
                        print(f"      Linha {id_linha}: {linha}")
            print()  # Linha em branco para separar soluções

    def salvar_projeto(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            json.dump(self.solucao, f, indent=4)
        print(f"Projeto salvo em '{nome_arquivo}'.")

    def carregar_projeto(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as f:
                self.solucao = json.load(f)
            print(f"Projeto '{nome_arquivo}' carregado.")
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")

def menu():
    projeto = Projeto()
    while True:
        print("\nMenu:")
        print("1. Adicionar Solução")
        print("2. Adicionar Regra")
        print("3. Adicionar Documento")
        print("4. Adicionar Linha")
        print("5. Listar Dados em Tabela")
        print("6. Listar Dados Separados")
        print("7. Salvar Projeto")
        print("8. Carregar Projeto")
        print("9. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id_solucao = input("Digite o ID da solução: ")
            nome_solucao = input("Digite o nome da solução: ")
            projeto.adicionar_solucao(id_solucao, nome_solucao)

        elif escolha == '2':
            id_solucao = input("Digite o ID da solução: ")
            id_regra = input("Digite o ID da regra: ")
            nome_regra = input("Digite o nome da regra: ")
            projeto.adicionar_regra(id_solucao, id_regra, nome_regra)

        elif escolha == '3':
            id_solucao = input("Digite o ID da solução: ")
            id_regra = input("Digite o ID da regra: ")
            id_documento = input("Digite o ID do documento: ")
            nome_documento = input("Digite o nome do documento: ")
            projeto.adicionar_documento(id_solucao, id_regra, id_documento, nome_documento)

        elif escolha == '4':
            id_solucao = input("Digite o ID da solução: ")
            id_regra = input("Digite o ID da regra: ")
            id_documento = input("Digite o ID do documento: ")
            projeto.adicionar_linha(id_solucao, id_regra, id_documento)

        elif escolha == '5':
            projeto.listar_dados_tabela()

        elif escolha == '6':
            projeto.listar_dados_separado()

        elif escolha == '7':
            nome_arquivo = input("Digite o nome do arquivo para salvar (com .json): ")
            projeto.salvar_projeto(nome_arquivo)

        elif escolha == '8':
            nome_arquivo = input("Digite o nome do arquivo para carregar (com .json): ")
            projeto.carregar_projeto(nome_arquivo)

        elif escolha == '9':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
