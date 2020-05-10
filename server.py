from lxml import objectify

from helpers.dbhelpers import DbHelper
from helpers.dbpopulator import DbPopulator
from routes.appserver import AppServer
from service.impl.service import Service
from storage.repository.Impl.repository import Repository

try:
    # read the constants folder
    with open('./resources/constants.xml', 'r') as file:
        constants = objectify.fromstring(file.read())

    # create the repository
    repository = Repository(helper=DbHelper(), constants=constants)
    if bool(constants.populatedb):
        DbPopulator(repository).get_files(file_path=str(constants.populatedbmainfolder))

    # start the server
    AppServer(service=Service(repository), constants=constants).start_server()

except Exception as e:
    print('Error', e)

