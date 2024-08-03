"""second migration

Revision ID: 2efdfcc31cd2
Revises: f5063a57e564
Create Date: 2024-07-31 20:31:50.399452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2efdfcc31cd2'
down_revision = 'f5063a57e564'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('capacity', sa.String(length=50), nullable=False),
    sa.Column('amenities', sa.String(length=255), nullable=False),
    sa.Column('ratecard', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spaces')
    # ### end Alembic commands ###
