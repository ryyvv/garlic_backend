"""added garlic plant _id

Revision ID: aab4d9977b5f
Revises: 1b4ea51c5576
Create Date: 2025-11-16 01:08:23.738457

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'aab4d9977b5f'
down_revision = '1b4ea51c5576'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute('DROP TABLE IF EXISTS garlic_images_list CASCADE')
    
    op.create_table('garlic_images_list',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('garlic_plant_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('images_name', sa.String(255), nullable=False),
        sa.Column('images_bucket', sa.String(255), nullable=False),
        sa.Column('images_url', sa.String(999), nullable=False),
        sa.Column('image_result', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['garlic_plant_id'], ['garlic_plant.id']),
        sa.PrimaryKeyConstraint('id')
    )

 
 