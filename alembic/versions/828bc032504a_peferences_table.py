"""peferences table

Revision ID: 828bc032504a
Revises: 1bf55ebc9ed2
Create Date: 2023-09-14 14:49:25.306852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '828bc032504a'
down_revision = '1bf55ebc9ed2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("peferences",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("choice", sa.String, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False), 
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))
    )
    pass


def downgrade() -> None:
    op.drop_table("peferences")
    pass
