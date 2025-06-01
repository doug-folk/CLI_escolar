import argparse
from operations.insert import Inserir
from operations.batch import Batch
from operations.queries import Consultas
from db import Database

def main():
    db = Database()
    db.criar_tabelas()

    parser = argparse.ArgumentParser(description="Sistema de Gerenciamento Escolar")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # --- Inserção individual ---
    p = subparsers.add_parser("add-professor")
    p.add_argument("--nome", required=True)
    p.add_argument("--email", required=True)
    p.set_defaults(func=lambda args: Inserir.add_professor(args.nome, args.email))

    p = subparsers.add_parser("add-aluno")
    p.add_argument("--nome", required=True)
    p.add_argument("--matricula", required=True)
    p.set_defaults(func=lambda args: Inserir.add_aluno(args.nome, args.matricula))

    p = subparsers.add_parser("add-disciplina")
    p.add_argument("--nome", required=True)
    p.add_argument("--creditos", type=int, required=True)
    p.add_argument("--ementa", default="")
    p.set_defaults(func=lambda args: Inserir.add_disciplina(args.nome, args.creditos, args.ementa))

    p = subparsers.add_parser("add-turma")
    p.add_argument("--nome", required=True)
    p.add_argument("--disciplina-id", type=int, required=True)
    p.add_argument("--professor-id", type=int, required=True)
    p.set_defaults(func=lambda args: Inserir.add_turma(args.nome, args.disciplina_id, args.professor_id))

    p = subparsers.add_parser("add-nota")
    p.add_argument("--aluno-id", type=int, required=True)
    p.add_argument("--turma-id", type=int, required=True)
    p.add_argument("--valor", type=float, required=True)
    p.set_defaults(func=lambda args: Inserir.add_nota(args.aluno_id, args.turma_id, args.valor))

    p = subparsers.add_parser("add-frequencia")
    p.add_argument("--aluno-id", type=int, required=True)
    p.add_argument("--turma-id", type=int, required=True)
    p.add_argument("--data", required=True)
    p.add_argument("--presente", type=bool, required=True)
    p.set_defaults(func=lambda args: Inserir.add_frequencia(args.aluno_id, args.turma_id, args.data, args.presente))

    # --- Batch ---
    p = subparsers.add_parser("add-professores-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_professores_batch(args.arquivo))

    p = subparsers.add_parser("add-alunos-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_alunos_batch(args.arquivo))

    p = subparsers.add_parser("add-disciplinas-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_disciplinas_batch(args.arquivo))

    p = subparsers.add_parser("add-turmas-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_turmas_batch(args.arquivo))

    p = subparsers.add_parser("add-notas-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_notas_batch(args.arquivo))

    p = subparsers.add_parser("add-frequencias-batch")
    p.add_argument("--arquivo", required=True)
    p.set_defaults(func=lambda args: Batch.add_frequencias_batch(args.arquivo))

    # --- Consultas ---
    p = subparsers.add_parser("listar-alunos")
    p.set_defaults(func=lambda args: Consultas.listar_alunos())

    p = subparsers.add_parser("listar-professores")
    p.set_defaults(func=lambda args: Consultas.listar_professores())

    p = subparsers.add_parser("listar-turmas")
    p.set_defaults(func=lambda args: Consultas.listar_turmas())

    p = subparsers.add_parser("listar-disciplinas")
    p.set_defaults(func=lambda args: Consultas.listar_disciplinas())

    p = subparsers.add_parser("listar-notas")
    p.add_argument("--aluno-id", type=int, required=True)
    p.set_defaults(func=lambda args: Consultas.listar_notas(args.aluno_id))

    p = subparsers.add_parser("frequencia-aluno")
    p.add_argument("--aluno-id", type=int, required=True)
    p.add_argument("--turma-id", type=int, required=True)
    p.set_defaults(func=lambda args: Consultas.frequencia_aluno(args.aluno_id, args.turma_id))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
