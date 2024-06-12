Steps that I took to approach this task.

I used the Butterfly Classification Dataset from Kaggle from https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification.

The DNN I used for the task is ResNet 50.

Importing Necessary Libraries and Modules:
Import required libraries and modules such as numpy, pandas, seaborn, matplotlib, TensorFlow, OpenCV, etc.

Dataset Loading:
Load training and testing datasets using pandas.
Define paths for dataset folders and output folders.

Plotting the Distribution of Butterflies:
Visualize the distribution of butterfly categories using matplotlib.

Hyperparameters Definition:
Define image size, batch size, epochs, learning rate, and class names.

Data Preprocessing:
Iterate through images, resize, normalize, and append them to features and their corresponding labels to labels.

Splitting the Data:
Split the dataset into training, validation, and testing sets using train_test_split.

Base Model Setup:
Initialize ResNet50 as the base model and configure it.
Set a portion of layers as trainable.

Model Definition:
Add custom layers on top of the base model.
Define the model using the functional API of Keras.

Model Compilation:
Compile the model with Adam optimizer and sparse categorical crossentropy loss.

Training:
Train the model on the training data.
Use early stopping and model checkpointing as callbacks.

Plotting Training Loss vs Validation Loss:
Plot training and validation loss over epochs and save the plot.
Plotting Training Accuracy vs Validation Accuracy:
Plot training and validation accuracy over epochs and save the plot.

Output Evaluation:
Make predictions on the test set.
Generate a classification report and save it to a text file.