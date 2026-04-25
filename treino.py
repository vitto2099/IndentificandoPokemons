import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_dados = os.path.join(diretorio_atual, 'Pokemons')

gerador_dados = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True,
    zoom_range=0.3,
    validation_split=0.2 
)

base_treinamento = gerador_dados.flow_from_directory(
    caminho_dados,
    target_size=(64, 64),
    batch_size=8,
    class_mode='categorical',
    subset='training'
)

base_teste = gerador_dados.flow_from_directory(
    caminho_dados,
    target_size=(64, 64),
    batch_size=8,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

rede_neural = Sequential([
    Conv2D(32, (3,3), input_shape=(64, 64, 3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    
    Flatten(),
    Dense(units=128, activation='relu'),
    Dropout(0.2),
    Dense(units=10, activation='softmax')
])

rede_neural.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

rede_neural.fit(base_treinamento, epochs=50, validation_data=base_teste)

rede_neural.save('pokemon.h5')