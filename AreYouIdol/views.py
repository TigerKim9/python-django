from django.shortcuts import render, redirect
from django.contrib import messages
from .apps import AreyouidolConfig as cf
from .PreProcessing.align_faces import crop
import numpy as np
from PIL import Image
import os
from django.core.files.storage import default_storage

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def find(request):
    # 세션 관리
    if request.session.session_key == None:
        request.session['visited']=1

    print(request.session.session_key)
    sess = request.session.session_key

    if request.method == 'POST':
        
        img = request.FILES.get("img")
        
        ex = os.path.splitext(str(img))[-1].lower()

        if ex in ['.jpg', '.jpeg', '.png']:
            # 파일이름 : 세션키 + 확장자명
            file_name = sess + ex
            

            # 같은 파일의 이름(같은 세션에서 업로드한 파일)이 존재하면 삭제
            if os.path.exists(os.path.join(cf.img_path, file_name)):
                os.remove(os.path.join(cf.img_path, file_name))
            if os.path.exists(os.path.join(cf.crop_path, file_name)):
                os.remove(os.path.join(cf.crop_path, file_name))

            # 이미지 저장 경로
            img_path = default_storage.save('images/' + file_name, img)
            # print('이미지 저장 경로 => ',img_path)

            file_path = os.path.join('media',img_path)
            # file_path = os.path.abspath(img_path)
            # print('파일패스 경로 => ',file_path)

            crop(file_name)

            # 모델 예측
            model = cf.model
            crop_image = os.path.join(cf.crop_path, file_name)
            # print('모델예측 전 크롭이미지 경로 =>', crop_image)
            crop_img = Image.open(crop_image)
            crop_img = crop_img.convert('RGB')
            data = np.asarray(crop_img)
            X = np.array(data)
            X = X.astype("float") / 255
            X = X.reshape(-1, 128, 128, 3)

            pred = model.predict(X)

            messages.add_message(request, messages.SUCCESS, file_path)

            messages.add_message(request, messages.INFO, '축하드려요! 당신은 아이돌상에 가깝습니다.') if np.array(pred)[0][np.argmax(pred)] > 0.37 else messages.add_message(request, messages.INFO, '당신은 아이돌보단 다른 매력이 있을거 같네요~')

            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 '이미지(jpg, jpeg, png) 파일을 업로드 해주세요.')

            return redirect('/')
    else:
        return render(request, 'areyouidol.html')

@api_view(['POST'])
def resultIdol(request):
    # 세션 관리
    if request.session.session_key == None:
        request.session['visited']=1

    print(request.session.session_key)
    sess = request.session.session_key

    if request.method == 'POST':
        
        img = request.FILES.get("img")
        
        ex = os.path.splitext(str(img))[-1].lower()

        if ex in ['.jpg', '.jpeg', '.png']:
            # 파일이름 : 세션키 + 확장자명
            file_name = sess + ex
            

            # 같은 파일의 이름(같은 세션에서 업로드한 파일)이 존재하면 삭제
            if os.path.exists(os.path.join(cf.img_path, file_name)):
                os.remove(os.path.join(cf.img_path, file_name))
            if os.path.exists(os.path.join(cf.crop_path, file_name)):
                os.remove(os.path.join(cf.crop_path, file_name))

            # 이미지 저장 경로
            img_path = default_storage.save('images/' + file_name, img)
            # print('이미지 저장 경로 => ',img_path)

            file_path = os.path.join('media',img_path)
            # file_path = os.path.abspath(img_path)
            # print('파일패스 경로 => ',file_path)

            crop(file_name)

            # 모델 예측
            model = cf.model
            crop_image = os.path.join(cf.crop_path, file_name)
            # print('모델예측 전 크롭이미지 경로 =>', crop_image)
            crop_img = Image.open(crop_image)
            crop_img = crop_img.convert('RGB')
            data = np.asarray(crop_img)
            X = np.array(data)
            X = X.astype("float") / 255
            X = X.reshape(-1, 128, 128, 3)

            pred = model.predict(X)

            messages.add_message(request, messages.SUCCESS, file_path)

            messages.add_message(request, messages.INFO, '축하드려요! 당신은 아이돌상에 가깝습니다.') if np.array(pred)[0][np.argmax(pred)] > 0.37 else messages.add_message(request, messages.INFO, '당신은 아이돌보단 다른 매력이 있을거 같네요~')

            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 '이미지(jpg, jpeg, png) 파일을 업로드 해주세요.')

            return redirect('/')
    else:
        return render(request, 'areyouidol.html')