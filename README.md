# HOG-SVM-ImageClassifier
**The HOG-SVM Image Classifier is a technique used for image recognition and object detection. To create a model, you collect a dataset and use HOG to extract features from images. These features are fed into the SVM algorithm to train the model. The trained model can classify new images. Testing involves using a separate set of images to evaluate the model's accuracy. The HOG-SVM Image Classifier is a powerful technique for accurately recognizing objects in a wide range of scenarios.**

# Some Images
![image_0002](https://github.com/Abdelrhman-Sayed70/HOG-SVM-ImageClassifier/assets/99830416/90f929c3-a7e4-4b0e-894f-bdd4e94b8cdd)
![image_0014](https://github.com/Abdelrhman-Sayed70/HOG-SVM-ImageClassifier/assets/99830416/4187e1e0-5b6b-43d4-83d3-2c4e35e9ab6a)

![image_0001](https://github.com/Abdelrhman-Sayed70/HOG-SVM-ImageClassifier/assets/99830416/25235865-47f3-44dc-a403-58b528c3a35a)
![image_0002](https://github.com/Abdelrhman-Sayed70/HOG-SVM-ImageClassifier/assets/99830416/ce4a0a50-4403-4f4e-b58b-f91d2b695718)

# Workflow
- **We have 2 dataset training and testing datasets.**
- **First we need to go the path of the training images**
- **Get each image & Extract features from it using Histogram of Oriented Gradients [HOG]**
- **Map each image to its class. Folder name is class of the image**
- **Now we have features (_extracted using HOG)_ and target for each image.**
- **Create SVM model & train it using training dataset we created.**
- **Create Testing dataset in the same way you create training dataset.**
- **Finally test the model using testing dataset**
