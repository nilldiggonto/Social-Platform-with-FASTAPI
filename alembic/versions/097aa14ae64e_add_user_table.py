"""add user table

Revision ID: 097aa14ae64e
Revises: 38c5357496bc
Create Date: 2022-01-09 22:17:04.427505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import UniqueConstraint


# revision identifiers, used by Alembic.
revision = '097aa14ae64e'
down_revision = '38c5357496bc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                        sa.Column('id',sa.Integer(),nullable=False),
                        sa.Column('email',sa.String(),nullable=False),
                        sa.Column('password',sa.String(),nullable=False),
                        sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                        sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
