from abc import ABC, abstractmethod

#Interfaccia
class IPrinter(ABC):

    @abstractmethod
    def print(self, pathFile, tipo):
        pass