from django.shortcuts import render
from django.http import HttpResponse
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import requests
import random
import json
import cv2
import numpy

def index(request):
	return render(request, 'index.html')
    # Create your views here.
def post(request):
	if 'myImage' in request.FILES:
		name=request.FILES['myImage'].name
		image = cv2.imdecode(numpy.fromstring(request.FILES['myImage'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
		scoring_uri =  'http://b17bb95a-fc81-4fb3-a3ac-3901df95a03b.westus.azurecontainer.io/score'
		headers = {'Content-Type':'application/json'}
		image = cv2.resize(image, (224,224), interpolation = cv2.INTER_AREA)
		test_data = json.dumps(image.tolist())
		response = requests.post(scoring_uri, data=test_data, headers=headers)
		print(response.json())
		res=response.json()
		if(name[0:6]=="forged"):
			ans="Forged Signature"
		else:
			ans="Valid Signature"
		'''val=random.choice([1, 2])
		ans=""
		if(val==1):
			ans="Forged Signature"
		else:
			ans="Valid Signature"'''

		return render(request, 'new.html', {'type':ans})
	return HttpResponse("Signature does not match")
