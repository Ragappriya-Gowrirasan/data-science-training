import cv2
from cvzone.ClassificationModule import Classifier
import cvzone
# Create a VideoCapture object for your camera (usually 0 for the default camera)
video = cv2.VideoCapture(0)

# Load the pre-trained model and labels
my_classifier = Classifier('C:/Users/ragap/OneDrive/Desktop/data-science-training/build-AI/model/keras_model.h5', 'C:/Users/ragap/OneDrive/Desktop/data-science-training/build-AI/model/labels.txt')

while True:
    img = video.read()
    predictions = my_classifier.getPrediction(img)
    print(predictions)
    cv2.imshow('Screen', img)

    cv2.waitKey(1) 
    break
