"""add user table

Revision ID: 5e6831305f97
Revises: 21a5176d9191
Create Date: 2025-10-19 21:19:53.963068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e6831305f97'
down_revision: Union[str, Sequence[str], None] = '21a5176d9191'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

    """Upgrade schema."""
    pass


def downgrade():
    op.drop_table('users')
    """Downgrade schema."""
    pass
