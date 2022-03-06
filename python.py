import numpy as np
from PIL import Image

def color_set(color, value): ##R成分を減らし，G,B成分を強調
    color[0] = abs(int(value / 2))
    color[1] = value + 30
    color[2] = value * 2
    if(color[1] > 255):
        color[2] = 255
    if(color[2] > 255):
        color[2] = 255



Image1 = Image.open("anime.jpg")
w, h = Image1.size
Image1 = np.array(Image1, dtype = "float64")
Image2 = Image.new("RGB", (w, h))

for y in range(h):
    for x in range(w):
        color = [Image1[y, x, 0], Image1[y, x, 1], Image1[y, x, 2]] ## r = Image1[y, x, 0] g = Image1[y, x, 1] b = Image1[y, x, 2]
        avg = int((color[0] + color[1] + color[2]) / 3)  
        if(avg < 50):
            color_set(color, 25)
        elif(avg < 100):
            color_set(color, 75)
        elif(avg < 150):
            color_set(color, 125)
        elif(avg < 200):
            color_set(color, 175)
        else:
            color_set(color, 225)
        Image2.putpixel((x, y), (int(color[0]), int(color[1]), int(color[2]))) #putpixel関数では画像のxyの順番が逆なので要注意！！

print("width : ", w)
print("height : ", h)

Image2.show()
Image2.save("output.jpg")

#print(Image[246, 220, 1])




