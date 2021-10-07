import sys
import os
from PIL import Image

#grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]


#check if new/ exists, if not create
if not os.path.exists(directory):
    os.makedirs(directory)

#loop through pokedex and convert to png
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')

#save
  img.save(f'{directory}/{clean_name}.png', 'png')
  print(f"{clean_name}.jpg converted to .png and saved to the new dir")