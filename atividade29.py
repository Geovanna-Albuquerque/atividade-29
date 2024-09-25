
def verificar_presenca(alunos_presentes):
    # Contar o número de alunos presentes
    total_presentes = len(alunos_presentes)

    # Exibir o total de alunos presentes e a lista
    print(f"Alunos presentes: {total_presentes}")
    print("Lista de alunos presentes:", ", ".join(alunos_presentes))

    # Verificar se o total de alunos presentes é menor que 5
    if total_presentes < 5:
        print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")
# Exemplo de uso
alunos = ['Ana', 'Bruno', 'Carlos', 'Daniela']
verificar_presenca(alunos)