from os import path, walk, listdir
import shutil

project_name = 'my_project'

try:
    for root, dirs, files in walk(project_name):
        if ' tamplaters' in dirs and root != project_name:
            for entry in listdir(path.join(root, "tamplates")):
                shutil.copytree(path.join(root, 'tamplates', entry), path.join(project_name, 'templates', entry))
except FileExistsError:
    print("Already worked")
