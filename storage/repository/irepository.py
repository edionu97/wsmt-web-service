from abc import abstractmethod


class IRepository:
    """
        This is the base class (interface) that defines the repository operations
    """
    def __init__(self):
        pass

    @abstractmethod
    def add(self, value):
        """
            This method is used for adding a new value into database
            :param value: the value that will be added
            :return: none
        """
        pass

    @abstractmethod
    def all(self, table):
        """
            This method is used to extract all data that exist in the database
            :return: a list with all the elements
        """
        pass

    @abstractmethod
    def filter(self, predicate, filters):
        """
            This method is used to filter the data
            :param predicate: the filtering predicate
            :return: a list of elements, that respects the given predicate
        """
        pass

