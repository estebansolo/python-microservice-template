from source.users.domain.fake import Fake
from source.users.ports.repositories.fake_repository import FakeRepository


class DummyFakeEntityRepository(FakeRepository):
    async def save(self, fake_entity: Fake) -> None:
        pass
