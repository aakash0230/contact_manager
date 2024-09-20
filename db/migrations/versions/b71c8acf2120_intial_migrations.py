"""intial migrations

Revision ID: b71c8acf2120
Revises: 
Create Date: 2024-09-21 00:10:24.717443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b71c8acf2120'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone_spam_mapping',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone_no', sa.String(length=50), nullable=True),
    sa.Column('_password', sa.String(length=200), nullable=True),
    sa.Column('otp', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_phone_mapping',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('phone_no', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_session',
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('session_key', sa.String(length=50), nullable=True),
    sa.Column('is_logged_out', sa.Boolean(), nullable=False),
    sa.Column('logout_time', sa.DateTime(), nullable=True),
    sa.Column('login_time', sa.DateTime(), nullable=True),
    sa.Column('access_token', sa.String(length=4000), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_session')
    op.drop_table('user_phone_mapping')
    op.drop_table('user')
    op.drop_table('phone_spam_mapping')
    # ### end Alembic commands ###
