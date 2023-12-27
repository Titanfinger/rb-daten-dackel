from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.expanduser('~/webserver/static/Bilder')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
                return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/slideshow')
def slideshow():
    image_names = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('slideshow.html', image_names=image_names)

if __name__ == '__main__':
    app.run(debug=True)

