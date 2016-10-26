"""empty message

Revision ID: 913e02ad49f5
Revises: f437d4a6a635
Create Date: 2016-10-24 06:05:29.404167

"""

# revision identifiers, used by Alembic.
revision = '913e02ad49f5'
down_revision = 'f437d4a6a635'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('year', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'year')
    ### end Alembic commands ###