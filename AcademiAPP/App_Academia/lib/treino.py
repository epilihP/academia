import os

class TreinoManager:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write("")

    def _ler_treinos(self):
        treinos = []
        with open(self.arquivo, 'r') as f:
            for linha in f:
                id, nome = linha.strip().split('|')
                treinos.append({'id': int(id), 'nome': nome})
        return treinos

    def _escrever_treinos(self, treinos):
        with open(self.arquivo, 'w') as f:
            for treino in treinos:
                f.write(f"{treino['id']}|{treino['nome']}\n")

    def adicionar_treino(self, nome):
        treinos = self._ler_treinos()
        novo_id = max([treino['id'] for treino in treinos], default=0) + 1
        treinos.append({'id': novo_id, 'nome': nome})
        self._escrever_treinos(treinos)
        return novo_id

    def buscar_treino(self, nome):
        treinos = self._ler_treinos()
        for treino in treinos:
            if treino['nome'] == nome:
                return treino
        return None

    def atualizar_treino(self, treino_id, novo_nome):
        treinos = self._ler_treinos()
        for treino in treinos:
            if treino['id'] == treino_id:
                treino['nome'] = novo_nome
                break
        self._escrever_treinos(treinos)

    def remover_treino(self, treino_id):
        treinos = self._ler_treinos()
        treinos = [treino for treino in treinos if treino['id'] != treino_id]
        self._escrever_treinos(treinos)