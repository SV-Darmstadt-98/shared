from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from shared.models import Base


class SyncLog(Base):
    __tablename__ = "sync_log"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False, index=True)
    status = Column(String, nullable=False)
    job_id = Column(String, index=True)
    started_at = Column(DateTime, nullable=False, server_default=func.now())
    finished_at = Column(DateTime)
    records_processed = Column(Integer)
    error_message = Column(Text)
    metadata_ = Column("metadata", JSONB)
