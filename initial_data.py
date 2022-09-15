import logging
from sqlalchemy.orm import Session

from core.base_class import Base
from core import base 
from core.session import SessionLocal, engine

logger = logging.getLogger(__name__)


def init():
    Base.metadata.create_all(bind=engine)

def main() -> None:
    logger.info("creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == '__main__':
    main()