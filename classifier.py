from taipy.gui import Gui
from tensorflow.keras import models  # Correct import
from PIL import Image
import numpy as np

class_names = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}

# Load the model
model = models.load_model("./assets/baseline_mariya.keras")

# Prediction function
def predict_image(model, path_to_img):
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    probs = model.predict(np.array([data])[:1])
    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]

    return top_prob, top_pred

# Initial content and image paths
content = ""
image_path = "./assets/images/placeholder_image.png"

prob = 0
pred = ""

# GUI Layout
index = """
<|text-center| 
<|{"./assets/images/logo.png"}|image|width=25vw|>

<|{content}|file_selector|extensions=.png|>
Select an image from your file system

<|{pred}|>

<|{image_path}|image|width=25vw|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25%|>
>
"""

# Handle changes in the file selector
def on_change(state, var_name, var_value): 
    if var_name == "content":
        top_prob, top_pred = predict_image(model, var_value)  # Call the prediction function
        state.prob = round(top_prob * 100)
        state.pred = "this is a " + top_pred
        state.image_path = var_value  # Update the image path when a new file is selected

# Run the GUI application
app = Gui(page=index)

if __name__ == '__main__':
    app.run(use_reloader=True)
