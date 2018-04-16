"""empty message

Revision ID: 196e194ddf5b
Revises: 71527ea3e8a0
Create Date: 2018-04-16 15:55:39.626672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196e194ddf5b'
down_revision = '71527ea3e8a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tap', sa.Column('people', sa.String(), nullable=True))
    op.drop_column('tap', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tap', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('tap', 'people')
    # ### end Alembic commands ###