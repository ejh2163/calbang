"""empty message

Revision ID: ce9550d2beec
Revises: None
Create Date: 2016-11-14 03:52:34.024245

"""

# revision identifiers, used by Alembic.
revision = 'ce9550d2beec'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('page', sa.String(length=12), nullable=False),
    sa.Column('viewed', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(length=12), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('kakaotalk', sa.String(length=30), nullable=True),
    sa.Column('city', sa.String(length=24), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('image_ext', sa.String(length=240), nullable=True),
    sa.Column('address', sa.String(length=240), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=False),
    sa.Column('bathrooms', sa.Integer(), nullable=False),
    sa.Column('parking', sa.Integer(), nullable=True),
    sa.Column('utilities', sa.String(length=6), nullable=True),
    sa.Column('internet', sa.String(length=6), nullable=True),
    sa.Column('furniture', sa.String(length=6), nullable=True),
    sa.Column('food', sa.String(length=6), nullable=True),
    sa.Column('sqft', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_joined', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    ### end Alembic commands ###
