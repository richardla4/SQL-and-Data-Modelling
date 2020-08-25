"""empty message

Revision ID: d733b85596e0
Revises: 173460d6cb2c
Create Date: 2020-07-05 21:21:51.563263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd733b85596e0'
down_revision = '173460d6cb2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.drop_constraint('Artist_name_key', 'Artist', type_='unique')
    op.alter_column('Venue', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.drop_constraint('Venue_name_key', 'Venue', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Venue_name_key', 'Venue', ['name'])
    op.alter_column('Venue', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    op.create_unique_constraint('Artist_name_key', 'Artist', ['name'])
    op.alter_column('Artist', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    # ### end Alembic commands ###