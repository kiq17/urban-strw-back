"""add slug column

Revision ID: 075a1702f6f2
Revises: 507a6a4415e9
Create Date: 2023-08-06 20:11:21.449511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '075a1702f6f2'
down_revision = '507a6a4415e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("products",
        sa.Column("slug", sa.String)    
    )
    pass


def downgrade() -> None:
    op.drop_column("products", "slug")
    pass
