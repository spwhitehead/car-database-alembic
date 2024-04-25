"""Initial migration

Revision ID: 582c4bc1af5e
Revises: 
Create Date: 2024-04-25 10:59:58.435134

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '582c4bc1af5e'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("cars",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("vin", sa.Text, nullable=False),
                    sa.Column("model", sa.Text),
                    sa.Column("make", sa.Text),
                    sa.Column("engine", sa.Text),
                    sa.Column("year", sa.Integer))

    op.create_table("dealerships",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.Text),
                    sa.Column("address", sa.Text),
                    sa.Column("phone_number", sa.Text))

    op.create_table("inventory",
                    sa.Column("car_id", sa.Integer, sa.ForeignKey("cars.id"), primary_key=True),
                    sa.Column("dealer_id", sa.Integer, sa.ForeignKey("dealerships.id"), primary_key=True),
                    sa.Column("cost", sa.Float),
                    sa.Column("is_sold", sa.Boolean))

def downgrade() -> None:
    op.drop_table("cars")
    op.drop_table("dealerships")
    op.drop_table("inventory")