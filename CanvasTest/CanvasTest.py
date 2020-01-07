from tkinter import *
import PIL
from PIL import Image, ImageDraw
import requests
import io
import pprint
API_HOST = 'http://10.20.1.216:8787/hr_test'
root = Tk()
lastx, lasty = None, None
my_obj = []
data = []


class ObjCanvas(object):
    count = 0  # 생성된 클래스 개수를 확인하기 위한 변수
    # 생성자(Constructor)선언

    def __init__(self, img, cv, draw):
        # 변수 초기화 img, cv, draw
        self.img = img
        self.cv = cv
        self.draw = draw
        self.set_bind()
        ObjCanvas.count = ObjCanvas.count + 1

    def set_bind(self):
        self.cv.bind('<1>', lambda event: activate_paint(event, cv=self.cv, draw=self.draw))
        self.cv.pack(expand=YES, fill=BOTH)


def activate_paint(e, cv, draw):
    global lastx, lasty
    cv.bind('<B1-Motion>', lambda event: paint(event, cv=cv, draw=draw))
    lastx, lasty = e.x, e.y


def paint(e, cv, draw):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=1)
    draw.line((lastx, lasty, x, y), fill='black', width=2)
    lastx, lasty = x, y


def get_image_text():

    for obj in my_obj:
        file_object = io.BytesIO()
        obj.img.save(file_object, 'png')
        file_object.seek(0)
        data.append(file_object)

    for i in range(len(data)):
        data[i] = {'img_file'+str(i): data[i]}
        try:
            url = API_HOST
            pprint.pprint('Request : ')
            result = requests.post(url, files=data[i])
            print('Response : ' + result.text)
        except Exception as e:
            print(e)


def insert_canvas():
    # 추가 버튼 클릭 시 Canvas를 추가
    image = PIL.Image.new('RGB', (224, 224), 'white')
    draw = ImageDraw.Draw(image)
    cv = Canvas(root, width=224, height=224, bg='white')

    # 클래스 객체 생성
    objc = ObjCanvas(img=image, cv=cv, draw=draw)
    my_obj.append(objc)


def main():
    btn_insert = Button(text="추가", command=insert_canvas)
    btn_insert.pack(side='right')
    btn_save = Button(text="GetImageText", command=get_image_text)
    btn_save.pack(side='right')
    root.mainloop()

if __name__ == '__main__':
    main()
