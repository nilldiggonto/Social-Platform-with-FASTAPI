"""Adding Optional Columns

Revision ID: 4a0eda4d11d1
Revises: 6fc0061f4b1f
Create Date: 2022-01-09 22:28:44.634744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a0eda4d11d1'
down_revision = '6fc0061f4b1f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                    sa.Column('publish',sa.Boolean(),nullable=False,server_default='True')
                )
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts','publish')
    op.drop_column('posts','created_at')
    pass
