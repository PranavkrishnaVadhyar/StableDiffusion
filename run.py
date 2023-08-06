import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image
import random
from database import value


print(value())
model_inputs = {
	"prompt": value(),
	"num_inference_steps":50,
	"guidance_scale":9,
	"height":512,
	"width":512,
	"seed": random.randint(0, 1000000)
}

api_key = "<API_KEY>"
model_key = "<MODEL_KEY>"

# Run the mode
out = banana.run(api_key, model_key, model_inputs)

# Extract the image and save to output.jpg
image_byte_string = out["modelOutputs"][0]["image_base64"]
image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")
