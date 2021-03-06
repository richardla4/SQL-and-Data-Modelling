"""empty message

Revision ID: 173460d6cb2c
Revises: 4445d13baa01
Create Date: 2020-07-05 15:53:27.520837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173460d6cb2c'
down_revision = '4445d13baa01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['name'])
    op.create_unique_constraint(None, 'Venue', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###
