from controller import Robot
import cv2
import numpy as np
import requests

robot = Robot()
timestep = int(robot.getBasicTimeStep())

camera = robot.getDevice('camera')
camera.enable(timestep)

while robot.step(timestep) != -1:
    image = camera.getImage()
    width = camera.getWidth()
    height = camera.getHeight()
    impg = np.frombuffer(image, npuint8).reshape(height, width, 4)
    bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    cv2.imwrite("frame.jpg", bgr)

    try:
        files = {"file": open('frame.jpg', 'rb')}
        response = requests.post("http://localhost:5000/detect", files=files)
        result = response.json()
        print("Detected objects:", result)
    except:
        print("Could not reach the cloud API.")

    break
