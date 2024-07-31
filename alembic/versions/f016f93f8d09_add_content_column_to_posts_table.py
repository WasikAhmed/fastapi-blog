"""add content column to posts table

Revision ID: f016f93f8d09
Revises: 2f4181d1aaea
Create Date: 2024-07-31 17:23:28.186998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f016f93f8d09'
down_revision: Union[str, None] = '2f4181d1aaea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
