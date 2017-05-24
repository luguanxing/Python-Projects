import urllib.request as request;
response = request.urlopen("http://placekitten.com/g/500/500");
cat_img = response.read();
with open("cat_img.jpg", "wb") as file:
    file.write(cat_img);