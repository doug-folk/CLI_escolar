from models import Professor, Aluno, Disciplina, Turma, Nota, Frequencia
from db import Database

db = Database()
session = db.get_session()

class Consultas:
    @staticmethod
    def listar_professores():
        professores = session.query(Professor).all()
        for p in professores:
            print(p)

    @staticmethod
    def listar_alunos():
        alunos = session.query(Aluno).all()
        for a in alunos:
            print(a)

    @staticmethod
    def listar_disciplinas():
        disciplinas = session.query(Disciplina).all()
        for d in disciplinas:
            print(d)

    @staticmethod
    def listar_turmas():
        turmas = session.query(Turma).all()
        for t in turmas:
            print(t)

    @staticmethod
    def listar_notas(aluno_id):
        notas = session.query(Nota).filter_by(aluno_id=aluno_id).all()
        
        if not notas:
            print(f"Nenhuma nota encontrada para aluno_id {aluno_id}")
            return

        print(f"Notas do aluno ID {aluno_id}:\n")
        for nota in notas:
            print(f"Turma: {nota.turma_id} | Nota: {nota.valor}")

    @staticmethod
    def frequencia_aluno(aluno_id, turma_id):
        frequencias = session.query(Frequencia).filter_by(aluno_id=aluno_id, turma_id=turma_id).all()
        if not frequencias:
            print(f"Nenhuma frequência encontrada para aluno ID {aluno_id} na turma ID {turma_id}")
        else:
            print(f"Frequências do aluno ID {aluno_id} na turma ID {turma_id}:")
            for f in frequencias:
                print(f)


