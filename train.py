from tensorflow import keras


def run():
    dataset = keras.preprocessing.image_dataset_from_directory(
        './cats/', batch_size=64, image_size=(500, 500)
    )

    # For demonstration, iterate over the batches yielded by the dataset.
    for data, labels in dataset:
        print(data.shape)  # (64, 200, 200, 3)
        print(data.dtype)  # float32
        print(labels.shape)  # (64,)
        print(labels.dtype)  # int32


if __name__ == '__main__':
    run()
