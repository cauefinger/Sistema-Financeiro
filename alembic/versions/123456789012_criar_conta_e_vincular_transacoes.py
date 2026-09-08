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

    # ============================================================
    # 1. CRIA A TABELA CONTA
    # ============================================================

    op.create_table(
        "conta",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("saldo", sa.Float(), nullable=False, server_default="0"),
        sa.Column("usuario_id", sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ["usuario_id"],
            ["usuarios.id"]
        ),

        sa.PrimaryKeyConstraint("id")
    )

    # ============================================================
    # 2. ADICIONA A COLUNA conta_id EM transacoes
    # ============================================================

    op.add_column(
        "transacoes",
        sa.Column(
            "conta_id",
            sa.Integer(),
            nullable=True
        )
    )

    # ============================================================
    # 3. CRIA UMA CONTA PARA CADA USUÁRIO
    # ============================================================

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

    # ============================================================
    # 4. VINCULA CADA TRANSAÇÃO À CONTA DO SEU USUÁRIO
    # ============================================================

    op.execute("""
        UPDATE transacoes
        SET conta_id = (
            SELECT conta.id
            FROM conta
            WHERE conta.usuario_id = transacoes.usuario_id
        )
    """)

    # ============================================================
    # 5. RECONSTRÓI A TABELA transacoes
    #
    # SQLite possui limitações para alterar foreign keys.
    # Aproveitamos para corrigir:
    #
    # categorias -> categoria
    #
    # e criar a FK:
    #
    # conta_id -> conta.id
    # ============================================================

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

            FOREIGN KEY(categoria_id)
                REFERENCES categoria (id),

            FOREIGN KEY(usuario_id)
                REFERENCES usuarios (id),

            FOREIGN KEY(conta_id)
                REFERENCES conta (id)
        )
    """)

    # ============================================================
    # 6. COPIA OS DADOS DA TABELA ANTIGA
    # ============================================================

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

    # ============================================================
    # 7. REMOVE A TABELA ANTIGA
    # ============================================================

    op.execute("DROP TABLE transacoes")

    # ============================================================
    # 8. RENOMEIA A NOVA TABELA
    # ============================================================

    op.execute("""
        ALTER TABLE transacoes_new
        RENAME TO transacoes
    """)

    op.execute("PRAGMA foreign_keys=ON")


def downgrade() -> None:

    # ============================================================
    # 1. RECONSTRÓI transacoes SEM conta_id
    # ============================================================

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

            FOREIGN KEY(categoria_id)
                REFERENCES categoria (id),

            FOREIGN KEY(usuario_id)
                REFERENCES usuarios (id)
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

    # ============================================================
    # 2. REMOVE A TABELA CONTA
    # ============================================================

    op.drop_table("conta")

    op.execute("PRAGMA foreign_keys=ON")