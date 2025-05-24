"""create table otp

Revision ID: 0f9a7741dd01
Revises: 828bc032504a
Create Date: 2023-12-26 16:03:53.417693

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '0f9a7741dd01'
down_revision = '828bc032504a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("otps",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("code",sa.String, nullable=False),
        sa.Column("temp_link",sa.String, nullable=False),
        sa.Column("user_id",sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at",sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"))
    )
    pass


def downgrade() -> None:
    op.drop_table("otps")
    pass
