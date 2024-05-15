import os
from PIL import Image

os.mkdir('kart')
k = 0

for i in os.listdir('photo'):
    if i.endswith('.jpg'):
        img = Image.open(os.path.join('photo', i))
        resized_img = img.resize((img.width // 2, img.height // 2))
        k += 1
        new_filename = f"img{k}.jpg"
        resized_img.save(os.path.join('kart', new_filename))
