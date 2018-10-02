from PIL import Image
im = Image.open('img.png')
fh = open('img.txt','a')
width = im.size[0]
print(width)
height = im.size[1]
print(height)
for i in range(height):
    for k in range(width):
        cl = im.getpixel((k,i))
        if cl[0]==cl[1]==cl[2]==255:
            fh.write('0')
        else:
            fh.write('1')
    fh.write('\n')
fh.close()