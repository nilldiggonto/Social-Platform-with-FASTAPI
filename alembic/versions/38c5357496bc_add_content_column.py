"""add content column

Revision ID: 38c5357496bc
Revises: 08f6dbc35d26
Create Date: 2022-01-09 22:10:44.116839

"""
from alembic import op
import sqlalchemy as sa
# from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '38c5357496bc'
down_revision = '08f6dbc35d26'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
