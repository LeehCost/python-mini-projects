
#dicionario = chaves
#igual ao struct no c, forma de oranizar varios dados bibliotecas possuem metodos
#pack e gri \ conrole de pedidos site get pega o vaor digiado e add em uma variavel

import tkinter as tk
from tkinter import messagebox
# dicionario para armazenar dados
dados = {}
#funcao para add pessoa
def adicionar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    if nome == "" or idade =="":
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return
    dados[nome] = idade
    atualizar_lista()
    entry_nome.delete(0,tk.END)
    entry_idade.delete(0, tk.END)
# funcao para atualizar lista na tela e o delete para limpar e salvar o prox
def atualizar_lista():
    lista.delete(0,tk.END)
    for nome, idade in dados.items():
        lista.insert(tk.END, f"{nome} - {idade} years")
# funcao para remover pessoa
def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Warning", "Select someone to remove!")
        return
    texto = lista.get(selecionado)
    nome = texto.split(" - ")[0]
    del dados[nome]
    atualizar_lista()
# criando janela principal
janela = tk.Tk()
janela.title("Dictionary-based registration")
#labels e entradas
tk.Label(janela,text="Name: ").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()
tk.Label(janela, text= "Age: ").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()
#botoes
tk.Button(janela, text="Add", command=adicionar).pack(pady=5)
tk.Button(janela, text="Remove", command=remover).pack(pady=5)
# lista
lista = tk.Listbox(janela,width=40)
lista.pack(pady=10)


janela.mainloop()
