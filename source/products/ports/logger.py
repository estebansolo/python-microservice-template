from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    async def info(self, message: str) -> None:
        raise NotImplementedError
