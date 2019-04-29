# Image thumbinail generation functione Example for OpenFaaS 
Simple OpenFaaS Python function for generating a thumbnail of an image that user submits though a typical HTTP (multipart/form-data) form. Uses Python Pillow image processing library. 

## Assumptions:
Content-Type of the input: multipart/form-data

Form field name, which contains the image data: pic

Location of the OpenFaaS deployment: localhost:8080

## Building the function using OpenFaas CLI:
```faas-cli build  --build-option dev --build-option pillow -f ./thumbnail.yml```

## Deploying the function using OpenFaas CLI:
```faas-cli deploy -f ./thumbnail.yml```

## Function REST enpoint:
http://localhost:8080/function/thumbnail

### HTML form for sending image to the function
```
<html>
  <body>
   <form method="post" enctype="multipart/form-data" action="http://localhost:8080/function/thumbnail">
      <input type="file" name="pic" accept="image/*">
      <input id="saveForm" type="submit" name="submit" value="Generate thumbnail" />
    </form>	
  </body>
</html>
```
