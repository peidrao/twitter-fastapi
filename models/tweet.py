from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Tweet(Base):
    id = Column(Integer, primary_key=True, index=True)
    text =  Column(String(140), nullable=False)
    likes = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", lazy='subquery', foreign_keys=[user_id])
    

class Like(Base):
    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)

    tweet = relationship("Tweet", foreign_keys=[tweet_id])
    user = relationship("User", foreign_keys=[user_id])


class Retweet(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String(140))
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)

    tweet = relationship(Tweet, foreign_keys=[tweet_id])
    user = relationship("User", foreign_keys=[user_id])
