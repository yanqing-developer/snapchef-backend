from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./snapchef.db"

engine = create_engine(
    DATABASE_URL,connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

