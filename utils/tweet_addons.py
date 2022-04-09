
from typing import Dict

from sqlmodel import Session
from models.tweet import Like, Retweet, Tweet


def tweet_count(tweet: Tweet, db: Session) -> Dict:
    tweet = tweet.dict()
    likes = db.query(Like).filter(Like.tweet == tweet['id'], Like.is_active == True).count()
    retweets = db.query(Retweet).filter(Retweet.tweet == tweet['id'], Retweet.is_active == True).count()
    tweet.update(likes=likes, retweets=retweets)

    return tweet