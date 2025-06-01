#  CLI Escolar - Sistema de Gerenciamento Escolar (via terminal)

Este projeto é um sistema de gerenciamento escolar simples via **linha de comando (CLI)**, desenvolvido em **Python** com banco de dados **PostgreSQL**, utilizando **SQLAlchemy ORM**.

## Funcionalidades

- Inserir e listar alunos, professores, disciplinas, turmas, notas e frequência
- Insert manual via cli e em lote via csv
- Banco de dados relacional com relacionamentos entre entidades
- Interface por linha de comando com o módulo `cmd`

---

## Requisitos

- Python 3.10 ou superior
- PostgreSQL
- `virtualenv` (opcional, mas recomendado)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/CLI_escolar.git
cd CLI_escolar
```

### 2. Crie e ative um ambiente virtual (opcional)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se o arquivo `requirements.txt` não existir, você pode instalar manualmente:

```bash
pip install sqlalchemy psycopg2
```

---

## Configuração do Banco de Dados

1. Crie um banco de dados no PostgreSQL:

```sql
CREATE DATABASE escola;
```

2. Configure a string de conexão no seu projeto, geralmente no arquivo `database.py`:

```python
self.engine = create_engine("postgresql://usuario:senha@localhost/escola")
```

Substitua `usuario`, `senha` e `escola` pelos dados reais do seu PostgreSQL.

3. Rode a criação das tabelas (isso ocorre automaticamente ao rodar o CLI, pois o sistema usa `Base.metadata.create_all(engine)`).

---

## Executando o Sistema

Execute o CLI com:

```bash
python3 cli.py
```

Você verá o prompt:

```bash
(escola)
```

Agora, você pode usar os seguintes comandos:

---

## Comandos disponíveis

| Comando                   | Uso                                                      |
|--------------------------|-----------------------------------------------------------|
| `inserir_aluno`          | inserir_aluno nome,matricula                             |
| `inserir_professor`      | inserir_professor nome,email                             |
| `inserir_disciplina`     | inserir_disciplina nome,professor_id                     |
| `inserir_turma`          | inserir_turma nome,disciplina_id                         |
| `inserir_nota`           | inserir_nota aluno_id,turma_id,valor                     |
| `inserir_frequencia`     | inserir_frequencia aluno_id,turma_id,data,presente       |
| `listar_alunos`          | Lista todos os alunos                                     |
| `listar_professores`     | Lista todos os professores                                |
| `listar_disciplinas`     | Lista todas as disciplinas                                |
| `listar_turmas`          | Lista todas as turmas                                     |
| `listar_notas`           | Lista todas as notas                                      |
| `listar_frequencias`     | Lista todas as frequências                                |
| `sair`                   | Encerra o CLI                                             |


---

## Exemplo de uso

```bash
(escola) inserir_aluno João Silva,2023010
(escola) inserir_professor Carla Lima,carla@email.com
(escola) inserir_disciplina Matemática,1
(escola) inserir_turma Turma A,1
(escola) inserir_nota 1,1,8.5
(escola) inserir_frequencia 1,1,2024-05-01,sim
```

---

## Observações

- Certifique-se de que o PostgreSQL está ativo e aceitando conexões.
- Caso ocorra erro ao conectar ao banco, revise o `database.py` e a string de conexão.

---

## Licença

Este projeto é livre para fins acadêmicos e educacionais.

---

## Autor

Douglas Rocha Felipe
