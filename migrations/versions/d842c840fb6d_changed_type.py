"""changed type

Revision ID: d842c840fb6d
Revises: fc652107441a
Create Date: 2018-10-27 23:05:20.311437

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd842c840fb6d'
down_revision = 'fc652107441a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('product', 'price',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('sale', 'payment',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sale', 'payment',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    op.alter_column('product', 'price',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    op.alter_column('product', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###