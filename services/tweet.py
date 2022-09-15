from typing import List
from fastapi import Response, HTTPException
from starlette import status
from sqlmodel import Session

from models import Tweet
from models.user import User
from schemas.user import UserAuth

from services.user import user as user_service
from schemas.tweet import TweetBase
from utils.tweet_addons import tweet_count


class TweetService:
    def create(self, request: TweetBase, request_user: UserAuth) -> Tweet:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user['id'])
            if user:
                tweet = Tweet(text=request.text, user=user.id)

                session.add(tweet)
                session.commit()
                session.refresh(tweet)
                return tweet
        
            raise HTTPException(detail='User not exists', status_code=404)

    def delete(self, id: int, request_user: UserAuth) -> Tweet:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user.id)
            tweet = session.query(Tweet).filter(Tweet.id == id).first()
            
            if user.id == tweet.user:
                tweet.is_active = False
                session.commit()  
                session.refresh(user)
                return Response(status_code=status.HTTP_204_NO_CONTENT)

            return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    # def get_all(self, db: Session, request_user: UserAuth) -> Tweet:
    #     user = db.query(User).filter(User.username == request_user['username'], User.is_active == True).first()
    #     user_actions = db.query(UserAction).filter(UserAction.user == user.id).all()
        
    #     json = []
    #     for user in user_actions:
    #         user = db.query(User).filter(User.id == user.user_ref, User.is_active == True).first()
    #         tweets = db.query(Tweet).filter(Tweet.user == user.id, Tweet.is_active == True).all()
    #         for tweet in tweets:
    #             data = {}
    #             data['id'] = tweet.id
    #             data['text'] = tweet.text
    #             data['user'] = tweet.user
    #             data['created_at'] = tweet.created_at

    #             json.append(data)

    #     json.sort(key=lambda x: x['created_at'], reverse=True)
    #     return json

    def get_tweet_by_id(self, id: int) -> Tweet:
        with Session(engine) as session:
            tweet = session.query(Tweet).filter(Tweet.id == id).first()
            tweet = tweet_count(tweet, db)
            return tweet

    def get_tweets_by_profile(self, username: str) -> List:
        tweets = []
        with Session(engine) as session:
            user = session.query(User).filter(User.username == username).first()
            if user:
                tweets = session.query(Tweet).filter(Tweet.user == user.id, Tweet.is_active == True).all()
        return tweets


tweet = TweetService()
