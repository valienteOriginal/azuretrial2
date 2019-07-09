from django.shortcuts import render
from django.http import HttpResponse
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import requests
import json
import cv2

def index(request):
    return render(request, 'index.html')
# Create your views here.
def post(request):
	if 'myImage' in request.FILES:
    	image = request.FILES['myImage']
        scoring_uri =  'http://b17bb95a-fc81-4fb3-a3ac-3901df95a03b.westus.azurecontainer.io/score'
        headers = {'Content-Type':'application/json'}
        image = cv2.resize(image, (224,224), interpolation = inter)
		image = img_to_array(image)
		test_data = json.dumps(image.tolist())
		response = requests.post(scoring_uri, data=test_data, headers=headers)
		print(response.json())
		res=response.json()
        return render(request, 'new.html', {'type':res['type']})
    return HttpResponse("Signature does not match")
