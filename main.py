from waitress import serve

from jobs.job_launcher import JobLauncher
from resources.routes import initialize_routes
from utils.config import *

# Iniciar tarefas agendadas
JobLauncher()


# Iniciar rotas
initialize_routes(api)

# Executar aplicacao
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8085)
