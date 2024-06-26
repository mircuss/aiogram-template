from sqlalchemy import BigInteger
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
