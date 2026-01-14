\# Image Classification with CNN and Tkinter Interface

!!!!EXERCITIUL CNN_ImageRecognition!!!!

Acest proiect antreneaza un model CNN pentru clasificarea imaginilor si ofera o interfata grafica pentru incarcarea unei imagini si prezicerea clasei acesteia.



\## Functionalitati



1\. \*\*Curatare dataset\*\*

&nbsp;  - Verifica toate imaginile din folderul `dataset`

&nbsp;  - Sterge fisiere corupte



2\. \*\*Setari antrenament\*\*

&nbsp;  - Dimensiune imagine: 150x150

&nbsp;  - Batch size: 32

&nbsp;  - Epoci: 5

&nbsp;  - Augmentare date: rotatie, translatie, zoom, flip, luminozitate



3\. \*\*Model CNN\*\*

&nbsp;  - Straturi convolutive + max pooling

&nbsp;  - Strat dens final + dropout

&nbsp;  - Output: strat softmax pentru clasificare multi-clasa



4\. \*\*Compilare\*\*

&nbsp;  - Optimizer: `adam`

&nbsp;  - Loss: `categorical\_crossentropy`

&nbsp;  - Metrici: `accuracy`



5\. \*\*EarlyStopping\*\*

&nbsp;  - Monitorizare `val\_loss`

&nbsp;  - Patience: 7 epoci

&nbsp;  - Restabilire cele mai bune greutati



6\. \*\*Antrenare\*\*

&nbsp;  - Se antreneaza pe setul de antrenament

&nbsp;  - Se valideaza pe subsetul de validare



7\. \*\*Evaluare\*\*

&nbsp;  - Se afiseaza acuratete finala pe setul de validare



8\. \*\*Salvare model si clase\*\*

&nbsp;  - Model salvat: `image\_classifier.keras`

&nbsp;  - Mapping clase: `classes.json`



9\. \*\*Interfata Tkinter\*\*

&nbsp;  - Incarcare imagine (`Load Image`)

&nbsp;  - Prezicere (`Predict`)

&nbsp;  - Afisare probabilitati sub forma de grafic

&nbsp;  - Dimensiune fereastra: 800x600



\## Cerinte



\- Python 3.8+

\- TensorFlow

\- Pillow

\- NumPy

\- Matplotlib

\- Tkinter (inclus in Python standard)

!!!!**EXERCITIUL InvatareSupervizataCifre**!!!!
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

git clone https://github.com/Marius-Suteu/Suteu-Marius-Master-IvatareAutomata-An1-NLP.git



