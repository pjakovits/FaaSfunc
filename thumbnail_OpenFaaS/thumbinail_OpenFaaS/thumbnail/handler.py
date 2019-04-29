from PIL import Image
import cgi
import io
import os


def handle(param):
    # Fetch the HTTP request body from the function input.
    bin_data = param
    bin_length = len(bin_data)

    # Convert it into a binary stream
    bin_stream = io.BytesIO(bin_data)

    # Fetch the content-type together with multipart boundary separator value from the Header
    # OpenFaaS passes HTTP header values through the environment
    input_content_type = os.getenv("Http_Content_Type")

    # Parse the multi party form data using cgi FieldStorage library
    form = cgi.FieldStorage(fp=bin_stream, environ={'REQUEST_METHOD': 'POST', 'CONTENT_LENGTH': bin_length,
                                                    'CONTENT_TYPE': input_content_type})

    # Extract the image data from HTML 'pic' input field
    dat = form["pic"]
    bytestream = dat.file.read()

    # Initiate the PILLOW library image object using the image binary stream
    image = Image.open(io.BytesIO(bytestream))

    # Apply image processing command
    image.thumbnail((128,128))

    # Save the result into as a byte array
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='PNG')
    imgByteArrValue = imgByteArr.getvalue()

    # Return the json result.
    # NB! Output content-type must be defined top be image/* (image/png) in the function.yaml file under environment
    return imgByteArrValue

