"""add image_url to garlic_images

Revision ID: 1b4ea51c5576
Revises: efffb4ae9d2f
Create Date: 2025-11-16 00:39:21.391044

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = '1b4ea51c5576'
down_revision = 'efffb4ae9d2f'
branch_labels = None
depends_on = None

def upgrade() -> None:
     op.execute('DROP TABLE IF EXISTS garlic_images_list CASCADE')
    
     op.create_table('garlic_images_list',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('images_name', sa.String(255), nullable=False),
        sa.Column('images_bucket', sa.String(255), nullable=False),
        sa.Column('images_url', sa.String(999), nullable=False),
        sa.Column('image_result', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

 