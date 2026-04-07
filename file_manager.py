import os
def criar_arquivo():
    nome = input("Enter the file name (e.g., teste.txt): ")
    conteudo = input("Enter initial content: ")
    with open(nome, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print("File created successfully at:", os.path.abspath(nome))

def ler_arquivo():
    nome = input("Enter the file name: ")
    if os.path.exists(nome):
      with open(nome, "r", encoding="utf-8") as f:
       print("\nFile content:\n")
       print(f.read())
    else:
        print("File not found!")

def adicionar_conteudo():
    nome = input("Enter the file name: ")
    if os.path.exists(nome):
        novo = input("Enter content to add: ")
        with open(nome,"a", encoding="utf-8") as f:
            f.write("\n" + novo)
        print("Content added!!")
    else:
        print("File not found!")

def excluir_arquivo():
    nome = input("Enter the file name: ")
    if os.path.exists(nome):
        os.remove(nome)
        print("FIle deleted successfully!!")
    else:
        print("File not found")

def menu():
    while True:
        print("\n=== FILE MANAGER ===")
        print("1 - Create file")
        print("2 - Read file")
        print("3 - Add content")
        print("4 - Delete file")
        print("0 - Exit")
        opcao = input("Choose an option: ")
        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            ler_arquivo()
        elif opcao == "3":
            adicionar_conteudo()
        elif opcao == "4":
            excluir_arquivo()
        elif opcao == "0":
            print("Exiting... ")
            break
        else:
            print("Invalid option!")
menu()
