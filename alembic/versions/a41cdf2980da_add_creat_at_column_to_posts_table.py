"""add creat_at column to posts table

Revision ID: a41cdf2980da
Revises: 44070aad5ed5
Create Date: 2025-10-19 21:54:46.806099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a41cdf2980da'
down_revision: Union[str, Sequence[str], None] = '44070aad5ed5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    """Upgrade schema."""
    pass


def downgrade():
    op.drop_column('posts', 'create_at')
    """Downgrade schema."""
    pass
