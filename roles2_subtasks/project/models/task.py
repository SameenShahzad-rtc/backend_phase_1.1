
from sqlalchemy import  Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = "tasks"  # make consistent: "tasks" not "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    des = Column(String, nullable=False)
    status = Column(String, default="pending", nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="tasks")
    assigned_user = relationship(
        "User",
        back_populates="assigned_tasks",
        foreign_keys=[assigned_to]
    )
    subtasks = relationship(
        "Subtask",  # string name ensures it can resolve later
        back_populates="task",
        cascade="all, delete-orphan"
    )