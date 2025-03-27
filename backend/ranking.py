class RankingGamificacao:
    def __init__(self):
        self.alunos = {}
        self.categorias = [
            (0, "Bronze"), (100, "Prata"), (250, "Ouro"),
            (500, "Platina"), (1000, "Diamante"), (1500, "Challenge"), (2000, "Imortal")
        ]

    def adicionar_pontos(self, aluno, pontos):
        if aluno not in self.alunos:
            self.alunos[aluno] = 0
        self.alunos[aluno] += pontos

    def obter_categoria(self, aluno):
        pontos = self.alunos.get(aluno, 0)
        for limite, categoria in reversed(self.categorias):
            if pontos >= limite:
                return categoria
        return "Bronze"
    
    def mostrar_ranking(self):
        print("="*30)
        print("RANKING DE ALUNOS")
        print("="*30)
        ranking = sorted(self.alunos.items(), key=lambda x: x[1], reverse=True)
        for i, (aluno, pontos) in enumerate(ranking, 1):
            print(f"{i}. {aluno} - {pontos} pontos - {self.obter_categoria(aluno)}")
        print("="*30)
    
    def mostrar_detalhes_aluno(self, aluno):
        print("="*30)
        print(f"DETALHES DE {aluno.upper()}")
        print("="*30)
        if aluno in self.alunos:
            print(f"Pontos: {self.alunos[aluno]}")
            print(f"Categoria: {self.obter_categoria(aluno)}")
        else:
            print("Aluno não encontrado.")
        print("="*30)

# Exemplo de uso
ranking = RankingGamificacao()
ranking.adicionar_pontos("Alice", 120)
ranking.adicionar_pontos("Bob", 600)
ranking.adicionar_pontos("Carlos", 1800)
ranking.mostrar_ranking()
ranking.mostrar_detalhes_aluno("Bob")