import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from PIL import Image, ImageOps, ImageDraw
import tkinter as tk

# 1. Incarcare si preprocesare MNIST 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255.0 # normalizeaza pixelii intre 0 si 1
x_test = x_test / 255.0
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 2. Definire model
model = Sequential()                        
model.add(Flatten(input_shape=(28,28)))     
model.add(Dense(128, activation='relu'))   
model.add(Dense(64, activation='relu'))     
model.add(Dense(10, activation='softmax'))  

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # algoritm de optimizare pentru ajustarea greutatilor
#from tensorflow.keras.optimizers import Adam
#optimizer = Adam(learning_rate=0.005)  # rata de invatare 0.005
#model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Antrenare model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# 4. Evaluare model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nAcuratetea pe setul de test: {test_acc:.4f}')

# 5. Interfata Tkinter pentru desen
class DrawDigit:
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.title("Deseneaza o cifra si apasa Predict")

        self.canvas = tk.Canvas(self.root, width=280, height=280, bg='white')
        self.canvas.pack()

        self.btn_predict = tk.Button(self.root, text="Predict", command=self.predict)
        self.btn_predict.pack(side='left')

        self.btn_clear = tk.Button(self.root, text="Clear", command=self.clear)
        self.btn_clear.pack(side='right')

        self.image = Image.new("L", (280,280), color=255)  # fundal alb
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x-4), (event.y-4)  # Linie mai subtire
        x2, y2 = (event.x+4), (event.y+4)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
        self.draw.ellipse([x1, y1, x2, y2], fill=0)

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0,0,280,280], fill=255)

    def predict(self):
        # Cropam cifra desenata la zona activa
        bbox = self.image.getbbox()
        if bbox is None:
            print("Nu ai desenat nimic!")
            return
        digit = self.image.crop(bbox)

        # Redimensionam la 20x20 pastrand proportia
        digit = digit.resize((20,20), Image.Resampling.LANCZOS)

        # Cream imagine finala 28x28 si punem cifra in centru
        final_img = Image.new('L', (28,28), color=255)
        upper_left = ((28-20)//2, (28-20)//2)
        final_img.paste(digit, upper_left)

        # Invertim culorile (MNIST are fundal negru)
        final_img = ImageOps.invert(final_img)

        # Pregatim pentru model
        img_array = np.array(final_img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predictie
        predictie = self.model.predict(img_array)
        clasa = np.argmax(predictie) # returneaza cifra cu cea mai mare probabilitate
        print(f'Modelul prezice cifra: {clasa}')
        print('Probabilitati:', [f'{p:.2f}' for p in predictie[0]])

# 6. Pornire interfata
DrawDigit(model)
