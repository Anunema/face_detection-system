from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from . import forms
from django.views.generic import TemplateView
import cv2
import numpy as np
import os
from . import models
# Create your views here.
def registrationPage(request):
    template = loader.get_template('registration.html') 
    return HttpResponse(template.render())

class Register(TemplateView):
    template = 'registration.html'

    def post(self, request):
        form = forms.Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
        success = init(username)
        if success == 0:
            return redirect('/auth/login/')
        args = {'form': form, 'username': username}
        return render(request, self.template, args)

    def get(self, request):
        form = forms.Registration()
        return render(request, self.template, {'form': form})
    
def init(username):
    face_classifier=cv2.CascadeClassifier('C:/Users/Anu Nema/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    os.mkdir('C:/Users/Anu Nema/Downloads/facedetection/'+username)
    def face_extractor(img):

        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)


        if faces is():
            return None

        for(x,y,w,h) in faces:
            cropped_face=img[y:y+h,x:x+w]

        return cropped_face


    cap=cv2.VideoCapture(0)
    count=0


    while True:
        ret,frame=cap.read()
        if face_extractor(frame) is not None:
            count+=1
            face=cv2.resize(face_extractor(frame),(200,200))
            face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

            file_name_path='C:/Users/Anu Nema/Downloads/facedetection/'+username+'/'+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)

            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
        else:
            print("Face not Found")
        pass

        if cv2.waitKey(1)==13 or count==100:
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0
    print('Collecting samples complete!!!')
    