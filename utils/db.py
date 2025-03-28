from sqlmodel import create_engine, SQLModel


DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=False)

SQLModel.metadata.create_all(engine)
