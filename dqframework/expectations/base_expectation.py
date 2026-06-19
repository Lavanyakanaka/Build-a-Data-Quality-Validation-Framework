from abc import ABC, abstractmethod

class BaseExpectation(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def validate(self, df):
        pass