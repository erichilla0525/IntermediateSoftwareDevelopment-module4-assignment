"""
Description: {description of the file.}
Author: {student name}
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstracted base class for observer pattern
    Method:
        update(message: str): Update the message received from subjects.
    """
    @abstractmethod
    def update(self, message: str):
        """
        Update the message received from the subject.

        Args:
            meessage(str): Message from the subject.
        """
        pass