import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt


model = MobileNetV2(weights='imagenet')


img_path = "/home/salma/Pictures/notebook.png"  


img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Make prediction
predictions = model.predict(img_array)
decoded_predictions = decode_predictions(predictions, top=3)[0]

# Display image
plt.imshow(image.load_img(img_path))
plt.axis('off')
plt.show()

# Print results
print("Recognition Results:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i+1}. {label}: {score*100:.2f}%")
