"""add_column_visits

Revision ID: 5b1162ee028a
Revises: 0f9a7741dd01
Create Date: 2024-05-05 14:19:40.444876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1162ee028a'
down_revision = '0f9a7741dd01'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("products",
        sa.Column("visitas", sa.Integer, server_default="0")    
    )
    pass


def downgrade() -> None:
    op.drop_column("products", "visitas")
    pass
