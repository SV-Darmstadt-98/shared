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
    total_distance: float | None
    sprints: int | None
    sprint_distance: float | None
    hsr_distance: float | None
    accelerations: int | None
    decelerations: int | None

    model_config = {"from_attributes": True}
