"""criar conta e vincular transacoes

Revision ID: 123456789012
Revises: 26c8ff796de2
Create Date: 2026-09-06
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "123456789012"
down_revision: Union[str, Sequence[str], None] = "26c8ff796de2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # A coluna conta_id já foi criada pela tentativa anterior
    # desta migration.
    #
    # Portanto, não usamos op.add_column() novamente.

    # 1. Cria uma conta para cada usuário que ainda não possui conta.
    op.execute("""
        INSERT INTO conta (saldo, usuario_id)
        SELECT 0, u.id
        FROM usuarios u
        WHERE NOT EXISTS (
            SELECT 1
            FROM conta c
            WHERE c.usuario_id = u.id
        )
    """)

    # 2. Vincula cada transação à conta do seu usuário.
    op.execute("""
        UPDATE transacoes
        SET conta_id = (
            SELECT conta.id
            FROM conta
            WHERE conta.usuario_id = transacoes.usuario_id
        )
    """)

    # 3. O SQLite não consegue usar batch_alter_table()
    #    porque a FK antiga aponta para "categorias", tabela
    #    que não existe mais.
    #
    #    Portanto, reconstruímos a tabela transacoes manualmente,
    #    já corrigindo a FK para "categoria".

    op.execute("PRAGMA foreign_keys=OFF")

    op.execute("""
        CREATE TABLE transacoes_new (
            id INTEGER NOT NULL PRIMARY KEY,
            Descricao VARCHAR,
            Valor FLOAT NOT NULL,
            tipo VARCHAR(7) NOT NULL,
            data DATE NOT NULL,
            categoria_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            conta_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria (id),
            FOREIGN KEY(usuario_id) REFERENCES usuarios (id),
            FOREIGN KEY(conta_id) REFERENCES conta (id)
        )
    """)

    # 4. Copia os dados existentes para a nova tabela.
    op.execute("""
        INSERT INTO transacoes_new (
            id,
            Descricao,
            Valor,
            tipo,
            data,
            categoria_id,
            usuario_id,
            conta_id
        )
        SELECT
            id,
            Descricao,
            Valor,
            tipo,
            data,
            categoria_id,
            usuario_id,
            conta_id
        FROM transacoes
    """)

    # 5. Remove a tabela antiga.
    op.execute("DROP TABLE transacoes")

    # 6. Renomeia a nova tabela.
    op.execute("""
        ALTER TABLE transacoes_new
        RENAME TO transacoes
    """)

    op.execute("PRAGMA foreign_keys=ON")


def downgrade() -> None:

    # Remove a FK/coluna conta_id reconstruindo a tabela,
    # pois SQLite possui limitações para alteração de FKs.

    op.execute("PRAGMA foreign_keys=OFF")

    op.execute("""
        CREATE TABLE transacoes_old (
            id INTEGER NOT NULL PRIMARY KEY,
            Descricao VARCHAR,
            Valor FLOAT NOT NULL,
            tipo VARCHAR(7) NOT NULL,
            data DATE NOT NULL,
            categoria_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria (id),
            FOREIGN KEY(usuario_id) REFERENCES usuarios (id)
        )
    """)

    op.execute("""
        INSERT INTO transacoes_old (
            id,
            Descricao,
            Valor,
            tipo,
            data,
            categoria_id,
            usuario_id
        )
        SELECT
            id,
            Descricao,
            Valor,
            tipo,
            data,
            categoria_id,
            usuario_id
        FROM transacoes
    """)

    op.execute("DROP TABLE transacoes")

    op.execute("""
        ALTER TABLE transacoes_old
        RENAME TO transacoes
    """)

    op.execute("PRAGMA foreign_keys=ON")
