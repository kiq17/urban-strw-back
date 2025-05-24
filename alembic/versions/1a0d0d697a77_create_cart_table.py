"""create cart table

Revision ID: 1a0d0d697a77
Revises: 5b1162ee028a
Create Date: 2024-06-02 12:34:41.356737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a0d0d697a77'
down_revision = '5b1162ee028a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("cart",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))               
    )
    pass


def downgrade() -> None:
    op.drop_table("cart")
    pass
