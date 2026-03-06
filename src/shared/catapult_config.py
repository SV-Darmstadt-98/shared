from dataclasses import dataclass, field


@dataclass
class Param:
    slug: str
    column: str
    session_agg: str = "sum"  # sum | max | avg


@dataclass
class DerivedMetric:
    column: str
    formula: callable
    description: str


@dataclass
class Group:
    column: str
    sources: list[str] = field(default_factory=list)


PARAMS = [
    # General
    Param("total_duration", "total_duration"),
    Param("total_distance", "total_distance"),
    Param("max_vel", "max_velocity", session_agg="max"),
    # Velocity band distance
    Param("velocity_band1_total_distance", "vb1_distance"),
    Param("velocity_band2_total_distance", "vb2_distance"),
    Param("velocity_band3_total_distance", "vb3_distance"),
    Param("velocity_band4_total_distance", "vb4_distance"),
    Param("velocity_band5_total_distance", "vb5_distance"),
    Param("velocity_band6_total_distance", "vb6_distance"),
    Param("velocity_band7_total_distance", "vb7_distance"),
    Param("velocity_band8_total_distance", "vb8_distance"),
    # Acceleration bands
    Param("gen2_acceleration_band6_total_distance", "accel_low_distance"),
    Param("gen2_acceleration_band6_total_effort_count", "accel_low_efforts"),
    Param("gen2_acceleration_band7_total_distance", "accel_med_distance"),
    Param("gen2_acceleration_band7_total_effort_count", "accel_med_efforts"),
    Param("gen2_acceleration_band8_total_distance", "accel_high_distance"),
    Param("gen2_acceleration_band8_total_effort_count", "accel_high_efforts"),
    # Deceleration bands
    Param("gen2_acceleration_band3_total_distance", "decel_low_distance"),
    Param("gen2_acceleration_band3_total_effort_count", "decel_low_efforts"),
    Param("gen2_acceleration_band2_total_distance", "decel_med_distance"),
    Param("gen2_acceleration_band2_total_effort_count", "decel_med_efforts"),
    Param("gen2_acceleration_band1_total_distance", "decel_high_distance"),
    Param("gen2_acceleration_band1_total_effort_count", "decel_high_efforts"),
]

GROUPS = [
    Group("low_velocity_distance", ["vb1_distance", "vb2_distance"]),
    Group("med_velocity_distance", ["vb3_distance", "vb4_distance"]),
    Group("high_velocity_distance", ["vb5_distance", "vb6_distance", "vb7_distance"]),
    Group("sprint_distance", ["vb8_distance"]),
]


def _calc_distance_per_min(row: dict) -> float | None:
    """total_distance / total_duration * 60"""
    duration = row.get("total_duration") or 0
    if duration == 0:
        return None
    distance = row.get("total_distance") or 0
    return distance / duration * 60


def _calc_high_speed_ratio(row: dict) -> float | None:
    """(high_velocity_distance + sprint_distance) / total_distance"""
    total_dist = row.get("total_distance") or 0
    if total_dist == 0:
        return None
    high_vel = row.get("high_velocity_distance") or 0
    sprint = row.get("sprint_distance") or 0
    return (high_vel + sprint) / total_dist


def _calc_mechanical_density(row: dict) -> float | None:
    """(accel_high_efforts + decel_high_efforts) / total_duration * 60"""
    duration = row.get("total_duration") or 0
    if duration == 0:
        return None
    accel = row.get("accel_high_efforts") or 0
    decel = row.get("decel_high_efforts") or 0
    return (accel + decel) / duration * 60


DERIVED_METRICS = [
    DerivedMetric(
        column="distance_per_min",
        formula=_calc_distance_per_min,
        description="Distance covered per minute (session-level calculation)",
    ),
    DerivedMetric(
        column="high_speed_ratio",
        formula=_calc_high_speed_ratio,
        description="Ratio of high-speed running to total distance",
    ),
    DerivedMetric(
        column="mechanical_density",
        formula=_calc_mechanical_density,
        description="High-intensity mechanical efforts per minute",
    ),
]

SLUG_TO_COLUMN = {p.slug: p.column for p in PARAMS}
ALL_SLUGS = [p.slug for p in PARAMS]
METRIC_COLUMNS = [p.column for p in PARAMS]
GROUP_COLUMNS = [g.column for g in GROUPS]
SESSION_AGG = {p.column: p.session_agg for p in PARAMS}
DERIVED_COLUMNS = [m.column for m in DERIVED_METRICS]

PCA_FEATURES = [
    "total_duration",
    "total_distance",
    "max_velocity",
    *GROUP_COLUMNS,
    "accel_low_distance",
    "accel_low_efforts",
    "accel_med_distance",
    "accel_med_efforts",
    "accel_high_distance",
    "accel_high_efforts",
    "decel_low_distance",
    "decel_low_efforts",
    "decel_med_distance",
    "decel_med_efforts",
    "decel_high_distance",
    "decel_high_efforts",
    *DERIVED_COLUMNS,
]

EXCLUDED_PERIOD_TAGS = ["Reha", "Individuell", "Testing"]
