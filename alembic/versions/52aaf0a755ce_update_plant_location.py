"""update plant_location

Revision ID: 52aaf0a755ce
Revises: e4366b77ee9a
Create Date: 2025-11-15 13:09:22.147392

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = '52aaf0a755ce'
down_revision = 'e4366b77ee9a'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute('DROP TABLE IF EXISTS plant_location CASCADE')
    
    op.create_table('plant_location',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('region', sa.String(255), nullable=True),
        sa.Column('region_code', sa.String(255), nullable=True),
        sa.Column('province', sa.String(255), nullable=True),
        sa.Column('province_code', sa.String(255), nullable=True),
        sa.Column('city', sa.String(255), nullable=True),
        sa.Column('city_code', sa.String(255), nullable=True),
        sa.Column('barangay', sa.String(255), nullable=True),
        sa.Column('barangay_code', sa.String(255), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    pass