import mimetypes
import os

from binaryornot.check import is_binary

from storage.model.models import Directory, File
from storage.repository.irepository import IRepository


class DbPopulator:

    def __init__(self, repository: IRepository):
        self.__repository = repository
        self.__directory_count = 0

    def get_files(self, file_path, parent_id=None):
        """
            Recursive method
            :param file_path: the path of the file
            :param parent_id: the parent_id (represents the directory)
            :return: none
        """

        # if the file is not directory
        if not os.path.isdir(file_path):
            self.__process_files(path=file_path, directory_id=parent_id)
            return

        # increment the number of total directories
        self.__directory_count += 1

        # get the name of the directory
        directory_name = file_path.split("\\")[-1]
        directories = [os.path.join(file_path, directory) for directory in os.listdir(file_path)]

        # noinspection PyTypeChecker
        self.__repository.add(
            Directory(name=directory_name, object_id=self.__directory_count, parent_directory_id=parent_id))

        # recursively create the directory structure
        parent_id = self.__directory_count
        for directory in directories:
            self.get_files(file_path=directory, parent_id=parent_id)

    def __process_files(self, path, directory_id):
        """
            This method is used in order to read the content of a file
            :param path: the file path
            :param directory_id: the parent directory
            :return: none
        """

        # open the file in reading
        binary = is_binary(path)
        with open(path, mode='rb' if binary else 'r') as opened_file:
            file = File(directory_id=directory_id, name=path.split("\\")[-1])

            # check if the file is binary
            if binary:
                file.binary_content = opened_file.read()
                self.__repository.add(file)
                return

            # the file is text
            file.text_content = opened_file.read()
            self.__repository.add(file)
