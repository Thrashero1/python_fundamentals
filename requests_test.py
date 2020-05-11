import requests
import simplejson as json
from io import BytesIO

# getting data through html get requests
'''params = {"q": "samsung"}
r = requests.get("https://www.theverge.com/search", params=params)
print(r.url)
print("Status:", r.status_code)

f = open("./text.html", "w+", encoding='utf-8')
f.write(r.text)
'''


# working with images
'''
r = requests.get("https://www.lifewire.com/thmb/Jir5TfpgXRt7pgL-m_9_LGnqO5o=/960x640/filters:no_upscale():max_bytes(150000):strip_icc()/png-file-photos-app-5b75972f46e0fb002c692c03.png")
p = requests.get("https://cdn.pixabay.com/photo/2018/01/12/10/19/fantasy-3077928_1280.jpg")

print("URL Status:", p.status_code)
print("Image Status:", r.status_code)

url_image = Image.open(BytesIO(p.content))
local_image = Image.open(BytesIO(r.content))

print("local:", local_image.size, local_image.format, local_image.mode)
path2 = "./local_image." + local_image.format.lower()

print("URL:", url_image.size, url_image.format, url_image.mode)
path1 = "./url_image." + url_image.format

try: url_image.save(path1, url_image.format)

except IOError:
    print("Cannot save the file")

try: local_image.save(path2, local_image.format)

except IOError:
    print(Exception)
'''

# using POST requests to post directly to the server (serverside)

'''my_data = {"name": "David Borg", "email": "test@test.om"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data= my_data)

f = open("myFile.html", "w+")
f.write(r.text)'''

# Posting Json

url = "https://api.rebrandly.com/v1/links"
data = {"destination": "https://www.youtube.com/channel/UCHK4HD0ltu1-I212icLPt3g",
        "domain": {"fullName": "rebrand.ly"}}
# need to get api key
headers = {
  "Content-type": "application/json",
  "apikey": "YOUR_API_KEY",
  "workspace": "YOUR_WORKSPACE_ID"
}
r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.status_code)
