"""add publish column to posts table

Revision ID: 5260bafeb06b
Revises: a41cdf2980da
Create Date: 2025-10-19 22:01:53.338188

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5260bafeb06b'
down_revision: Union[str, Sequence[str], None] = 'a41cdf2980da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('publish', sa.Boolean(), nullable=False, server_default="TRUE"))

    """Upgrade schema."""
    pass


def downgrade():
    op.drop_column('posts', "publish")
    """Downgrade schema."""
    pass
