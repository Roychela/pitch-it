"""Fifth Migration

Revision ID: de9cdf29a406
Revises: b4b4a1f632fb
Create Date: 2019-07-01 07:38:31.615927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de9cdf29a406'
down_revision = 'b4b4a1f632fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_pitch_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_fkey', 'comments', 'users', ['pitch'], ['id'])
    # ### end Alembic commands ###
