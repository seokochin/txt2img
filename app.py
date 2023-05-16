import torch
import torchvision
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from flask import Flask, request, render_template

app = Flask(__name__)
model_id = "stabilityai/stable-diffusion-2"

# Use the Euler scheduler here instead
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    prompt = request.form['sentence']
    image = pipe(prompt).images[0]
    image.save("output/output.png")
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
