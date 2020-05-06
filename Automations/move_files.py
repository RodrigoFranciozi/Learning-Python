from watchdog.observers import Observer
import time 
from watchdog.events import FileSystemEventHandler

import os
import json
     
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for nome_arquivo in os.listdir(pasta_para_rastrear):
            src = pasta_para_rastrear + "/" + nome_arquivo
            novo_destino = pasta_destino + "/" + nome_arquivo
            os.rename(src, novo_destino) 

pasta_para_rastrear = "C:/Users/rodri/Downloads"
pasta_destino = "C:/Users/rodri/Desktop/dowload_manager"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, pasta_para_rastrear, recursive=True)
observer.start()

try:   
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
