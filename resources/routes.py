from api.status_api import StatusApi


def initialize_routes(app):
    # Rotas de acesso aos endpoints da API
    app.add_resource(StatusApi, '/api/status')
