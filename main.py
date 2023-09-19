from bestconfig import Config
import os.path, shutil, pathlib
config = Config("configuration.json")
WORKING_DIR = ""

def main():
    # Get configuration values
    WORKING_DIR = config.get("MAIN")
    COPY = config.get("COPY")
    CHANGE = config.get("CHANGE")
    DELETE = config.get("DELETE")
    change(CHANGE)
    delete(DELETE)
    copy(COPY) 


# Change all text in files 
def change(CHANGE):
    for c in CHANGE:
        f = config.get(f'CHANGE.{c}.from')
        t = config.get(f'CHANGE.{c}.to')
        p = config.get(f'CHANGE.{c}.in')
        path = pathlib.Path(p)
        path.write_text(path.read_text().replace(f, t))

def delete(DELETE):
    for d in DELETE:
        file = WORKING_DIR + config.get(f'DELETE.{d}.dir')
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)

# Copy files in working directory
def copy(COPY):
    for c in COPY:
        cp = 1

main()