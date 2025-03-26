from flask import Flask, request, jsonify
import torch
from PIL import Image
import io

app = Flask(__name__)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.route('/detect',methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # object detection from images
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    results = model(img)

    labels = results.names
    detect_classes = results.pred[0][:, -1].tolist()

    # turns class index to label and adds label to list
    detected = []
    for cls in detected_classes:
        label = label[int(cls)]
        if label not in detected:
            detected.append(label)
    
    return jsonify({'labels':detected})

if __name__ == "main":
    app.run(debug=True)


