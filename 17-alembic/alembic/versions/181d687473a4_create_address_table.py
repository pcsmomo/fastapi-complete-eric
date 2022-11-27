"""Create address table

Revision ID: 181d687473a4
Revises: 9b73fc7d3375
Create Date: 2022-11-27 12:46:55.212073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '181d687473a4'
down_revision = '9b73fc7d3375'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
