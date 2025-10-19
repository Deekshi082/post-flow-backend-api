"""add foreign-key to posts table

Revision ID: 44070aad5ed5
Revises: 5e6831305f97
Create Date: 2025-10-19 21:42:28.073049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44070aad5ed5'
down_revision: Union[str, Sequence[str], None] = '5e6831305f97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    """Upgrade schema."""
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    """Downgrade schema."""
    pass
