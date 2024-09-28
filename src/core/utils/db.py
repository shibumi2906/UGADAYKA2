from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.models import Base


# Указываем путь к базе данных в папке src
DATABASE_URL = "sqlite:///src/db/data.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для инициализации базы данных
def init_db():
    Base.metadata.create_all(bind=engine)



