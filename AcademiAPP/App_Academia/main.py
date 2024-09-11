from lib.treino import TreinoManager
from lib.exercicio import ExercicioManager

def main():
    treino_manager = TreinoManager('treinos.txt')
    exercicio_manager = ExercicioManager('exercicios.txt')

    while True:
        print("\n1 - Consultar um Treino")
        print("2 - Cadastrar um Treino")
        print("3 - Atualizar um Treino")
        print("4 - Remover um Treino")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do treino: ")
            treino = treino_manager.buscar_treino(nome)
            if treino:
                print(f"\nTreino: {treino['nome']}")
                exercicios = exercicio_manager.buscar_exercicios_por_treino(treino['id'])
                for ex in exercicios:
                    print(f"Exercício: {ex['nome']}, Séries: {ex['series']}, Repetições: {ex['repeticoes']}, Peso: {ex['peso']}kg")
            else:
                print("Treino não encontrado.")

        elif opcao == "2":
            nome = input("Digite o nome do treino: ")
            treino_id = treino_manager.adicionar_treino(nome)
            while True:
                exercicio = input("Digite o nome do exercício (ou 'fim' para terminar): ")
                if exercicio.lower() == 'fim':
                    break
                series = int(input(f"Número de séries para {exercicio}: "))
                repeticoes = int(input(f"Número de repetições para {exercicio}: "))
                peso = float(input(f"Peso utilizado para {exercicio} (em kg): "))
                exercicio_manager.adicionar_exercicio(treino_id, exercicio, series, repeticoes, peso)
            print("Treino cadastrado com sucesso!")

        elif opcao == "3":
            nome = input("Digite o nome do treino que deseja atualizar: ")
            treino = treino_manager.buscar_treino(nome)
            if treino:
                novo_nome = input("Digite o novo nome do treino (ou Enter para manter o mesmo): ")
                if novo_nome:
                    treino_manager.atualizar_treino(treino['id'], novo_nome)
                print("Exercícios atuais:")
                exercicios = exercicio_manager.buscar_exercicios_por_treino(treino['id'])
                for i, ex in enumerate(exercicios, 1):
                    print(f"{i}. {ex['nome']}, Séries: {ex['series']}, Repetições: {ex['repeticoes']}, Peso: {ex['peso']}kg")
                while True:
                    acao = input("Deseja adicionar (A), atualizar (U) ou remover (R) um exercício? (ou 'fim' para terminar): ")
                    if acao.lower() == 'fim':
                        break
                    elif acao.upper() == 'A':
                        exercicio = input("Nome do novo exercício: ")
                        series = int(input(f"Número de séries para {exercicio}: "))
                        repeticoes = int(input(f"Número de repetições para {exercicio}: "))
                        peso = float(input(f"Peso utilizado para {exercicio} (em kg): "))
                        exercicio_manager.adicionar_exercicio(treino['id'], exercicio, series, repeticoes, peso)
                    elif acao.upper() == 'U':
                        index = int(input("Número do exercício a atualizar: ")) - 1
                        if 0 <= index < len(exercicios):
                            ex_id = exercicios[index]['id']
                            novo_nome = input("Novo nome do exercício (ou Enter para manter): ")
                            novas_series = input("Novo número de séries (ou Enter para manter): ")
                            novas_repeticoes = input("Novo número de repetições (ou Enter para manter): ")
                            novo_peso = input("Novo peso em kg (ou Enter para manter): ")
                            exercicio_manager.atualizar_exercicio(
                                ex_id, 
                                novo_nome or None, 
                                int(novas_series) if novas_series else None,
                                int(novas_repeticoes) if novas_repeticoes else None,
                                float(novo_peso) if novo_peso else None
                            )
                        else:
                            print("Índice inválido.")
                    elif acao.upper() == 'R':
                        index = int(input("Número do exercício a remover: ")) - 1
                        if 0 <= index < len(exercicios):
                            exercicio_manager.remover_exercicio(exercicios[index]['id'])
                        else:
                            print("Índice inválido.")
                print("Treino atualizado com sucesso!")
            else:
                print("Treino não encontrado.")

        elif opcao == "4":
            nome = input("Digite o nome do treino que deseja remover: ")
            treino = treino_manager.buscar_treino(nome)
            if treino:
                confirmacao = input(f"Tem certeza que deseja remover o treino '{nome}'? (S/N): ")
                if confirmacao.upper() == 'S':
                    treino_manager.remover_treino(treino['id'])
                    exercicio_manager.remover_exercicios_por_treino(treino['id'])
                    print("Treino removido com sucesso!")
                else:
                    print("Operação cancelada.")
            else:
                print("Treino não encontrado.")

        elif opcao == "5":
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
