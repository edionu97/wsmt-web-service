from flask_jsonrpc.proxy import ServiceProxy


class Interface:

    def __init__(self, service: ServiceProxy):
        self.__service = service

    def run(self):
        actions = self.__create_menu()

        while True:

            Interface.__show_options()

            option = input("Enter option: ")
            if option not in actions:
                print("Wrong option")
                continue

            actions[option]()
        pass

    @staticmethod
    def __show_options():
        print("\n\n\n\n\n========================================\n")
        print("     1. For getting the files filtered by name")
        print("     2. For getting the files filtered by content")
        print("     3. For getting the filed filtered by hex bytes")
        print("     4. For getting all the duplicates")
        print("     5. For application exit")
        print("\n========================================")

    def __create_menu(self):
        return {
            "1": self.__option_1,
            "2": self.__option_2,
            "3": self.__option_3,
            "4": self.__option_4,
            "5": lambda: exit(0)
        }

    def __option_1(self):
        result = self.__result(self.__service.App.getFilesByName(name=input("Enter file name part: ")))
        if len(result) == 0:
            print("No files are matching")
            return

        for file in result:
            print(file)

    def __option_2(self):
        result = self.__result(self.__service.App.getFilesByText(text=input("Enter file text part: ")))
        if len(result) == 0:
            print("No files are matching")
            return

        for file in result:
            print(file)

    # ff,d8,ff (the witcher 3)
    def __option_3(self):
        result = self.__result(self.__service.App.getFilesByBinary(binary=input("Enter binary bytes, and separate by "
                                                                                "comma: ").split(",")))

        if len(result) == 0:
            print("No files are matching")
            return

        for file in result:
            print(file)

    def __option_4(self):
        result = self.__result(self.__service.App.getDuplicates())
        if len(result) == 0:
            print("No files are matching")
            return

        for duplicate in result:
            print("\n********")
            for file in duplicate:
                print("           ", file)
            print("********\n")

    @staticmethod
    def __result(call):
        return call['result']
