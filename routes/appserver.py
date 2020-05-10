from flask import Flask

from routes import jsonrpc, app
from service.iservice import IService


class AppServer:
    service: IService

    def __init__(self, service: IService, constants):
        AppServer.service = service
        self.__constants = constants

    def start_server(self):
        """
            This method is used in order to start the server
            :return: None
        """
        app.run(host=str(self.__constants.host),
                port=int(self.__constants.port),
                debug=bool(self.__constants.runindebug))

    @staticmethod
    @jsonrpc.method('App.getFilesByName')
    def find_file_by_name(**kwargs):
        """
            This method returns a list of files, filtered by a name
            :param kwargs: this dictionary must contain a entry for :param name,
                            representing the pattern that must be found in the files name
            :return: the list of filtered values
        """
        return AppServer.service.find_file_by_name(name=kwargs['name'])

    @staticmethod
    @jsonrpc.method('App.getFilesByText')
    def find_file_by_text(**kwargs):
        """
            This method returns a list of files, filtered by a name
            :param kwargs: this dictionary must contain a entry for :param text,
                            representing the pattern that must be found in the files content
            :return: the list of filtered values
        """
        return AppServer.service.find_file_by_name(name=kwargs['text'])

    @staticmethod
    @jsonrpc.method('App.getFilesByBinary')
    def find_file_by_binary(**kwargs):
        """
            This method returns a list of files, filtered by a name
            :param kwargs: this dictionary must contain a entry for :param binary,
                            representing the pattern that must be found in the files binary content
            :return: the list of filtered values
        """
        return AppServer.service.find_file_by_binary(binary=kwargs['binary'])

    @staticmethod
    @jsonrpc.method('App.getDuplicates')
    def find_duplicates():
        """
            This method returns a list of duplicate files
        """
        return AppServer.service.find_duplicated_files()
