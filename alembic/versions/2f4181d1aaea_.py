"""empty message

Revision ID: 2f4181d1aaea
Revises: 0217283d9cd0
Create Date: 2024-07-31 17:20:07.044914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f4181d1aaea'
down_revision: Union[str, None] = '0217283d9cd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
