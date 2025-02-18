"""login_password nullable True

Revision ID: 5e962e6ec768
Revises: 0e8247fe359c
Create Date: 2025-01-28 15:14:35.080162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '5e962e6ec768'
down_revision: Union[str, None] = '0e8247fe359c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_pwd',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_pwd',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###
