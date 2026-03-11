from sqlalchemy import (
    ARRAY,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from shared.models import Base


class CatapultTeam(Base):
    __tablename__ = "catapult_teams"

    id = Column(Integer, primary_key=True, index=True)
    catapult_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    slug = Column(String)
    sport_name = Column(String)
    primary_colour = Column(String)
    secondary_colour = Column(String)
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    athletes = relationship("CatapultAthlete", back_populates="team")


class CatapultAthlete(Base):
    __tablename__ = "catapult_athletes"

    id = Column(Integer, primary_key=True, index=True)
    catapult_id = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String)
    jersey = Column(String)
    height = Column(Integer)
    weight = Column(Integer)
    date_of_birth = Column(Date)
    position = Column(String)
    team_id = Column(Integer, ForeignKey("catapult_teams.id"))
    velocity_max = Column(Float)
    heart_rate_max = Column(Integer)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    team = relationship("CatapultTeam", back_populates="athletes")


class CatapultActivity(Base):
    __tablename__ = "catapult_activities"

    id = Column(Integer, primary_key=True, index=True)
    catapult_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    owner_id = Column(String)
    athlete_count = Column(Integer)
    period_count = Column(Integer)
    tags = Column(ARRAY(String))
    day_code = Column(String, nullable=True)
    activity_type = Column(String, nullable=True)
    modified_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    periods = relationship("CatapultPeriod", back_populates="activity")


class CatapultPeriod(Base):
    __tablename__ = "catapult_periods"

    id = Column(Integer, primary_key=True, index=True)
    catapult_id = Column(String, unique=True, index=True, nullable=False)
    activity_id = Column(Integer, ForeignKey("catapult_activities.id"), nullable=False)
    name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    tags = Column(ARRAY(String))
    is_injected = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    activity = relationship("CatapultActivity", back_populates="periods")


class CatapultParameter(Base):
    __tablename__ = "catapult_parameters"

    id = Column(Integer, primary_key=True, index=True)
    catapult_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    base_name = Column(String)
    slug = Column(String, unique=True, index=True, nullable=False)
    band = Column(Integer)
    aggregation = Column(String)
    group_by = Column(String)
    unit_type = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )


class CatapultWorkload(Base):
    __tablename__ = "catapult_workload"
    __table_args__ = (UniqueConstraint("athlete_id", "activity_id", "period_id"),)

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(
        Integer, ForeignKey("catapult_athletes.id"), nullable=False, index=True
    )
    activity_id = Column(
        Integer, ForeignKey("catapult_activities.id"), nullable=False, index=True
    )
    period_id = Column(Integer, ForeignKey("catapult_periods.id"), index=True)
    # General
    total_duration = Column(Float)
    total_distance = Column(Float)
    max_velocity = Column(Float)
    # Velocity band distance
    vb1_distance = Column(Float)
    vb2_distance = Column(Float)
    vb3_distance = Column(Float)
    vb4_distance = Column(Float)
    vb5_distance = Column(Float)
    vb6_distance = Column(Float)
    vb7_distance = Column(Float)
    vb8_distance = Column(Float)
    # Velocity band effort count
    vb1_efforts = Column(Float)
    vb2_efforts = Column(Float)
    vb3_efforts = Column(Float)
    vb4_efforts = Column(Float)
    vb5_efforts = Column(Float)
    vb6_efforts = Column(Float)
    vb7_efforts = Column(Float)
    vb8_efforts = Column(Float)
    # Acceleration bands
    accel_low_distance = Column(Float)
    accel_low_efforts = Column(Float)
    accel_med_distance = Column(Float)
    accel_med_efforts = Column(Float)
    accel_high_distance = Column(Float)
    accel_high_efforts = Column(Float)
    # Deceleration bands
    decel_low_distance = Column(Float)
    decel_low_efforts = Column(Float)
    decel_med_distance = Column(Float)
    decel_med_efforts = Column(Float)
    decel_high_distance = Column(Float)
    decel_high_efforts = Column(Float)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )


class CatapultSessionWorkload(Base):
    __tablename__ = "catapult_session_workload"
    __table_args__ = (UniqueConstraint("athlete_id", "activity_id"),)

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(
        Integer, ForeignKey("catapult_athletes.id"), nullable=False, index=True
    )
    activity_id = Column(
        Integer, ForeignKey("catapult_activities.id"), nullable=False, index=True
    )
    activity_name = Column(String, nullable=False)
    activity_start_time = Column(DateTime, nullable=False)
    activity_end_time = Column(DateTime, nullable=False)
    activity_tags = Column(ARRAY(String))
    athlete_first_name = Column(String, nullable=False)
    athlete_last_name = Column(String, nullable=False)
    athlete_jersey = Column(String)
    athlete_position = Column(String)
    # General
    total_duration = Column(Float)
    total_distance = Column(Float)
    max_velocity = Column(Float)
    distance_per_min = Column(Float)
    # Velocity band distance
    vb1_distance = Column(Float)
    vb2_distance = Column(Float)
    vb3_distance = Column(Float)
    vb4_distance = Column(Float)
    vb5_distance = Column(Float)
    vb6_distance = Column(Float)
    vb7_distance = Column(Float)
    vb8_distance = Column(Float)
    # Velocity band effort count
    vb1_efforts = Column(Float)
    vb2_efforts = Column(Float)
    vb3_efforts = Column(Float)
    vb4_efforts = Column(Float)
    vb5_efforts = Column(Float)
    vb6_efforts = Column(Float)
    vb7_efforts = Column(Float)
    vb8_efforts = Column(Float)
    # Acceleration bands
    accel_low_distance = Column(Float)
    accel_low_efforts = Column(Float)
    accel_med_distance = Column(Float)
    accel_med_efforts = Column(Float)
    accel_high_distance = Column(Float)
    accel_high_efforts = Column(Float)
    # Deceleration bands
    decel_low_distance = Column(Float)
    decel_low_efforts = Column(Float)
    decel_med_distance = Column(Float)
    decel_med_efforts = Column(Float)
    decel_high_distance = Column(Float)
    decel_high_efforts = Column(Float)
    # Velocity groups
    low_velocity_distance = Column(Float)
    med_velocity_distance = Column(Float)
    high_velocity_distance = Column(Float)
    sprint_distance = Column(Float)
    # Derived metrics
    high_speed_ratio = Column(Float)
    mechanical_density = Column(Float)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )


class CatapultChronicWorkload(Base):
    __tablename__ = "catapult_chronic_workload"
    __table_args__ = (UniqueConstraint("athlete_id", "date", "parameter"),)

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(
        Integer, ForeignKey("catapult_athletes.id"), nullable=False, index=True
    )
    date = Column(Date, nullable=False, index=True)
    parameter = Column(String, nullable=False)
    daily_value = Column(Float)
    acute_value = Column(Float)
    chronic_value = Column(Float)
    acwr = Column(Float)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
