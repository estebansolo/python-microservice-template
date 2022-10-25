from source.users.ports.logger import Logger


class PrintLogger(Logger):
    async def info(self, message: str) -> None:
        print(message)
