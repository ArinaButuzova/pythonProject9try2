import os
from PIL import Image

if not os.path.exists('kart2'):
    os.mkdir('kart2')

k = 1

for i in os.listdir('photo'):
    if i.lower().endswith('.jpg'):
        img = Image.open(os.path.join('photo', i))
        resized_img = img.resize((img.width // 3, img.height // 3))
        new_filename = f"img{k}.jpg"
        resized_img.save(os.path.join('kart2', new_filename))
    if i.lower().endswith('.png'):
            img = Image.open(os.path.join('photo', i))
            resized_img = img.resize((img.width // 3, img.height // 3))
            new_filename = f"img{k}.png"
            resized_img.save(os.path.join('kart2', new_filename))
    k += 1

print("Программа успешно выполнена.")
