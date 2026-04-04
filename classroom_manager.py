alunos = {}

total_alunos = int(input("How many students are in the class? "))

for i in range(total_alunos):
    print(f"\n == Student {i+1} registration ==")

    nome = input("Enter student name: ")
    idade = input("Enter student age:")

    notas = []
    quantidade_notas = int(input("How many grades for this student? "))

    for j in range(quantidade_notas):
        nota = float(input(f"Enter grade {j+1}: "))
        notas.append(nota)

    alunos[nome] = {
        "idade": idade, "notas": notas}
    

print("\n ** Student List **")

for nome, dados in alunos.items():
    notas = dados["notas"]
    media = sum(notas) / len(notas)

    if media >= 7:
        status = "Approved"
    else:
        status = "Failed"

    print(f"\nStudent:{nome}")
    print(f"\nAge: {dados['idade']}")
    print(f"Grades: {notas}")
    print(f"Average: {media:.2f}")
    print(f"Status: {status}")
