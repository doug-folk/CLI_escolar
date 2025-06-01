import sys
import os
import cmd
import tkinter as tk
from tkinter import filedialog
from db import Database
from operations.insert import Inserir
from operations.queries import Consultas
from operations.batch import Batch 

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

db = Database()

def escolher_arquivo():
    root = tk.Tk()
    root.withdraw()
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")]
    )
    root.destroy()
    return caminho

class EscolaCLI(cmd.Cmd):
    intro = "Bem-vindo ao sistema escolar CLI. Digite 'help' para ver os comandos disponíveis."
    prompt = "(escola) "

    def do_listar_alunos(self, arg):
        Consultas.listar_alunos()

    def do_listar_professores(self, arg):
        Consultas.listar_professores()

    def do_listar_disciplinas(self, arg):
        Consultas.listar_disciplinas()

    def do_listar_notas(self, arg):
        try:
            aluno_id = int(arg.strip())
            Consultas.listar_notas(aluno_id)
        except Exception:
            print("Uso: listar_notas aluno_id obrigatório")

    def do_listar_frequencia(self, arg):
        try:
            aluno_id, turma_id = arg.split(',')
            Consultas.frequencia_aluno(int(aluno_id.strip()), int(turma_id.strip()))
        except Exception:
            print("Uso: listar_frequencia aluno_id,turma_id")

    def do_inserir_aluno(self, arg):
        try:
            nome, matricula = arg.split(',')
            session = db.get_session()  
            Inserir.add_aluno(session, nome.strip(), matricula.strip())
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_aluno nome,matricula")
            print(f"Erro: {e}")


    def do_inserir_professor(self, arg):
        try:
            nome, email = arg.split(',')
            session = db.get_session()
            Inserir.add_professor(session, nome.strip(), email.strip())
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_professor nome,email")
            print(f"Erro: {e}")

    def do_inserir_disciplina(self, arg):
        try:
            nome, professor_id = arg.split(',')
            session = db.get_session()
            Inserir.add_disciplina(session, nome.strip(), int(professor_id.strip()))
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_discplina nome,professor_id")
            print(f"Erro: {e}")

    def do_inserir_turma(self, arg):
        try:
            nome, disciplina_id = arg.split(',')
            session = db.get_session()
            Inserir.add_turma(session, nome.strip(), int(disciplina_id.strip()))
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_turma nome,disciplina_id")
            print(f"Erro: {e}")

    def do_inserir_nota(self, arg):
        try:
            aluno_id, turma_id, valor = arg.split(',')
            session = db.get_session()
            Inserir.add_nota(session, int(aluno_id.strip()), int(turma_id.strip()), float(valor.strip()))
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_nota aluno_id,turma_id,valor")
            print(f"Erro: {e}")

    def do_inserir_frequencia(self, arg):
        try:
            aluno_id, turma_id, data_str, presente = arg.split(',')
            presente_bool = presente.strip().lower() in ['true', '1', 'sim', 's']
            session = db.get_session()
            Inserir.add_frequencia(session, int(aluno_id.strip()), int(turma_id.strip()), data_str.strip(), presente_bool)
            session.commit()
            session.close()
        except Exception as e:
            print("Uso: inserir_frequenica aluno_id,turma_id,data<AAAA-MM-DD>,present(True,False)")
            print(f"Erro: {e}")

    def _importar_arquivo(self, arg, func_batch, nome_entidade):
        if not arg:
            print(f"Nenhum arquivo informado para importar {nome_entidade}, abrindo diálogo para selecionar arquivo...")
            arquivo = escolher_arquivo()
            if not arquivo:
                print("Nenhum arquivo selecionado.")
                return
        else:
            arquivo = arg.strip()
        try:
            func_batch(arquivo)
            print(f"{nome_entidade.capitalize()} importados com sucesso.")
        except Exception as e:
            print(f"Erro ao importar {nome_entidade}: {e}")

    def do_importar_alunos(self, arg):
        self._importar_arquivo(arg, Batch.add_alunos_batch, "alunos")

    def do_importar_professores(self, arg):
        self._importar_arquivo(arg, Batch.add_professores_batch, "professores")

    def do_importar_disciplinas(self, arg):
        self._importar_arquivo(arg, Batch.add_disciplinas_batch, "disciplinas")

    def do_importar_turmas(self, arg):
        self._importar_arquivo(arg, Batch.add_turmas_batch, "turmas")

    def do_importar_notas(self, arg):
        self._importar_arquivo(arg, Batch.add_notas_batch, "notas")

    def do_importar_frequencias(self, arg):
        self._importar_arquivo(arg, Batch.add_frequencias_batch, "frequências")

    def do_exit(self, arg):
        print("Saindo...")
        return True

if __name__ == '__main__':
    EscolaCLI().cmdloop()
