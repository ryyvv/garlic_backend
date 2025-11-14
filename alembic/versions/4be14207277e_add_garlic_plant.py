"""add garlic_plant

Revision ID: 4be14207277e
Revises: 7c0195ff4d79
Create Date: 2025-11-14 23:07:42.338541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '4be14207277e'
down_revision = '7c0195ff4d79'
branch_labels = None
depends_on = None

def upgrade() -> None:
    
    op.execute('DROP TABLE IF EXISTS users CASCADE')
    op.execute('DROP TABLE IF EXISTS garlic_plant CASCADE')
    
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('firebase_uid', sa.String(128), nullable=True, unique=True),
        sa.Column('fullname', sa.String(255), nullable=False),
        sa.Column('birthday', sa.DateTime(), nullable=False),
        sa.Column('email', sa.String(255), nullable=False), 
        sa.Column('gender', sa.String(255), nullable=False),
        sa.Column('plant_location_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['plant_location_id'], ['plant_location.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garlic_plant',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', sa.UUID(255), nullable=True),
        sa.Column('garlic_title', sa.String(255), nullable=True),
        sa.Column('variety_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('plant_location_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('date_setup', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.Column('date_planted', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['variety_id'], ['garlic_variety.id']),
        sa.ForeignKeyConstraint(['plant_location_id'], ['plant_location.id']),
        sa.PrimaryKeyConstraint('id')
    )
    