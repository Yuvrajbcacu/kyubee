"""Modify nullable constraint

Revision ID: 44aa05fd3f92
Revises: 
Create Date: 2024-01-21 01:36:41.080391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44aa05fd3f92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_login', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cookie', sa.String(length=90), nullable=False))
        batch_op.drop_column('COOKIE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_login', schema=None) as batch_op:
        batch_op.add_column(sa.Column('COOKIE', sa.VARCHAR(length=90), nullable=False))
        batch_op.drop_column('cookie')

    # ### end Alembic commands ###
