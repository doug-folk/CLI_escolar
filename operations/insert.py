from models import Professor, Aluno, Disciplina, Turma, TurmaAluno, Nota, Frequencia
from datetime import datetime

class Inserir:
    @staticmethod
    def add_professor(session, nome, email):
        professor = Professor(nome=nome, email=email)
        session.add(professor)
        print(f"Professor '{nome}' adicionado.")

    @staticmethod
    def add_aluno(session, nome, matricula):
        aluno = Aluno(nome=nome, matricula=matricula)
        session.add(aluno)
        print(f"Aluno '{nome}' adicionado.")

    @staticmethod
    def add_disciplina(session, nome, professor_id):
        disciplina = Disciplina(nome=nome, professor_id=professor_id)
        session.add(disciplina)
        print(f"Disciplina '{nome}' adicionada.")

    @staticmethod
    def add_turma(session, nome, disciplina_id):
        turma = Turma(nome=nome, disciplina_id=disciplina_id)
        session.add(turma)
        print(f"Turma '{nome}' adicionada.")

    @staticmethod
    def add_nota(session, aluno_id, turma_id, valor):
        nota = Nota(aluno_id=aluno_id, turma_id=turma_id, valor=valor)
        session.add(nota)
        print(f"Nota {valor} adicionada para aluno_id {aluno_id} na turma_id {turma_id}.")

    @staticmethod
    def add_frequencia(session, aluno_id, turma_id, data_str, presente):
        data = datetime.strptime(data_str, "%Y-%m-%d").date()
        frequencia = Frequencia(aluno_id=aluno_id, turma_id=turma_id, data=data, presente=presente)
        session.add(frequencia)
        print(f"Frequência adicionada para aluno_id {aluno_id} na turma_id {turma_id} em {data} (Presente={presente}).")
