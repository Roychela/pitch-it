"""Fourth Migration

Revision ID: b4b4a1f632fb
Revises: 28fe85a5334d
Create Date: 2019-07-01 07:34:33.625194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4b4a1f632fb'
down_revision = '28fe85a5334d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['pitch'], ['id'])
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch')
    # ### end Alembic commands ###
