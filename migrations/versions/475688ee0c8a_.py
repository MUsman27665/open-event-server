"""empty message

Revision ID: 475688ee0c8a
Revises: 7017afcbe5b2
Create Date: 2016-07-06 20:14:58.548159

"""

# revision identifiers, used by Alembic.
revision = '475688ee0c8a'
down_revision = '7017afcbe5b2'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('tw_consumer_key', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('tw_consumer_secret', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'tw_consumer_secret')
    op.drop_column('settings', 'tw_consumer_key')
    ### end Alembic commands ###