import requests
import os
import shutil

if not os.path.exists("femme"):
    os.mkdir("femme")
if not os.path.exists("homme"):
    os.mkdir("homme")
def random_pic_generator():
    req = requests.get('https://fakeface.rest/face/json?minimum_age=18')
    url =req.json()['image_url']
    filename = url.split('/')[-1]
    if "female" in url:
        rq = requests.get(url, stream=True)
        with open("femme/"+filename, 'wb') as f:
            shutil.copyfileobj(rq.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        rq = requests.get(url, stream=True)
        with open("homme/" + filename, 'wb') as f:
            shutil.copyfileobj(rq.raw, f)
        print('Image sucessfully Downloaded: ', filename)



for i in range(100):
    random_pic_generator()
