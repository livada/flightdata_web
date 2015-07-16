#from mod_python import apache

import os.path
import subprocess

basedir = os.path.dirname(__file__)

def index(req):
    response_filepath = os.path.join(basedir, 'files/flightdata.kml')
    response_filename = os.path.basename(response_filepath)

    # UploadedFile instance
    csvfile = req.form['file']
    csv_filepath = os.path.join(basedir, 'files/input.csv')

    # Test if the file was uploaded
    if csvfile.filename:
        with open(csv_filepath, 'w') as f:
            f.write(csvfile.file.read())

        subprocess.call([os.path.join(basedir, 'usr/bin/flight2kml'), csv_filepath, response_filepath])

        req.sendfile(response_filepath)

