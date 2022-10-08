from spyne import ServiceBase, Unicode, rpc, Application
import xml.etree.ElementTree as ET
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

countries = {"be":"Belgium", "az":"	Azerbaijan", "fr":"France", "de":"Germany"}

class ExampleService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def getCountry(ctx, request):
        try:
            r = ET.fromstring(request)
        except:
            return u'No XML sent'
        try:
            return u'Requested country: %s' % countries[r[0].text]
        except:
            return u'Country not found'

application = Application(
    services = [ExampleService],
    tns = 'example',
    in_protocol = Soap11(validator = 'lxml'),
    out_protocol = Soap11()
)

application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print("listening to http://127.0.0.1:8000")
    print("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()