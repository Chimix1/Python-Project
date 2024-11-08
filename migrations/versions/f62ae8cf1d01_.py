"""empty message

Revision ID: f62ae8cf1d01
Revises: d3e3264f6cb6
Create Date: 2024-10-28 13:36:06.910660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f62ae8cf1d01'
down_revision = 'd3e3264f6cb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('permissions', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_roles_default'), ['default'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_default'))
        batch_op.drop_column('permissions')
        batch_op.drop_column('default')

    # ### end Alembic commands ###
