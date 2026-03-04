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
    modified_at = Column(DateTime)
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
    total_distance = Column(Float)
    sprints = Column(Integer)
    sprint_distance = Column(Float)
    hsr_distance = Column(Float)
    accelerations = Column(Integer)
    decelerations = Column(Integer)
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
    total_distance = Column(Float)
    sprints = Column(Integer)
    sprint_distance = Column(Float)
    hsr_distance = Column(Float)
    accelerations = Column(Integer)
    decelerations = Column(Integer)
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
