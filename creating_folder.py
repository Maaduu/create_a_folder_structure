# Importing Operating System module
import os
import json

def creating_folder(folders):
  for key, values in folders.items():
    for value in values:
      folder = '{0}/{1}/{2}'.format(path_folder, key, value)
      os.makedirs(folder)
      print('Creating folder {0}'.format(folder))

def creating_json_file(path_json_file, dictionnaire):
  with open(path_json_file, 'w') as f:
    json.dump(dictionnaire, f, indent=4)


path_folder = r'C:\wamp64\www\Dev\u\Python\in_git\create_a_folder_structure\creating_folder\structure'
path_folder = path_folder.replace('\\', '/')
#os.listdir(path_folder)

path_json_file = r'C:\wamp64\www\Dev\u\Python\in_git\create_a_folder_structure\creating_folder\structure\structure.json'
path_json_file = path_json_file.replace('\\', '/')

structure = {
  'Movies': ['Game of Trhones', 'Get rich or die', 'Dogs of instambul'],
  'Music': ['Rock', 'Rap', 'Reggae']
}

# Create the folders
creating_folder(structure)
# Create the json file
creating_json_file(path_json_file, structure)
