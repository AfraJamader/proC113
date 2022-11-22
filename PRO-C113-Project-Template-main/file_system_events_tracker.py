import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ="C:/Users/Dell/Downloads"
to_dir = "C:/Users/Dell/OneDrive/Documents"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"hey , {event.from_dir} has been created! ")

    #2_on_deleted
    def on_deleted(self, event):
        print(f"oops ! someone has deleted your {event.from_dir}")

    #3_on_modified
    def on_modified(self, event):
        print(f"hey there ! {event.from_dir} has been modified")

    #4_on_moved
    def on_moved(self, event):
        print(f"hey ! someone has moved {event.from_dir} to {event.to_dir}")

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running..p.")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()







