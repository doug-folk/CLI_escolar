from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Boolean, Text
from sqlalchemy.orm import relationship
from db import Base

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Professor(id={self.id}, nome={self.nome}, email={self.email})>"

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    matricula = Column(String, unique=True, nullable=False)
    turmas = relationship("TurmaAluno", back_populates="aluno")
    notas = relationship("Nota", back_populates="aluno")
    frequencias = relationship("Frequencia", back_populates="aluno")

    def __repr__(self):
        return f"<Aluno(id={self.id}, nome={self.nome}, matricula={self.matricula})>"

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    professor_id = Column(Integer, ForeignKey('professores.id'), nullable=False)
    turmas = relationship("Turma", back_populates="disciplina")

    def __repr__(self):
        return f"<Disciplina(id={self.id}, nome={self.nome})>"

class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'), nullable=False)

    disciplina = relationship("Disciplina", back_populates="turmas")
    alunos = relationship("TurmaAluno", back_populates="turma")
    notas = relationship("Nota", back_populates="turma")
    frequencias = relationship("Frequencia", back_populates="turma")

    def __repr__(self):
        return f"<Turma(id={self.id}, nome={self.nome})>"

class TurmaAluno(Base):
    __tablename__ = 'turmas_alunos'
    id = Column(Integer, primary_key=True)
    turma_id = Column(Integer, ForeignKey('turmas.id'), nullable=False)
    aluno_id = Column(Integer, ForeignKey('alunos.id'), nullable=False)

    turma = relationship("Turma", back_populates="alunos")
    aluno = relationship("Aluno", back_populates="turmas")

    def __repr__(self):
        return f"<TurmaAluno(turma_id={self.turma_id}, aluno_id={self.aluno_id})>"

class Nota(Base):
    __tablename__ = 'notas'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'), nullable=False)
    turma_id = Column(Integer, ForeignKey('turmas.id'), nullable=False)
    valor = Column("nota", Float, nullable=False)

    aluno = relationship("Aluno", back_populates="notas")
    turma = relationship("Turma", back_populates="notas")

    def __repr__(self):
        return f"<Nota(aluno_id={self.aluno_id}, turma_id={self.turma_id}, valor={self.valor})>"

class Frequencia(Base):
    __tablename__ = 'frequencias'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'), nullable=False)
    turma_id = Column(Integer, ForeignKey('turmas.id'), nullable=False)
    data = Column(Date, nullable=False)
    presente = Column(Boolean, nullable=False)

    aluno = relationship("Aluno", back_populates="frequencias")
    turma = relationship("Turma", back_populates="frequencias")

    def __repr__(self):
        return f"<Frequencia(aluno_id={self.aluno_id}, turma_id={self.turma_id}, data={self.data}, presente={self.presente})>"
