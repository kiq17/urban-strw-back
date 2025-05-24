"""create product details

Revision ID: 1bf55ebc9ed2
Revises: 075a1702f6f2
Create Date: 2023-08-07 14:43:11.462581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bf55ebc9ed2'
down_revision = '075a1702f6f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("products_details",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("modelo",sa.String, nullable=False),
        sa.Column("composicao",sa.String, nullable=False),
        sa.Column("info",sa.String, nullable=False),
        sa.Column("fabricacao",sa.String, nullable=False),
        sa.Column("product_id",sa.Integer, sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))
    )
    pass


def downgrade() -> None:
    op.drop_table("products_details")
    pass
