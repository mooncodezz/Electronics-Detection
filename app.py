from keras.models import load_model
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import cv2 
import os

output_name = ['Arduino', 'Capacitor', 'IC', 'Led', 'NodeMCU', 'Resistor', 'Transistor']
output = ''

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
while True:
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('image.jpg', image)
    del(camera)
    image = Image.open('image.jpg')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    p = prediction[0]
    os.system('clear')

    for i in range(len(output_name)):
        if p[i] >= p[0] and p[i] >= p[1] and p[i] >= p[2] and p[i] >= p[3] and p[i] >= p[4] and p[i] >= p[5] and p[i] >= p[6]:
            output = output_name[i]

    img = Image.open('image.jpg')
    width, height = img.size
    width = width // 2; height = height // 2
    img_text = ImageDraw.Draw(img)
    img_text.text((width, height), output, size=50, fill=(255, 0, 0))
    img.save("image.jpg")
    os.system('figlet ' + output)


exit_process = 'q' 

    