import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data/",
    labels="inferred",
    label_mode="categorical",
    color_mode="grayscale",
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset="training",
    seed=123,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data/",
    labels="inferred",
    label_mode="categorical",
    color_mode="grayscale",
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset="validation",
    seed=123,
)

# Define the model
model = keras.Sequential([
    layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(7, activation="softmax"),
])


model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)


model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)


test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data/",
    labels="inferred",
    label_mode="categorical",
    color_mode="grayscale",
    batch_size=32,
    image_size=(256, 256),
    seed=123,
)
model.evaluate(test_ds)

#  HDF5 file
model.save("xray_classification_model.h5")