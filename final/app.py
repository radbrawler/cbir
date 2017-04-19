# http://flask.pocoo.org/docs/patterns/fileuploads/
import os, glob
import flask_search
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify, send_file, render_template
from werkzeug import secure_filename
import shutil


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','ppm'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/query', methods=['POST'])
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
            filepath = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            result_from_search = flask_search.flask_search(filepath)
            
            shutil.rmtree('query_images')
            os.mkdir('query_images')
            i = 9
            for _, res in result_from_search:
                shutil.copyfile('original1/'+ res, 'query_images/' +str(i)+ res)
                i = i-1
            # result_path = cd.function(file)
            # for browser, add 'redirect' function on top of 'url_for'
            # response = send_file(result_from_search[1])
            return jsonify(result_from_search)
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''
    return "Error in request processing"

@app.route('/')
def home_page():
    files = [os.path.basename(x) for x in glob.glob('./query_images/*.png')]
    return render_template("home.html", urls=files)

@app.route('/result/<filename>')
def uploaded_file(filename):
    return send_from_directory("query_images", filename)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print (request.method)
    if request.method == 'GET':
        var = "somethig"
        msg = "Hi!! you sent GET Req"
        return render_template('response.html', msg=msg)
    if request.method == 'POST':
        args = request.json
        print (args)
        msg = "Hi!! you sent POST Req"
        return msg

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')