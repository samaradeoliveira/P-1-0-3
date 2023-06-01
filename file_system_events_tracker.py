import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/preet/Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!")

    def on_modified(self, event):
        print(f"Olá!, {event.src_path} foi modificado")
    
    def on_moved(self, event):
        print(f"Alguém moveu {event.src_path} para {event.dest_path}")
        

# Escolha o certo para: Inicializar a Classe Gerenciadora de Eventos
#event_handler = FileEventHandler()
#event_handl = FileEventHandler()
#event_handler = FileHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

#descomente para funcionar o Observer
#observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()

