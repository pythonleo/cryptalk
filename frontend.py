from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def main(_):
    with open("current.txt", encoding="utf-8") as fr:
        return Response(fr.read())


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('main', '/')
        config.add_view(main, route_name='main')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 80, app)
    server.serve_forever()
