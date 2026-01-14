import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("image_classifier.h5")

with open("classes.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

IMG_SIZE = (64, 64)

def load_image():
    global img_path, img_display
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img = img.resize((250, 250))
        img_display = ImageTk.PhotoImage(img)
        image_label.config(image=img_display)

def predict_image():
    img = Image.open(img_path).resize(IMG_SIZE)
    img = np.array(img) / 255.0
    if img.shape[-1] == 4:
        img = img[:, :, :3]
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)[0]
    predicted_class = class_names[np.argmax(predictions)]
    result_label.config(text=f"Predictie: {predicted_class}")
    
    # Grafic probabilitati
    plt.figure()
    plt.bar(class_names, predictions)
    plt.title("Probabilitati")
    plt.xticks(rotation=45)
    plt.show()

root = tk.Tk()
root.title("Recunoastere imagini CNN")
root.geometry("800x600")

image_label = tk.Label(root)
image_label.pack()

tk.Button(root, text="Load Image", command=load_image).pack(pady=5)
tk.Button(root, text="Predict", command=predict_image).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
