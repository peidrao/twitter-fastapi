from fastapi import Response, status, HTTPException
from sqlmodel import Session

from models import Tweet
from models.user import User, UserAction
from schemas.user import UserAuth

from services.user import user as user_service
from schemas.tweet import TweetBase
from utils.tweet_actions import verify_status_profile
from utils.tweet_addons import tweet_count


class TweetService:
    def create(self, db: Session, request: TweetBase, request_user: UserAuth) -> Tweet:
        user = user_service.get_user_by_id(db, request_user['id'])
        if user:
            tweet = Tweet(
                text=request.text,
                user=user.id
            )

            db.add(tweet)
            db.commit()
            db.refresh(tweet)
            return tweet
    
        raise HTTPException(detail='User not exists', status_code=404)

    def delete(self, db: Session, id: int, request_user: UserAuth) -> Tweet:
        user = user_service.get_user_by_id(db, request_user['id'])
        tweet = db.query(Tweet).filter(Tweet.id == id).first()
        
        if user.id == tweet.user:
            tweet.is_active = False
            db.commit()  
            db.refresh(user)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    def get_all(self, db: Session, request_user: UserAuth) -> Tweet:
        user = db.query(User).filter(User.username == request_user['username'], User.is_active == True).first()
        user_actions = db.query(UserAction).filter(UserAction.user == user.id).all()
        
        json = []
        for user in user_actions:
            user = db.query(User).filter(User.id == user.user_ref, User.is_active == True).first()
            tweets = db.query(Tweet).filter(Tweet.user == user.id, Tweet.is_active == True).all()
            for tweet in tweets:
                data = {}
                data['id'] = tweet.id
                data['text'] = tweet.text
                data['user'] = tweet.user
                data['created_at'] = tweet.created_at

                json.append(data)

        json.sort(key=lambda x: x['created_at'], reverse=True)
        return json

    def get_tweet_by_id(self, db: Session, id: int) -> Tweet:
        tweet = db.query(Tweet).filter(Tweet.id == id).first()
        tweet = tweet_count(tweet, db)
        return tweet

    
    def get_tweets_by_profile(self, db: Session, username: str, request_user: UserAuth) -> Tweet:
        user = db.query(User).filter(User.username == username).first()
        user_action = db.query(UserAction).filter(UserAction.user == request_user['id'], UserAction.user_ref == user.id).first()
        user_action2 = db.query(UserAction).filter(UserAction.user == user.id, UserAction.user_ref == request_user['id']).first()
        
        status = verify_status_profile(user_action)
        status2 = verify_status_profile(user_action2)

        if not status:
            return False
        
        if not status2:
            return False

        tweets = db.query(Tweet).filter(Tweet.user == user.id, Tweet.is_active == True).all()
        return tweets


tweet = TweetService()
