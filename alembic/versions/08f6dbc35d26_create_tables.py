"""Create Tables

Revision ID: 08f6dbc35d26
Revises: 
Create Date: 2022-01-09 21:55:54.308844

"""
from alembic import op
import sqlalchemy as sa
# from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '08f6dbc35d26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                            sa.Column('title',sa.String(),nullable=False))
    pass



def downgrade():
    op.drop_table('posts')
    pass