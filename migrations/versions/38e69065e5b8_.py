"""empty message

Revision ID: 38e69065e5b8
Revises: 5a08d54f0d17
Create Date: 2014-08-17 16:36:05.828664

"""

# revision identifiers, used by Alembic.
revision = '38e69065e5b8'
down_revision = '5a08d54f0d17'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_image', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_image')
    ### end Alembic commands ###
