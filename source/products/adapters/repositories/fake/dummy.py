from source.products.domain.fake import Fake
from source.products.ports.repositories.fake_repository import FakeRepository


class DummyFakeEntityRepository(FakeRepository):
    async def save(self, fake_entity: Fake) -> None:
        pass
