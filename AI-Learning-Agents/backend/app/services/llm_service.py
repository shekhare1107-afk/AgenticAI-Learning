from abc import ABC, abstractmethod


class LLMService(ABC):

    @abstractmethod
    def decide(self, message: str) -> dict:
        pass