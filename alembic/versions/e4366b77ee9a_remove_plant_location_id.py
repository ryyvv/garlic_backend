"""remove plant_location_id

Revision ID: e4366b77ee9a
Revises: 4be14207277e
Create Date: 2025-11-15 13:02:56.398146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = 'e4366b77ee9a'
down_revision = '4be14207277e'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute('DROP TABLE IF EXISTS users CASCADE')
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('firebase_uid', sa.String(128), nullable=True, unique=True),
        sa.Column('fullname', sa.String(255), nullable=False),
        sa.Column('birthday', sa.DateTime(), nullable=False),
        sa.Column('email', sa.String(255), nullable=False), 
        sa.Column('gender', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

