"""Adding foreign key to post table

Revision ID: 6fc0061f4b1f
Revises: 097aa14ae64e
Create Date: 2022-01-09 22:23:54.302279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc0061f4b1f'
down_revision = '097aa14ae64e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                    sa.Column('owner_id',sa.Integer(),nullable=False),
                )
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')

    pass
