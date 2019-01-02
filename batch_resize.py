from PIL import Image
import os, sys

path = os.getcwd()+"/"+sys.argv[1]
dirs = os.listdir(path)
size = (int(sys.argv[2]), int(sys.argv[3]))
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize(size, Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=50)

resize()
