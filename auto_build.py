import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JupyterBookHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.md') or event.src_path.endswith('.yml'):
            print(f"Fichier modifié : {event.src_path}")
            print("Reconstruction en cours...")
            subprocess.run(['jupyter-book', 'build', '.'])
            print("Build terminé !")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(JupyterBookHandler(), path='.', recursive=True)
    observer.start()
    print("Surveillance activée. Appuyez sur Ctrl+C pour arrêter.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()