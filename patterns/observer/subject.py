"""
Description: {description of the file.}
Author: {student name}
"""
from patterns.observer.observer import Observer

class Subject:
    """
    """
    def __init__(self):
        """
        """
        self._observers = []

    def attach(self, observer: Observer):
        """
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """
        """
        for observer in self._observers:
            observer.update(message)