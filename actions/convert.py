#from mod_python import apache

import os
import subprocess

basedir = os.path.dirname(__file__)

def index(req):
    response_filepath = os.path.join(basedir, 'cache/flightdata.kml')
    response_filename = os.path.basename(response_filepath)

    # UploadedFile instance
    csvfile = req.form['file']
    csv_filepath = os.path.join(basedir, 'cache/input.csv')

    # Clean cache dir if not empty
    if os.path.exists(csv_filepath):
        os.remove(csv_filepath)
    if os.path.exists(response_filepath):
        os.remove(response_filepath)

    # Test if the file was uploaded
    if csvfile.filename:
        with open(csv_filepath, 'w') as f:
            f.write(csvfile.file.read())

        subprocess.call([os.path.join(basedir, 'usr/bin/flight2kml'), csv_filepath, response_filepath])

        if os.path.exists(csv_filepath):
            os.remove(csv_filepath)

        if os.path.exists(response_filepath):
            req.sendfile(response_filepath)

