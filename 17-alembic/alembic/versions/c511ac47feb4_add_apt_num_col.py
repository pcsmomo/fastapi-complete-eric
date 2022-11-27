"""add apt num col

Revision ID: c511ac47feb4
Revises: 4f808f0d858c
Create Date: 2022-11-27 13:44:54.714765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c511ac47feb4'
down_revision = '4f808f0d858c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
