# http://flask.pocoo.org/docs/patterns/fileuploads/
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','ppm'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print ('No file part')
            return redirect(request.url)
        print ("POST request", request.files)   
        file = request.files['file']
        if file and allowed_file(file.filename):
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
            # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file',
                                    filename=filename)
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''

    return "Image is compatible"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print (request.method)
    if request.method == 'GET':
        msg = "Hi!! you sent GET Req"
        return msg
    if request.method == 'POST':
        args = request.json
        print (args)
        msg = "Hi!! you sent POST Req"
        return msg

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')