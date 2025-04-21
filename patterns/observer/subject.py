"""
Description: {description of the file.}
Author: {student name}
"""
from patterns.observer.observer import Observer

class Subject:
    """
    Contains a list of obersevers.
    Args:
        _observers(): The list of observers.

    Methods:
        attach(observer): Add observer to the observers list.
        detach(observer): Remove observer from the observers list.
        notify(message:str): Notify all observer in the list with the message given.
    """
    def __init__(self):
        """
        Initialize a object with an empty list
        """
        self._observers = []

    def attach(self, observer: Observer):
        """
        Add observer to the observers list.
        Args:
            observer: The object that been added to the observers list.

        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Remove observer from the observers list.
        Args:
            The object that been removed from the observers list.

        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """
        Notify all observer in the list with the message given.
        Args:
            message(str): Message been notified to all observers in the list.
        """
        for observer in self._observers:
            observer.update(message)