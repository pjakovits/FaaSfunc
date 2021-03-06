# Thumbnail generation function example for IBM cloud functions (OpenWhisk)
Simple IBM cloud Python function for generating a thumbnail of an image that user submits though a typical HTTP (multipart/form-data) form. Uses Python Pillow image processing library. 

## Assumptions:
Content-Type of the input: multipart/form-data

Function runtime is Python 3.6.6

Form field name, which contains the image data: pic

Function Action has been exposed as a Web Action

IBM_FUNCTION_ENDPOINT does not end with .json (e.g https://eu-gb.functions.cloud.ibm.com/api/v1/web/jakovits_zone/default/thumbnail)

## Installation
Function can be created and deployed through IBM Cloud Functions web interface at https://cloud.ibm.com/openwhisk/

## HTML form for sending image to the function
```
<html>
  <body>
   <form method="post" enctype="multipart/form-data" action="IBM_FUNCTION_ENDPOINT">
      <input type="file" name="pic" accept="image/*">
      <input id="saveForm" type="submit" name="submit" value="Send message" />
    </form>	
  </body>
</html>
```

IBM_FUNCTION_ENDPOINT needs to be replaced with an actual  Function endpoint generated by IBM cloud (e.g https://eu-gb.functions.cloud.ibm.com/api/v1/web/jakovits_zone/default/thumbnail)

NB! IBM_FUNCTION_ENDPOINT must not end with ".json"
