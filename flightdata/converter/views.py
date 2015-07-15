from django.http import StreamingHttpResponse
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

import os.path
import mimetypes
import subprocess

def converter(request):
    newfile = None
    if request.method == 'POST':
        response_filepath = 'files/flightdata.kml'
        response_filename = os.path.basename(response_filepath)
        chunksize = 8192

        # UploadedFile instance
        csvfile = request.FILES['file']

        csv_filepath = 'files/input.csv'

        with open(csv_filepath, 'w') as f:
            f.write(csvfile.read())
        
        subprocess.call(['../usr/bin/flight2kml', csv_filepath, response_filepath])

        response = StreamingHttpResponse(
            FileWrapper(open(response_filepath), chunksize),
            content_type=mimetypes.guess_type(response_filepath)[0]
        )
        response['Content-Length'] = os.path.getsize(response_filepath)
        response['Content-Disposition'] = 'attachment; filename=%s' % response_filename 
        return response
 
    context = {'file': newfile}

    return render(request, 'converter/converter.html', context)
