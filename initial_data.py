import logging

from database import engine, Base

logger = logging.getLogger(__name__)


def init():
    Base.metadata.create_all(bind=engine)

def main() -> None:
    logger.info("creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == '__main__':
    main()