import tensorflow as tf

# путь к старой .h5 модели
h5_path = "converted_keras/keras_model.h5"
# путь для новой модели
keras_path = "converted_keras/keras_model_fixed.keras"

# загружаем модель
model = tf.keras.models.load_model(h5_path, compile=False)

# сохраняем в новый формат .keras
model.save(keras_path)
print(f"Модель успешно сохранена в {keras_path}")