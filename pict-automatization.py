from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import os
import shutil

class Handler(PatternMatchingEventHandler):

    def on_modified(self, event):
        extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp']

        for filename in os.listdir(old_folder):
            file = filename.split('.')
            file_extension = file[-1].lower()
            if file_extension in extensions:
                old_place = old_folder + '/' + filename
                new_place = new_folder + '/' + filename
                shutil.move(old_place, new_place)


old_folder = os.path.join('')
new_folder = os.path.join('')

handler = Handler()
observer = Observer()
observer.schedule(handler, old_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()