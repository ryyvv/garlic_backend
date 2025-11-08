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
   
    
    
    
    op.create_table('garlic_variety',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('variety_name', sa.String(50), nullable=False),
        sa.Column('variety_description', sa.Text(999), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #FK-garlic_variety
    op.create_table('garlic_variety_category_bullet_details',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('variety_category_bullet_details_id', sa.UUID(), sa.ForeignKey('garlic_variety.id'), nullable=False),
        sa.Column('variety_category_bullet_details_name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #FK-garlic_variety_category_bullet_details
    op.create_table('garlic_variety_sub_bullet_details',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('variety_sub_bullet_details_id', sa.UUID(), sa.ForeignKey('garlic_variety_category_bullet_details.id'), nullable=False),
        sa.Column('variety_sub_bullet_details__content', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )

    #only for list of images per Variety docs
    #bucket: garlic-varieties
    #FK-garlic_variety
    op.create_table('garlic_variety_images',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('variety_id', sa.UUID(), sa.ForeignKey('garlic_variety.id'), nullable=False),
        sa.Column('images_name', sa.String(999), nullable=False),
        sa.Column('remarks', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #only for planting Material Location
    op.create_table('plant_location',
        sa.Column('id',  sa.UUID(), primary_key=True, nullable=False),
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
    )
    
    op.create_table('users',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('fullname', sa.String(255), nullable=False),
        sa.Column('birthday', sa.DateTime(), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('gender', sa.String(255), nullable=False),
        sa.Column('plant_location_id', sa.UUID(), sa.ForeignKey('plant_location.id'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('is_superuser', sa.Boolean(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #list of Planting Material
    #FK-garlic_variety
    #FK-plant_location
    #FK-garlic_images_list
    op.create_table('garlic_plant',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_title', sa.String(255), nullable=True),
        sa.Column('variety_id', sa.UUID(), sa.ForeignKey('garlic_variety.id'), nullable=False),
        sa.Column('plant_location_id', sa.UUID(), sa.ForeignKey('plant_location.id'), nullable=False),
        sa.Column('image_name', sa.UUID(), sa.ForeignKey('garlic_images_list.id'), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    #only for garlic images to be identify per planting material
    # This will part of data will be use in accessing/assesment for knowledge and decision based needed
    #bucket: garlic-identification
    #FK-garlic_plant
    op.create_table('garlic_images_list',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('images_name', sa.String(999), nullable=False),
        sa.Column('image_result', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('garlic_images_list_created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('garlic_images_list_updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #post-assesment-description
    #FK-garlic_plant
    op.create_table('garlic_plant_description',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('date_planted', sa.DateTime(), nullable=False),
        sa.Column('date_harvested', sa.DateTime(), nullable=False),
        sa.Column('garlic_plain_text', sa.String(999), nullable=False),
        sa.Column('harvest_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    #post-assesment-yield-tracking based from profit such as grand-total kilogram-harvest, sub-total kilogram-harvest of bulb-size in: [small, medium, large], percentage of bulb-size in: [small, medium, large], and total expenses of garlic planting
    #FK-garlic_plant
    op.create_table('garlic_assesment-yield-tracker',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_plant_task_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        # Yield tracking metrics
        sa.Column('harvest_date', sa.DateTime(), nullable=False),
        sa.Column('grand_total_kg', sa.Float(), nullable=False),
        sa.Column('subtotal_small_kg', sa.Float(), nullable=True),
        sa.Column('subtotal_medium_kg', sa.Float(), nullable=True),
        sa.Column('subtotal_large_kg', sa.Float(), nullable=True),
        sa.Column('percent_small_bulb', sa.Float(), nullable=True),
        sa.Column('percent_medium_bulb', sa.Float(), nullable=True),
        sa.Column('percent_large_bulb', sa.Float(), nullable=True),
        # Financial data
        sa.Column('total_expenses', sa.Numeric(12, 2), nullable=True),
        sa.Column('market_price_per_kg', sa.Numeric(12, 2), nullable=True),
        sa.Column('gross_income', sa.Numeric(12, 2), nullable=True),
        sa.Column('net_profit', sa.Numeric(12, 2), nullable=True),
        sa.Column('profit_margin', sa.Float(), nullable=True),
        # Optional remarks or notes
        sa.Column('farmer_satisfaction_rating', sa.String(50), nullable=True),
        sa.Column('farmer_feedback', sa.String(999), nullable=True),
        sa.Column('remarks', sa.String(50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    
    
    #today-task
    #FK-garlic_plant
    op.create_table('garlic_plant_forecast_today',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_plant_task_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('forecast_task_today_name', sa.String(255), nullable=False),
        sa.Column('forecast_task_today__remarks', sa.String(255), nullable=False),
        sa.Column('forecast_task_today__date', sa.DateTime(), nullable=False),
        sa.Column('forecast_task_today__type', sa.String(50), nullable=False),
        sa.Column('forecast_task_today__status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    #Forecast-task
    #FK-garlic_plant
    op.create_table('garlic_plant_forecast_task',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_plant_task_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('forecast_task_name', sa.String(255), nullable=False),
        sa.Column('forecast_task_remarks', sa.String(255), nullable=False),
        sa.Column('forecast_task_date', sa.DateTime(), nullable=False),
        sa.Column('forecast_task_type', sa.String(50), nullable=False),
        sa.Column('forecast_task_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    #Completed-task
    #FK-garlic_plant
    op.create_table('garlic_plant_completed_task',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('garlic_plant_task_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('completed_task_name', sa.String(255), nullable=False),
        sa.Column('completed_task_remarks', sa.String(255), nullable=False),
        sa.Column('completed_task_date', sa.DateTime(), nullable=False),
        sa.Column('completed_task_type', sa.String(50), nullable=False),
        sa.Column('completed_task_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    
    
    #garlic-weather-realtime forecast logs for ave-temperature: [min, max, and aveg], wind , humidity and precipitation and for another hourly ave-temperature: [min, max, and aveg], wind , humidity and precipitation.
    #FK-garlic_plant
    op.create_table('garlic_weather_forecast-logs',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('weather_forecast_today_log_ave_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_min_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_max_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_humidity', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_wind', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_preipitation', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_sunrise', sa.String(50), nullable=False),
        sa.Column('weather_forecast_today_log_sunset', sa.String(50), nullable=False),
        sa.Column('weather_forecast_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #garlic-weather-realtime hourly forecast logs for ave-temperature: [min, max, and aveg], wind , humidity and precipitation and for another hourly ave-temperature: [min, max, and aveg], wind , humidity and precipitation.
    #FK-garlic_plant
    op.create_table('garlic_weather_forecast-logs-hourly',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('weather_forecast_hourly_log_ave_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_min_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_max_temp', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_humidity', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_wind', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_preipitation', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_sunrise', sa.String(50), nullable=False),
        sa.Column('weather_forecast_hourly_log_sunset', sa.String(50), nullable=False),
        sa.Column('weather_forecast_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #historical
    #garlic-weather-realtime hourly forecast logs for ave-temperature: [min, max, and aveg], wind , humidity and precipitation and for another hourly ave-temperature: [min, max, and aveg], wind , humidity and precipitation.
    #FK-garlic_plant
    op.create_table('garlic_historical_weather_forecast_logs',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('historical_weather_forecast_today_log_ave_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_today_log_min_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_today_log_max_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_today_log_humidity', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_today_log_wind', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_today_log_preipitation', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #FK-garlic_plant
    op.create_table('garlic_historical_weather_forecast-logs-hourly',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_ave_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_min_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_max_temp', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_humidity', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_wind', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_preipitation', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_sunrise', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_hourly_log_sunset', sa.String(50), nullable=False),
        sa.Column('historical_weather_forecast_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #garlic-treatment #garlic-variety #pre-assesment-per-treatment
    #FK-garlic_plant
    #FK-garlic_plant_completed_task
    op.create_table('garlic_treatment',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('treatment_completed_id', sa.UUID(), sa.ForeignKey('garlic_plant_completed_task.id'), nullable=False),
        sa.Column('treatment_assesment', sa.String(999), nullable=False),
        sa.Column('treatment_satisfaction', sa.String(50), nullable=False),
        sa.Column('treatment_date', sa.DateTime(), nullable=False),
        sa.Column('treatment_type', sa.String(), nullable=False),
        sa.Column('treatment_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #new technology/practices applied during the garlic planting
    #FK-garlic_plant
    #FK-garlic_new_technology
    #FK-garlic_plant_completed_task
    op.create_table('garlic_new_technology',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('garlic_technology_treatment_id', sa.UUID(), sa.ForeignKey('garlic_treatment.id'), nullable=False),
        sa.Column('new_technology_treatment_completed_id', sa.UUID(), sa.ForeignKey('garlic_plant_completed_task.id'), nullable=False),
        sa.Column('new_technology_treatment_assesment', sa.String(999), nullable=False),
        sa.Column('new_technology_treatment_satisfaction', sa.String(50), nullable=False),
        sa.Column('new_technology_treatment_date', sa.DateTime(), nullable=False),
        sa.Column('new_technology_treatment_type', sa.String(255), nullable=False),
        sa.Column('new_technology_treatment_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    #FK-garlic_plant
    #FK-garlic_new_technology
    op.create_table('garlic_new_technology_images',
        sa.Column('id', sa.UUID(), primary_key=True, nullable=False),
        sa.Column('garlic_plant_id', sa.UUID(), sa.ForeignKey('garlic_plant.id'), nullable=False),
        sa.Column('new_technology_treatment_images_id', sa.UUID(), sa.ForeignKey('garlic_new_technology.id'), nullable=False),
        sa.Column('new_technology_treatment_images_front', sa.String(999), nullable=False),
        sa.Column('new_technology_treatment_images_back', sa.String(999), nullable=False),
        sa.Column('new_technology_treatment_images_satisfaction', sa.String(255), nullable=False),
        sa.Column('new_technology_treatment_images_date', sa.DateTime(), nullable=False),
        sa.Column('new_technology_treatment_images_type', sa.String(255), nullable=False),
        sa.Column('new_technology_treatment_images_status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )
    
    

def downgrade() -> None:
    # Drop tables in reverse order of upgrade() creation
    op.drop_table('garlic_new_technology_images')
    op.drop_table('garlic_new_technology')
    op.drop_table('garlic_treatment')
    op.drop_table('garlic_historical_weather_forecast-logs-hourly')
    op.drop_table('garlic_historical_weather_forecast_logs')
    op.drop_table('garlic_weather_forecast-logs-hourly')
    op.drop_table('garlic_weather_forecast-logs')
    op.drop_table('garlic_plant_completed_task')
    op.drop_table('garlic_plant_forecast_task')
    op.drop_table('garlic_plant_forecast_today')
    op.drop_table('garlic_assesment-yield-tracker')
    op.drop_table('garlic_plant_description')
    op.drop_table('garlic_images_list')
    op.drop_table('garlic_plant')
    op.drop_table('users')
    op.drop_table('plant_location')
    op.drop_table('garlic_variety_images')
    op.drop_table('garlic_variety_sub_bullet_details')
    op.drop_table('garlic_variety_category_bullet_details')
    op.drop_table('garlic_variety')
    
    
    