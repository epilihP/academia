import os

class ExercicioManager:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write("")

    def _ler_exercicios(self):
        exercicios = []
        with open(self.arquivo, 'r') as f:
            for linha in f:
                id, treino_id, nome, series, repeticoes, peso = linha.strip().split('|')
                exercicios.append({
                    'id': int(id),
                    'treino_id': int(treino_id),
                    'nome': nome,
                    'series': int(series),
                    'repeticoes': int(repeticoes),
                    'peso': float(peso)
                })
        return exercicios

    def _escrever_exercicios(self, exercicios):
        with open(self.arquivo, 'w') as f:
            for ex in exercicios:
                f.write(f"{ex['id']}|{ex['treino_id']}|{ex['nome']}|{ex['series']}|{ex['repeticoes']}|{ex['peso']}\n")

    def adicionar_exercicio(self, treino_id, nome, series, repeticoes, peso):
        exercicios = self._ler_exercicios()
        novo_id = max([ex['id'] for ex in exercicios], default=0) + 1
        exercicios.append({
            'id': novo_id,
            'treino_id': treino_id,
            'nome': nome,
            'series': series,
            'repeticoes': repeticoes,
            'peso': peso
        })
        self._escrever_exercicios(exercicios)

    def buscar_exercicios_por_treino(self, treino_id):
        exercicios = self._ler_exercicios()
        return [ex for ex in exercicios if ex['treino_id'] == treino_id]

    def atualizar_exercicio(self, exercicio_id, nome=None, series=None, repeticoes=None, peso=None):
        exercicios = self._ler_exercicios()
        for ex in exercicios:
            if ex['id'] == exercicio_id:
                if nome is not None:
                    ex['nome'] = nome
                if series is not None:
                    ex['series'] = series
                if repeticoes is not None:
                    ex['repeticoes'] = repeticoes
                if peso is not None:
                    ex['peso'] = peso
                break
        self._escrever_exercicios(exercicios)

    def remover_exercicio(self, exercicio_id):
        exercicios = self._ler_exercicios()
        exercicios = [ex for ex in exercicios if ex['id'] != exercicio_id]
        self._escrever_exercicios(exercicios)

    def remover_exercicios_por_treino(self, treino_id):
        exercicios = self._ler_exercicios()
        exercicios = [ex for ex in exercicios if ex['treino_id'] != treino_id]
        self._escrever_exercicios(exercicios)