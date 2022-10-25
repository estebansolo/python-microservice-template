from dataclasses import dataclass

from source.users.domain.fake import Fake
from source.users.ports.logger import Logger
from source.users.ports.repositories.fake_repository import FakeRepository


@dataclass
class FakeService:
    fake_repository: FakeRepository
    logger: Logger

    async def execute(self, id: int, name: str) -> None:
        fake_entity = Fake(id=id, name=name)
        await self.fake_repository.save(fake_entity)
