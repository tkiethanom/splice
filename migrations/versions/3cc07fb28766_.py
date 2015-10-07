"""empty message

Revision ID: 3cc07fb28766
Revises: 16fa35dd63a2
Create Date: 2015-09-22 14:39:21.811450

"""

# revision identifiers, used by Alembic.
revision = '3cc07fb28766'
down_revision = '16fa35dd63a2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('UQ_ACCOUNT_NAME', 'accounts', ['name'])
    op.alter_column('campaigns', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint('UQ_CAMPAIGN_ACCOUNT_ID_NAME', 'campaigns', ['account_id', 'name'])
    op.add_column('adgroups', sa.Column('paused', sa.Boolean(), server_default=sa.text(u'false'), nullable=False))
    op.add_column('adgroups', sa.Column('type', sa.String(length=16), nullable=True))
    op.drop_column('adgroups', 'start_date')
    op.drop_column('adgroups', 'end_date_dt')
    op.drop_column('adgroups', 'end_date')
    op.drop_column('adgroups', 'start_date_dt')
    op.drop_column('campaigns', 'locale')
    op.add_column('tiles', sa.Column('paused', sa.Boolean(), server_default=sa.text(u'false'), nullable=False))
    op.add_column('tiles', sa.Column('status', sa.String(length=16), server_default=u'unapproved', nullable=False))
    op.drop_column('tiles', 'locale')
    ### end Alembic commands ###


def downgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('UQ_ACCOUNT_NAME', 'accounts', type_='unique')
    op.alter_column('campaigns', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('UQ_CAMPAIGN_ACCOUNT_ID_NAME', 'campaigns', type_='unique')
    op.add_column('tiles', sa.Column('locale', sa.VARCHAR(length=14), autoincrement=False, nullable=True))
    op.drop_column('tiles', 'status')
    op.drop_column('tiles', 'paused')
    op.add_column('campaigns', sa.Column('locale', sa.VARCHAR(length=14), autoincrement=False, nullable=True))
    op.add_column('adgroups', sa.Column('start_date_dt', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('adgroups', sa.Column('end_date', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column('adgroups', sa.Column('end_date_dt', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('adgroups', sa.Column('start_date', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.drop_column('adgroups', 'type')
    op.drop_column('adgroups', 'paused')
    ### end Alembic commands ###


def upgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

