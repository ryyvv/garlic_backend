"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2024-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create base tables first (no foreign keys)
    op.create_table('garlic_variety',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_name', sa.String(50), nullable=False),
        sa.Column('variety_description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('plant_location',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('reg_name', sa.String(255), nullable=False),
        sa.Column('reg_code', sa.String(255), nullable=False),
        sa.Column('prov_name', sa.String(255), nullable=False),
        sa.Column('prov_code', sa.String(255), nullable=False),
        sa.Column('mun_name', sa.String(255), nullable=False),
        sa.Column('mun_code', sa.String(255), nullable=False),
        sa.Column('brgy_name', sa.String(255), nullable=False),
        sa.Column('brgy_code', sa.String(255), nullable=False),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('long', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
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

    # Create garlic_images_list first (referenced by garlic_plant)
    op.create_table('garlic_images_list',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('images_name', sa.String(999), nullable=False),
        sa.Column('image_result', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('garlic_images_list_created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('garlic_images_list_updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create garlic_plant (references garlic_variety, plant_location, garlic_images_list)
    op.create_table('garlic_plant',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', sa.UUID(255), nullable=True),
        sa.Column('garlic_title', sa.String(255), nullable=True),
        sa.Column('variety_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('plant_location_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['variety_id'], ['garlic_variety.id']),
        sa.ForeignKeyConstraint(['plant_location_id'], ['plant_location.id']),
        sa.ForeignKeyConstraint(['image_name'], ['garlic_images_list.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Update garlic_images_list to reference garlic_plant
    op.add_column('garlic_images_list', sa.Column('garlic_plant_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key('fk_garlic_images_list_plant', 'garlic_images_list', 'garlic_plant', ['garlic_plant_id'], ['id'])

    # Create remaining tables with foreign keys
    op.create_table('garlic_variety_category_bullet_details',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_category_bullet_details_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_category_bullet_details_name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['variety_category_bullet_details_id'], ['garlic_variety.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('garlic_variety_sub_bullet_details',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_sub_bullet_details_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_sub_bullet_details__content', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['variety_sub_bullet_details_id'], ['garlic_variety_category_bullet_details.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('garlic_variety_images',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variety_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('images_name', sa.String(999), nullable=False),
        sa.Column('remarks', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['variety_id'], ['garlic_variety.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('garlic_variety_images')
    op.drop_table('garlic_variety_sub_bullet_details')
    op.drop_table('garlic_variety_category_bullet_details')
    op.drop_constraint('fk_garlic_images_list_plant', 'garlic_images_list', type_='foreignkey')
    op.drop_column('garlic_images_list', 'garlic_plant_id')
    op.drop_table('garlic_plant')
    op.drop_table('garlic_images_list')
    op.drop_table('users')
    op.drop_table('plant_location')
    op.drop_table('garlic_variety')