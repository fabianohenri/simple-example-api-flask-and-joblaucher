import threading
import time

from jobs.safe_schedule import SafeScheduler


def run():
    # Instanciar a execucao segura dos jobs
    scheduler = SafeScheduler()

    # Roda o reset todos os dias a 03:00
    #scheduler.every().day.at("03:00").do(ResetIp.reset)

    # Manter o loop
    while True:
        scheduler.run_pending()
        time.sleep(1)


class JobLauncher:
    # Construtor
    def __init__(self):
        # Iniciar a thread
        thread_customer_create = threading.Thread(target=run, args=())
        thread_customer_create.daemon = True
        thread_customer_create.name = "JobLaucher"
        thread_customer_create.start()
