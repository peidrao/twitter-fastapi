from turtle import back
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .user import User
from database.session import Base


# class Tweet(Base):
#     __tablename__ = 'tweet'
#     id = Column(Integer, primary_key=True, index=True)

#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime)
#     deleted_at = Column(DateTime, default=None)
    
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User, back_populates='items')



# class User(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     username: Optional[str] = Field(max_length=120, nullable=False)
#     email: Optional[str] = Field(max_length=200, nullable=False)
#     password: Optional[str] = Field(max_length=200, nullable=False)
#     birthday: Optional[datetime] = Field(nullable=False)

#     is_active: Optional[bool] = Field(default=True)
#     is_banned: Optional[bool] = Field(default=False)

#     created_at: Optional[datetime] = Field(default=datetime.utcnow)
#     updated_at: Optional[datetime] = Field(default=datetime.utcnow)