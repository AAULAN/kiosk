"""'initial'

Revision ID: 71ea4abdf655
Revises: 
Create Date: 2018-10-27 18:04:37.069060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71ea4abdf655'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('payment', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('product')
    # ### end Alembic commands ###
