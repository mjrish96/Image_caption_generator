from flask import Flask, request, redirect, render_template

import generate_caption

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    if request.method =='POST':
        
        f = request.files['userfile']
        path = "/home/rish/Downloads/Image-Caption/static/{}".format(f.filename)
        f.save(path)
       
        caption = generate_caption.caption_this_image(path)
       
        result_dec = {
            'image':path,
            'caption':caption
        }
            
        
    return render_template('index.html', your_result = result_dec)

if __name__ == "__main__":
    app.run(debug=True)