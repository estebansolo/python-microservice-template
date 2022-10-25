from abc import ABC, abstractmethod

from source.users.domain.fake import Fake


class FakeRepository(ABC):
    @abstractmethod
    async def save(self, fake: Fake) -> None:
        raise NotImplementedError
