from abc import ABC, abstractmethod

from source.products.domain.fake import Fake


class FakeRepository(ABC):
    @abstractmethod
    async def save(self, fake: Fake) -> None:
        raise NotImplementedError
