"""empty message

Revision ID: 5ab3e316e149
Revises: 
Create Date: 2021-04-28 09:01:21.165637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ab3e316e149'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Movie', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Movie', 'description')
    # ### end Alembic commands ###
