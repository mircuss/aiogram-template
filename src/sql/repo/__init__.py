from sqlalchemy.ext.asyncio.session import AsyncSession
from .user_repo import UserRepo


class Repo(UserRepo):
    def __init__(self, session: AsyncSession):
        super().__init__(session)


__all__ = [Repo]
