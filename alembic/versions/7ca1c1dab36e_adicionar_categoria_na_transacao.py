"""adicionar categoria na transacao

Revision ID: 7ca1c1dab36e
Revises: 123456789012
Create Date: 2026-09-13 17:39:11.542715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca1c1dab36e'
down_revision: Union[str, Sequence[str], None] = '123456789012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    categoria_enum = sa.Enum(
        'GERAL',
        'NECESSIDADES',
        'LAZER',
        'DIVIDAS',
        'INVESTIMENTO',
        'RENDA_EXTRA',
        'TRANSFERENCIA',
        'SALARIO',
        'TRANSPORTE',
        'MORADIA',
        'SAUDE',
        name='categoria'
    )

    with op.batch_alter_table('transacoes') as batch_op:

        # Cria a nova coluna categoria.
        batch_op.add_column(
            sa.Column(
                'categoria',
                categoria_enum,
                nullable=False,
                server_default='GERAL'
            )
        )

        # Remove a antiga FK.
        batch_op.drop_column('categoria_id')

    # Remove o default usado apenas durante a migração.
    with op.batch_alter_table('transacoes') as batch_op:
        batch_op.alter_column(
            'categoria',
            server_default=None
        )

    # As tabelas antigas de categorias não são mais necessárias.
    op.drop_table('categorias')
    op.drop_table('categoria')


def downgrade() -> None:
    """Downgrade schema."""

    # Recria as tabelas antigas, se necessário.
    op.create_table(
        'categoria',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'categorias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    with op.batch_alter_table('transacoes') as batch_op:
        batch_op.add_column(
            sa.Column(
                'categoria_id',
                sa.Integer(),
                nullable=True
            )
        )

        batch_op.drop_column('categoria')