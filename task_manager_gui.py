import tkinter as tk
from tkinter import messagebox
tarefas = {}

def adicionar():
    tarefa = entry_tarefa.get()
    if tarefa == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return
    tarefas[tarefa] = "Pending"
    atualizar_lista()
    entry_tarefa.delete(0,tk.END)

def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa, status in tarefas.items():
        lista.insert(tk.END, f"{tarefa} - {status}")

def concluir():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Warning", "Select a task!")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    tarefas[tarefa] = "Completed"
    atualizar_lista()

def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Warning", "Select a task!")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    del tarefas[tarefa]
    atualizar_lista()

janela = tk.Tk()
janela.title("Task List")

tk.Label(janela, text="New Task:").pack()
entry_tarefa = tk.Entry(janela, width=40)
entry_tarefa.pack()
tk.Button(janela, text="Add", command=adicionar).pack(pady=5)
tk.Button(janela, text="Complete", command=concluir).pack(pady=5)
tk.Button(janela, text="Remove", command=remover).pack(pady=5)
lista = tk.Listbox(janela,width=50)
lista.pack(pady=10)

janela.mainloop()

