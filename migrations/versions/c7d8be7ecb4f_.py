"""empty message

Revision ID: c7d8be7ecb4f
Revises: 084d780f214c
Create Date: 2022-01-04 15:19:35.613146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c7d8be7ecb4f"
down_revision = "084d780f214c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("questions", sa.Text(), nullable=False),
        sa.Column("answers", sa.Text(), nullable=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("started_on", sa.DateTime(), nullable=True),
        sa.Column("ended_on", sa.DateTime(), nullable=True),
        sa.Column("refund_window", sa.DateTime(), nullable=True),
        sa.Column("current_question", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("events")
    # ### end Alembic commands ###
