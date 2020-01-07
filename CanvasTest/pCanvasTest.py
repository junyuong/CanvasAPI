from tkinter import *
import PIL
from PIL import Image, ImageDraw
import requests
import io
API_HOST = 'http://10.20.1.216:8787/hr_test'


def get_image_text():
    global image_number
    file_object1 = io.BytesIO()
    file_object2 = io.BytesIO()
    file_object3 = io.BytesIO()
    file_object4 = io.BytesIO()

    image1.save(file_object1, 'png')
    image2.save(file_object2, 'png')
    image3.save(file_object3, 'png')
    image4.save(file_object4, 'png')

    file_object1.seek(0)
    file_object2.seek(0)
    file_object3.seek(0)
    file_object4.seek(0)
    data = {'img_file1': file_object1, 'img_file2': file_object2, 'img_file3': file_object3, 'img_file4': file_object4}
    print(data)
    url = API_HOST
    result = requests.post(url, files=data)
    print(result.text)
    image_number += 1

def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y

def activate_paint1(e):
    global lastx1, lasty1
    cv1.bind('<B1-Motion>', paint1)
    lastx1, lasty1 = e.x, e.y

def activate_paint2(e):
    global lastx2, lasty2
    cv2.bind('<B1-Motion>', paint2)
    lastx2, lasty2 = e.x, e.y

def activate_paint3(e):
    global lastx3, lasty3
    cv3.bind('<B1-Motion>', paint3)
    lastx3, lasty3 = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=1)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=2)
    lastx, lasty = x, y

def paint1(e):
    global lastx1, lasty1
    x, y = e.x, e.y
    cv1.create_line((lastx1, lasty1, x, y), width=1)
    #  --- PIL
    draw1.line((lastx1, lasty1, x, y), fill='black', width=2)
    lastx1, lasty1 = x, y

def paint2(e):
    global lastx2, lasty2
    x, y = e.x, e.y
    cv2.create_line((lastx2, lasty2, x, y), width=1)
    #  --- PIL
    draw2.line((lastx2, lasty2, x, y), fill='black', width=2)
    lastx2, lasty2 = x, y

def paint3(e):
    global lastx3, lasty3
    x, y = e.x, e.y
    cv3.create_line((lastx3, lasty3, x, y), width=1)
    #  --- PIL
    draw3.line((lastx3, lasty3, x, y), fill='black', width=2)
    lastx3, lasty3 = x, y

root = Tk()

lastx, lasty = None, None
lastx1, lasty1 = None, None
lastx2, lasty2 = None, None
lastx3, lasty3 = None, None
image_number = 0

cv = Canvas(root, width=224, height=224, bg='white')
cv1 = Canvas(root, width=224, height=224, bg='white')
cv2 = Canvas(root, width=224, height=224, bg='white')
cv3 = Canvas(root, width=224, height=224, bg='white')

# --- PIL
image1 = PIL.Image.new('RGB', (224, 224), 'white')
image2 = PIL.Image.new('RGB', (224, 224), 'white')
image3 = PIL.Image.new('RGB', (224, 224), 'white')
image4 = PIL.Image.new('RGB', (224, 224), 'white')

draw = ImageDraw.Draw(image1)
draw1 = ImageDraw.Draw(image2)
draw2 = ImageDraw.Draw(image3)
draw3 = ImageDraw.Draw(image4)

cv.bind('<1>', activate_paint)
cv1.bind('<1>', activate_paint1)
cv2.bind('<1>', activate_paint2)
cv3.bind('<1>', activate_paint3)

cv.pack(expand=YES, fill=BOTH)
cv1.pack(expand=YES, fill=BOTH)
cv2.pack(expand=YES, fill=BOTH)
cv3.pack(expand=YES, fill=BOTH)

btn_save = Button(text="GetImageText", command=get_image_text)
btn_save.pack()

root.mainloop()