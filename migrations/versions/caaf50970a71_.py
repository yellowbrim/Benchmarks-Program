"""empty message

Revision ID: caaf50970a71
Revises: 1b07a280dd91
Create Date: 2018-02-19 15:08:12.411910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caaf50970a71'
down_revision = '1b07a280dd91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_email', sa.String(length=64), nullable=True),
    sa.Column('list_id', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('app_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_app_user_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_app_user_user_email'), ['user_email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_app_user_user_email'))
        batch_op.drop_index(batch_op.f('ix_app_user_timestamp'))

    op.drop_table('app_user')
    # ### end Alembic commands ###
