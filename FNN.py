import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

model = Sequential([
    Dense(4, input_dim=2, activation='relu'), 
    Dense(1, activation='sigmoid')             
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, verbose=1)

loss, accuracy = model.evaluate(X_train, y_train, verbose=0)
print(f'Loss: {loss:.4f}')
print(f'Accuracy: {accuracy:.4f}')

predictions = model.predict(X_train)
print("Predictions:")
for i, prediction in enumerate(predictions):
    print(f"Input: {X_train[i]} -> Predicted: {round(prediction[0])}")
