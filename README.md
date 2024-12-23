# Image Classifier GUI

This project is a graphical user interface (GUI) for an image classification model. It uses a pre-trained model to predict the class of an input image. The application is built with Taipy GUI and TensorFlow.

## Features
- Allows users to upload an image from their file system.
- Displays the uploaded image and predicts its class.
- Shows the prediction confidence as a progress indicator.
- Uses a pre-trained deep learning model (`baseline_mariya.keras`) for classification.

## Requirements
- Python 3.8 or later
- Required Python libraries:
  - `taipy-gui`
  - `tensorflow`
  - `numpy`
  - `Pillow`
- Download all the requirements dependencies from `requirements.txt`

## Installation
1. Clone this repository or download the `classifier.py` script and necessary files.
2. Ensure the following files are in the same directory as the script:
   - `baseline_mariya.keras`: Pre-trained model file.
   - `logo.png`: Logo image displayed in the GUI.
   - `placeholder_image.png`: Placeholder image displayed initially.
3. Install the required Python libraries:
   ```bash
   pip install taipy-gui tensorflow numpy pillow

## How to Run
1. Navigate to the project directory in your terminal.
2. Run the application:
    ```bash
    python classifier.py
3. Open your browser and navigate to the local server URL displayed in the terminal (e.g., http://127.0.0.1:5000).

## File Structure
- classifier.py: Main application script.
- baseline_mariya.keras: Pretrained imageclassification model.
- logo.png: Logo displayed in the application.
- placeholder_image.png: Default placeholderimage.

## Prediction Logic
1. Input Preprocessing:
    - Converts the uploaded image to RGB format.
    - Resizes the image to 32x32 pixels.
    - Normalizes pixel values to [0, 1].

2. Model Prediction:
    - Feeds the preprocessed image into the model.
    - Outputs prediction probabilities for each class.

3. Result Display:
    - Finds the class with the highest probability.
    - Displays the predicted class and the confidence score.

## License
This project is licensed under the MIT License.

## Credit
- Neural Pattern from: freepik.com
- Brain Icon from: flaticon.com
- Github: MariyaSha