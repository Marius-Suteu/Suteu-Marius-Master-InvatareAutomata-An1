\# MNIST Digit Recognition with Tkinter Interface



Acest proiect antreneaza un model simplu de recunoastere a cifrelor MNIST folosind TensorFlow/Keras si ofera o interfata grafica (Tkinter) pentru desenarea unei cifre si prezicerea acesteia.



\## Functionalitati



1\. \*\*Incarcare si preprocesare MNIST\*\*  

&nbsp;  - Normalizeaza imaginile intre 0 si 1  

&nbsp;  - One-hot encoding pentru etichete



2\. \*\*Model Keras\*\*

&nbsp;  - Input: imagine 28x28 flatten

&nbsp;  - 2 straturi Dense (128 si 64 unitati, activare ReLU)

&nbsp;  - Strat final Dense 10 unitati (softmax)

&nbsp;  - Compilare: `optimizer='adam'`, `loss='categorical\_crossentropy'`, `metrics=\['accuracy']`



3\. \*\*Antrenare\*\*

&nbsp;  - Epoci: 10

&nbsp;  - Batch size: 32

&nbsp;  - Validation split: 0.1



4\. \*\*Evaluare\*\*

&nbsp;  - Se afiseaza acuratetea pe setul de test



5\. \*\*Interfata Tkinter\*\*

&nbsp;  - Canvas pentru desenarea cifrei (280x280 px)

&nbsp;  - Buton \*\*Predict\*\* pentru prezicerea cifrei desenate

&nbsp;  - Buton \*\*Clear\*\* pentru resetarea canvasului

&nbsp;  - Cifra desenata este redimensionata si centrata la 28x28 px

&nbsp;  - Imaginea este inversata si normalizata pentru model



\## Cerinte



\- Python 3.8+

\- TensorFlow

\- Pillow (PIL)

\- NumPy

\- Tkinter (inclus in Python standard)

\- Optional: pip install `requirements.txt`



\## Utilizare



1\. Cloneaza repository-ul:

```bash

git clone https://github.com/Marius-Suteu/Suteu-Marius-Master-IvatareAautomata-An1-NLP.git



