from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)

from app.db.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class Run(Base):

    __tablename__ = "runs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    issue_number = Column(
        Integer,
        nullable=False
    )

    repository = Column(
        String(255),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


class AgentRun(Base):

    __tablename__ = "agent_runs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    run_id = Column(
        Integer,
        ForeignKey("runs.id"),
        nullable=False
    )

    agent_name = Column(
        String(100),
        nullable=False
    )

    input = Column(
        Text,
        nullable=True
    )

    output = Column(
        Text,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=False,
        default="running"
    )

    duration = Column(
        Integer,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now
    )


class Artifact(Base):

    __tablename__ = "artifacts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    run_id = Column(
        Integer,
        ForeignKey("runs.id"),
        nullable=False
    )

    artifact_type = Column(
        String(100),
        nullable=False
    )

    content = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now
    )