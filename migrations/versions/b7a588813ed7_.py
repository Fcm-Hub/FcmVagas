"""empty message

Revision ID: b7a588813ed7
Revises: 
Create Date: 2020-01-23 11:47:26.493019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7a588813ed7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token')
    op.drop_column('user', 'security_code')
    op.drop_column('user', 'last_token')
    op.drop_column('user', 'passwordchangerequest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passwordchangerequest', sa.BOOLEAN(), nullable=True))
    op.add_column('user', sa.Column('last_token', sa.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('security_code', sa.VARCHAR(length=255), nullable=True))
    op.add_column('user', sa.Column('token', sa.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
