from db import Database
import csv
from operations.insert import Inserir
db = Database()

class Batch:
    @staticmethod
    def _processar_lote(callback):
        session = db.get_session()
        try:
            callback(session)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def add_professores_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Inserir.add_professor(session, row['nome'], row['email'])
        Batch._processar_lote(processar)

    @staticmethod
    def add_alunos_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Inserir.add_aluno(session, row['nome'], row['matricula'])
        Batch._processar_lote(processar)

    @staticmethod
    def add_disciplinas_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    professor_id = int(row['professor_id'])
                    Inserir.add_disciplina(session, row['nome'], professor_id)
        Batch._processar_lote(processar)

    @staticmethod
    def add_turmas_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    disciplina_id = int(row['disciplina_id'])
                    Inserir.add_turma(session, row['nome'], disciplina_id)
        Batch._processar_lote(processar)

    @staticmethod
    def add_notas_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    aluno_id = int(row['aluno_id'])
                    turma_id = int(row['turma_id'])
                    valor = float(row['valor'])
                    Inserir.add_nota(session, aluno_id, turma_id, valor)
        Batch._processar_lote(processar)

    @staticmethod
    def add_frequencias_batch(arquivo):
        def processar(session):
            with open(arquivo, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    aluno_id = int(row['aluno_id'])
                    turma_id = int(row['turma_id'])
                    data = row['data']
                    presente = row['presente'].lower() in ['true', '1', 'sim', 'yes']
                    Inserir.add_frequencia(session, aluno_id, turma_id, data, presente)
        Batch._processar_lote(processar)