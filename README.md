# HOG-SVM-ImageClassifier
**The HOG-SVM Image Classifier is a technique used for image recognition and object detection. To create a model, you collect a dataset and use HOG to extract features from images. These features are fed into the SVM algorithm to train the model. The trained model can classify new images. Testing involves using a separate set of images to evaluate the model's accuracy. The HOG-SVM Image Classifier is a powerful technique for accurately recognizing objects in a wide range of scenarios.**

# Workflow
- **We have 2 dataset training and testing datasets.**
- **First we need to go the path of the training images**
- **Get each image & Extract features from it using Histogram of Oriented Gradients [HOG]**
- **Map each image to its class. Folder name is class of the image**
- **Now we have features (_extracted using HOG)_ and target for each image.**
- **Create SVM model & train it using training dataset we created.**
- **Create Testing dataset in the same way you create training dataset.**
- **Finally test the model using testing dataset**
