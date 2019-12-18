from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import cv2                                      #cascade classifier training
import numpy as np
from os import listdir                          # fetching data from directory
from os.path import isfile, join
from datetime import datetime 
from . import forms
from django.views.generic import TemplateView
from registration.models import user
# Create your views here.
class LoginPage(TemplateView):
    template = 'login.html'
    def post(self, request):
        form = forms.Registration(request.POST)
        if request.method == 'POST' and form.is_valid():
            username = form.cleaned_data['username']
            u1 = user.objects.filter(username = username)
            if u1:
                login = init(username)
                print(login)
                if login == 0:
                    return redirect('Success')
                else:
                    return HttpResponse('No Login')
            else:
                return HttpResponse('NoUserExists')
    def get(self, request):
        form = forms.Registration()
        return render(request, self.template, {'form': form})
    
def LogoutPage(request):
    template = loader.get_template('logout.html') 
    return HttpResponse(template.render())

def Success(request):
    template = loader.get_template('trans.html')
    return HttpResponse(template.render())


def init(username):
    login = 1
    data_path ='C:/Users/Anu Nema/Downloads/facedetection/' + username + '/'
    print(data_path)
    onlyfiles =[f for f in listdir(data_path) if isfile(join(data_path,f))]

    Training_Data, Labels = [],[]
    for i, files in enumerate(onlyfiles):
        image_path =data_path + onlyfiles[i]
        images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images,dtype=np.uint8))
        Labels.append(i)

    Labels=np.asarray(Labels,dtype=np.int32)

    model=cv2.face.LBPHFaceRecognizer_create() #linear binary phase histogram face recognizier


    model.train(np.asarray(Training_Data),np.asarray(Labels))

    print("model training complete")

    face_classifier=cv2.CascadeClassifier('C:/Users/Anu Nema/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    def face_detector(img,size= 0.5):
        gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)

        if faces is():
            return img,[]
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h,x:x+w]
            roi=cv2.resize(roi,(200,200))

        return img,roi

    cap =cv2.VideoCapture(0)

    ret, frame=cap.read()

    image,face =face_detector(frame)

    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result= model.predict(face)

        if result[1]<500:
            confidence=int(100*(1-(result[1])/300))
            display_string=str(confidence)+'% Confidence it is user'
        cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)



        if confidence>85:
            login = 0
            cv2.putText(image,"unlock",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(image, "lock",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    except:
            cv2.putText(image,"face not found",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0, 0), 2)
            pass
    cap.release()
    cv2.destroyAllWindows()
    return login