"""added reviews table

Revision ID: 147cf7ff8ecd
Revises: 4097a9b9fb41
Create Date: 2020-04-15 14:58:53.670013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '147cf7ff8ecd'
down_revision = '4097a9b9fb41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('star_rating', sa.String(length=10), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('reviewer', sa.Integer(), nullable=True),
    sa.Column('reviewed_restaurant', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reviewed_restaurant'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['reviewer'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
