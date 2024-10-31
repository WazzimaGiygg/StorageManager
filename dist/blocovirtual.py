import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.root.geometry("600x400")
        
        # Atributos para gerenciar o arquivo
        self.arquivo_salvo = None

        # Área de texto
        self.text_area = tk.Text(root)
        self.text_area.pack(expand=True, fill='both')

        # Menu principal
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # Menu Arquivo
        arquivo_menu = tk.Menu(self.menu, tearoff=0)
        arquivo_menu.add_command(label="Salvar", command=self.salvar)
        arquivo_menu.add_command(label="Salvar Como", command=self.salvar_como)
        arquivo_menu.add_separator()
        arquivo_menu.add_command(label="Fechar", command=self.fechar)
        self.menu.add_cascade(label="Arquivo", menu=arquivo_menu)

        # Menu Editar
        editar_menu = tk.Menu(self.menu, tearoff=0)
        editar_menu.add_command(label="Desfazer", command=lambda: self.text_area.edit_undo())
        editar_menu.add_command(label="Refazer", command=lambda: self.text_area.edit_redo())
        editar_menu.add_separator()
        editar_menu.add_command(label="Copiar", command=lambda: self.text_area.clipboard_append(self.text_area.selection_get()))
        editar_menu.add_command(label="Excluir", command=lambda: self.text_area.delete("sel.first", "sel.last"))
        editar_menu.add_command(label="Localizar", command=self.localizar)
        editar_menu.add_command(label="Localizar e substituir", command=self.localizar_substituir)
        self.menu.add_cascade(label="Editar", menu=editar_menu)

    def salvar(self):
        if self.arquivo_salvo is None:
            self.salvar_como()
        else:
            try:
                with open(self.arquivo_salvo, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                    messagebox.showinfo("Salvar", f"Arquivo salvo como {self.arquivo_salvo}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar: {e}")

    def salvar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.arquivo_salvo = file_path
            self.salvar()

    def fechar(self):
        self.root.quit()

    def localizar(self):
        termo = simpledialog.askstring("Localizar", "Digite o termo a ser localizado:")
        if termo:
            conteudo = self.text_area.get("1.0", tk.END)
            pos = conteudo.find(termo)
            if pos >= 0:
                self.text_area.tag_remove("highlight", "1.0", tk.END)
                start = f"1.0 + {pos} chars"
                end = f"1.0 + {pos + len(termo)} chars"
                self.text_area.tag_add("highlight", start, end)
                self.text_area.see(start)
                self.text_area.tag_config("highlight", background="yellow")
            else:
                messagebox.showinfo("Localizar", "Termo não encontrado.")

    def localizar_substituir(self):
        termo = simpledialog.askstring("Localizar e Substituir", "Digite o termo a ser localizado:")
        if termo:
            substituto = simpledialog.askstring("Localizar e Substituir", "Digite o novo termo:")
            conteudo = self.text_area.get("1.0", tk.END)
            novo_conteudo = conteudo.replace(termo, substituto)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", novo_conteudo)
            messagebox.showinfo("Localizar e Substituir", f"Substituído '{termo}' por '{substituto}'.")

if __name__ == "__main__":
    root = tk.Tk()
    bloco_de_notas = BlocoDeNotas(root)
    root.mainloop()
