"""empty message

Revision ID: 1d1a3ab8d5ca
Revises: 2671c78b7a5c
Create Date: 2023-06-11 00:44:56.731519

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1d1a3ab8d5ca'
down_revision = '2671c78b7a5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('is_mobile_verified', sa.Boolean(), nullable=True),
    sa.Column('is_email_verified', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('todo_notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('note_title', sa.String(length=50), nullable=False),
    sa.Column('note_description', sa.String(length=250), nullable=True),
    sa.Column('status', sa.Enum('upcoming', 'completed', 'due', name='todo_status'), nullable=True),
    sa.Column('priority', sa.Enum('extreme', 'high', 'medium', 'low', name='todo_priority'), nullable=True),
    sa.Column('location', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['todo_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_notes')
    op.drop_table('todo_user')
    # ### end Alembic commands ###