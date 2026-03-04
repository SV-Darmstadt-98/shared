from datetime import datetime

from pydantic import BaseModel


class AthleteRead(BaseModel):
    id: int
    catapult_id: str
    first_name: str
    last_name: str
    jersey: str | None
    position: str | None

    model_config = {"from_attributes": True}


class ActivityRead(BaseModel):
    id: int
    catapult_id: str
    name: str
    start_time: datetime
    end_time: datetime
    tags: list[str] | None

    model_config = {"from_attributes": True}


class SessionWorkloadRead(BaseModel):
    id: int
    athlete_id: int
    activity_id: int
    activity_name: str
    activity_start_time: datetime
    activity_end_time: datetime
    activity_tags: list[str] | None
    athlete_first_name: str
    athlete_last_name: str
    athlete_jersey: str | None
    athlete_position: str | None
    # General
    total_duration: float | None
    total_distance: float | None
    average_velocity: float | None
    max_velocity: float | None
    total_player_load: float | None
    # Velocity band distance
    vb1_distance: float | None
    vb2_distance: float | None
    vb3_distance: float | None
    vb4_distance: float | None
    vb5_distance: float | None
    vb6_distance: float | None
    vb7_distance: float | None
    vb8_distance: float | None
    # Velocity band efforts
    vb1_efforts: float | None
    vb2_efforts: float | None
    vb3_efforts: float | None
    vb4_efforts: float | None
    vb5_efforts: float | None
    vb6_efforts: float | None
    vb7_efforts: float | None
    vb8_efforts: float | None
    # Acceleration bands
    accel_low_distance: float | None
    accel_low_efforts: float | None
    accel_med_distance: float | None
    accel_med_efforts: float | None
    accel_high_distance: float | None
    accel_high_efforts: float | None
    # Deceleration bands
    decel_low_distance: float | None
    decel_low_efforts: float | None
    decel_med_distance: float | None
    decel_med_efforts: float | None
    decel_high_distance: float | None
    decel_high_efforts: float | None
    # Groups
    low_velocity_distance: float | None
    low_velocity_efforts: float | None
    med_velocity_distance: float | None
    med_velocity_efforts: float | None
    high_velocity_distance: float | None
    high_velocity_efforts: float | None
    sprint_distance: float | None
    sprint_efforts: float | None

    model_config = {"from_attributes": True}


class ChronicWorkloadRead(BaseModel):
    id: int
    athlete_id: int
    date: datetime
    parameter: str
    daily_value: float | None
    acute_value: float | None
    chronic_value: float | None
    acwr: float | None

    model_config = {"from_attributes": True}


class TeamChronicWorkloadRead(BaseModel):
    athlete_id: int
    athlete_first_name: str
    athlete_last_name: str
    athlete_jersey: str | None
    parameter: str
    daily_value: float | None
    acute_value: float | None
    chronic_value: float | None
    acwr: float | None

    model_config = {"from_attributes": True}
