"""empty message

Revision ID: d0499f91a945
Revises: ba56f2c7298e
Create Date: 2020-11-11 14:23:56.917839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0499f91a945'
down_revision = 'ba56f2c7298e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
