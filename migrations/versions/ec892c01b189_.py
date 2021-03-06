"""empty message

Revision ID: ec892c01b189
Revises: e42d72d3c94f
Create Date: 2018-03-05 15:40:33.668848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec892c01b189'
down_revision = 'e42d72d3c94f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('list_stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('list_stats', schema=None) as batch_op:
        batch_op.drop_column('count')

    # ### end Alembic commands ###
