"""update plant_locations

Revision ID: efffb4ae9d2f
Revises: 52aaf0a755ce
Create Date: 2025-11-15 17:55:56.518450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'efffb4ae9d2f'
down_revision = '52aaf0a755ce'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute('DROP TABLE IF EXISTS plant_location CASCADE')
    
    op.create_table('plant_location',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('region', sa.String(255), nullable=True),
        sa.Column('province', sa.String(255), nullable=True),
        sa.Column('city', sa.String(255), nullable=True),
        sa.Column('barangay', sa.String(255), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

 