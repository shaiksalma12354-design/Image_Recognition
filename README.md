 🖼️ Image Recognition Using MobileNetV2
 
 📌 Project Overview

This project demonstrates a basic Image Recognition system using a pre-trained deep learning model, **MobileNetV2**, from TensorFlow/Keras. The model identifies objects present in an image and displays the top predictions with confidence scores.

The project is designed for beginners to understand how AI-powered image classification works without training a model from scratch.


🎯 Objective

* Implement a basic image recognition task using available AI libraries.
* Use a pre-trained model for object classification.
* Perform recognition on sample images.
* Display the prediction results clearly.

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Pillow (PIL)

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Image-Recognition-Project.git
cd Image-Recognition-Project
```

### Install Dependencies

```bash
pip install tensorflow pillow matplotlib numpy
```


## 🚀 How to Run

1. Place your image in the project folder.
2. Update the image path in the script:

```python
img_path = "sample.jpg"
```

3. Run the program:

```bash
python image_recognition.py
```

## 📸 Sample Output

```text
Recognition Results:

1. Labrador_retriever: 95.67%
2. Golden_retriever: 2.31%
3. Beagle: 0.89%
```

The image will also be displayed along with the predicted labels.


## 🧠 How It Works

1. Load the pre-trained MobileNetV2 model.
2. Resize and preprocess the input image.
3. Pass the image to the model.
4. Obtain prediction probabilities.
5. Decode and display the top predictions.


## 🔑 Key Features

* Uses a pre-trained MobileNetV2 model.
* No model training required.
* Supports recognition of thousands of object categories.
* Beginner-friendly implementation.
* Fast and efficient image classification.


## 📈 Skills Gained

* Working with pre-trained AI models
* Image preprocessing techniques
* Image classification using deep learning
* Understanding model outputs and confidence scores
* Using TensorFlow and Keras libraries



## 📜 License

This project is developed for educational and learning purposes as part of the AI Internship Program at Decode Labs.



