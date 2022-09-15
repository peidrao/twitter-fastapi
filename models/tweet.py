from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from core.base_class import Base


class Tweet(Base):
    id = Column(Integer, primary_key=True, index=True)
    text =  Column(String(140), nullable=False)
    likes = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", back_populates="tweet")
    

class Like(Base):
    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)

    tweet = relationship(Tweet, back_populates='like')
    user = relationship("User", back_populates='like')



class Retweet(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String(140))
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)

    tweet = relationship(Tweet, back_populates='retweet')
    user = relationship("User", back_populates='retweet')
