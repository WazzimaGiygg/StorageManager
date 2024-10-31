import json
import tkinter as tk
from tkinter import font, filedialog, messagebox, simpledialog, colorchooser

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Editor de Texto Formatado")

        self.text = tk.Text(master, wrap='word', font=("Arial", 12))
        self.text.pack(expand=1, fill='both')

        self.create_menu()
        self.create_toolbar()

        self.bold = False
        self.italic = False
        self.underline = False
        self.font_family = "Arial"
        self.font_size = 12

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # Menu Arquivo
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_as_json)
        self.file_menu.add_command(label="Exportar .TXT", command=self.export_txt)
        self.file_menu.add_command(label="Importar .TXT", command=self.import_txt)
        self.file_menu.add_command(label="Imprimir", command=self.print_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.master.quit)

        # Menu Editar
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Localizar", command=self.find_text)
        self.edit_menu.add_command(label="Localizar e Substituir", command=self.replace_text)
        self.edit_menu.add_command(label="Exibir/Ocultar Régua", command=self.toggle_ruler)
        self.edit_menu.add_command(label="Quebra Automática de Linha", command=self.toggle_wrap)
        self.edit_menu.add_command(label="Ampliar Zoom", command=self.zoom_in)
        self.edit_menu.add_command(label="Reduzir Zoom", command=self.zoom_out)

        # Menu Formatação
        self.format_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Formatar", menu=self.format_menu)
        self.format_menu.add_command(label="Selecionar Fonte", command=self.choose_font)

        # Tamanho da Fonte
        self.size_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tamanho da Fonte", menu=self.size_menu)
        for size in range(8, 33, 2):
            self.size_menu.add_command(label=str(size), command=lambda s=size: self.change_font_size(s))

    def create_toolbar(self):
        toolbar = tk.Frame(self.master, bd=1, relief=tk.RAISED)

        # Botão Negrito
        bold_btn = tk.Button(toolbar, text="B", command=self.toggle_bold)
        bold_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Itálico
        italic_btn = tk.Button(toolbar, text="I", command=self.toggle_italic)
        italic_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Sublinhado
        underline_btn = tk.Button(toolbar, text="U", command=self.toggle_underline)
        underline_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Tachado
        strikethrough_btn = tk.Button(toolbar, text="~", command=self.toggle_strikethrough)
        strikethrough_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Cor do Texto
        color_btn = tk.Button(toolbar, text="Cor", command=self.change_text_color)
        color_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Alinhar à Esquerda
        align_left_btn = tk.Button(toolbar, text="A Esquerda", command=lambda: self.align_text('left'))
        align_left_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Alinhar ao Centro
        align_center_btn = tk.Button(toolbar, text="Centro", command=lambda: self.align_text('center'))
        align_center_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Alinhar à Direita
        align_right_btn = tk.Button(toolbar, text="A Direita", command=lambda: self.align_text('right'))
        align_right_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Justificar
        justify_btn = tk.Button(toolbar, text="Justificar", command=lambda: self.align_text('justify'))
        justify_btn.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    # Funções de Arquivo
    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, data["text"])
                self.font_family = data["font"]
                self.font_size = data["size"]
                self.bold = data["bold"]
                self.italic = data["italic"]
                self.underline = data["underline"]
                self.update_font()

    def save_as_json(self):
        content = self.text.get("1.0", tk.END)
        formatting = {
            "font": self.font_family,
            "size": self.font_size,
            "bold": self.bold,
            "italic": self.italic,
            "underline": self.underline,
            "text": content
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                   filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as json_file:
                json.dump(formatting, json_file, indent=4)
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

    def export_txt(self):
        content = self.text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as txt_file:
                txt_file.write(content)
            messagebox.showinfo("Exportado", "Arquivo exportado com sucesso!")

    def import_txt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as txt_file:
                content = txt_file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)

    def print_file(self):
        messagebox.showinfo("Imprimir", "Função de impressão não implementada.")

    def find_text(self):
        search_query = simpledialog.askstring("Localizar", "Texto a localizar:")
        if search_query:
            start = self.text.search(search_query, "1.0", tk.END)
            if start:
                self.text.tag_add("highlight", start, f"{start}+{len(search_query)}c")
                self.text.tag_config("highlight", background="yellow")
            else:
                messagebox.showinfo("Não encontrado", "Texto não encontrado.")

    def replace_text(self):
        search_query = simpledialog.askstring("Localizar", "Texto a localizar:")
        replace_query = simpledialog.askstring("Substituir", "Texto a substituir:")
        if search_query and replace_query:
            content = self.text.get("1.0", tk.END)
            new_content = content.replace(search_query, replace_query)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, new_content)

    def toggle_ruler(self):
        messagebox.showinfo("Régua", "Função de régua não implementada.")

    def toggle_wrap(self):
        current_wrap = self.text.cget("wrap")
        self.text.config(wrap='none' if current_wrap == 'word' else 'word')

    def zoom_in(self):
        self.font_size += 2
        self.update_font()

    def zoom_out(self):
        self.font_size = max(8, self.font_size - 2)
        self.update_font()

    def toggle_bold(self):
        self.bold = not self.bold
        self.apply_formatting()

    def toggle_italic(self):
        self.italic = not self.italic
        self.apply_formatting()

    def toggle_underline(self):
        self.underline = not self.underline
        self.apply_formatting()

    def toggle_strikethrough(self):
        current_tags = self.text.tag_names("sel.first")
        if "strikethrough" in current_tags:
            self.text.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            self.text.tag_add("strikethrough", "sel.first", "sel.last")
            self.text.tag_config("strikethrough", overstrike=True)

    def align_text(self, alignment):
        if alignment == 'left':
            self.text.tag_configure("left", justify='left')
            self.text.tag_add("left", "sel.first", "sel.last")
        elif alignment == 'right':
            self.text.tag_configure("right", justify='right')
            self.text.tag_add("right", "sel.first", "sel.last")
        elif alignment == 'center':
            self.text.tag_configure("center", justify='center')
            self.text.tag_add("center", "sel.first", "sel.last")
        elif alignment == 'justify':
            self.text.tag_configure("justify", justify='justify')
            self.text.tag_add("justify", "sel.first", "sel.last")

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text.tag_add("colored", "sel.first", "sel.last")
            self.text.tag_config("colored", foreground=color)

    def choose_font(self):
        font_family = simpledialog.askstring("Escolher Fonte", "Nome da fonte:")
        if font_family:
            self.font_family = font_family
            self.apply_formatting()

    def change_font_size(self, size):
        self.font_size = size
        self.apply_formatting()

    def apply_formatting(self):
        try:
            start, end = self.text.index("sel.first"), self.text.index("sel.last")
            self.text.tag_add("font", start, end)
            self.text.tag_configure("font", font=(self.font_family, self.font_size))
            if self.bold:
                self.text.tag_configure("bold", font=(self.font_family, self.font_size, 'bold'))
                self.text.tag_add("bold", start, end)
            if self.italic:
                self.text.tag_configure("italic", font=(self.font_family, self.font_size, 'italic'))
                self.text.tag_add("italic", start, end)
            if self.underline:
                self.text.tag_configure("underline", underline=True)
                self.text.tag_add("underline", start, end)
        except tk.TclError:
            pass  # No selection, do nothing

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
