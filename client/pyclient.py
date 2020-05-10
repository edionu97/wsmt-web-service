from flask_jsonrpc.proxy import ServiceProxy
from lxml import objectify

from client.ui.interface import Interface

try:
    # open the constants folder to get the host and port necessary for client app to connect
    with open('../resources/constants.xml', 'r') as file:
        constants = objectify.fromstring(file.read())

    # create the proxy service (connect to the service)
    service = ServiceProxy(service_url="http://{host}:{port}/api"
                           .format(host=str(constants.host), port=int(constants.port)))

    # run the interface
    Interface(service=service).run()
except Exception as e:
    print(e)



