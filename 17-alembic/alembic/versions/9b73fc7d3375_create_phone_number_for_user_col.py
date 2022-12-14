"""create phone number for user col

Revision ID: 9b73fc7d3375
Revises:
Create Date: 2022-11-27 10:22:49.232107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b73fc7d3375'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
