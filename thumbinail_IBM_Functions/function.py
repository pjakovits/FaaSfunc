# main() will be run when you invoke this action
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
# @return The output of this action, which must be a JSON object.

import sys
from PIL import Image
from io import BytesIO
import base64
import cgi
import io

def main(param):
  #Fetch the HTTP request body from the function input. 
  request_body = param["__ow_body"]
  
  #decode the base64 encoded body object and convert it into a binary stream
  bin_data = base64.b64decode(request_body)
  bin_length = len(bin_data)
  bin_stream = io.BytesIO(bin_data)

  #Parse the multi party form data using cgi library
  form = cgi.FieldStorage(fp=bin_stream,  environ={'REQUEST_METHOD':'POST', 'CONTENT_LENGTH': bin_length, 'CONTENT_TYPE': param["__ow_headers"]["content-type"]})
  
  #Extract the image data from HTML 'pic' input field
  dat = form["pic"]
  bytes = dat.file.read()
  
  #Initiate the PILLOW library image object using the image binary stream
  image = Image.open(io.BytesIO(bytes))
  
  #Apply image processing command
  roiImg = image.rotate(45)
 
  #Save the result into as a byte array
  imgByteArr = io.BytesIO()
  roiImg.save(imgByteArr, format='PNG')
  
  #encode the binary array as base64
  imgByteArrValue = imgByteArr.getvalue()
  out = base64.b64encode(imgByteArrValue)
  
  #Return the json result, defining the output content type to be an image.
  #Openwhisk supports automatically converting the resulting JSON document into corresponding (based on content type) HTTP response.  
  return {
    "headers": {
      "Content-Type": "image/png"
    },
    "statusCode": 200,
    "body": out
  }
