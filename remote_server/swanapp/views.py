from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .models import SwanTask, SwanSubTask
from django.conf import settings
import base64
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from .swanstarter import get_swan_matrixes
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoConfig
import torch
import pathlib


from rest_framework.views import APIView, Response



@csrf_exempt
def table_SWAN():
    return {
        'velocity': {
            'lower': 0,
            'upper': 30,
            'sampling_input': True,
        },
        'direction': {
            'lower': 0,
            'upper': 360,
                'sampling_input': True,
        },
        'x coordinate': {
            'lower': 0,
            'upper': 1000,
            'sampling_input': False,
        },
        'y coordinate': {
            'lower': 0,
            'upper': 1000,
                'sampling_input': False,
        },
        'target': {
            'lower': 0,
            'upper': 1000,
            'sampling_input': False,
        },
    }


@csrf_exempt
def get_matrixes(request):
    if request.method == 'GET':

        res = table_SWAN() 
        return JsonResponse(res,json_dumps_params={'ensure_ascii': False}) 

    if request.method == 'POST':
        json_data = json.loads(json.loads(request.body))
        print(json_data)
        swan_params = json_data['data']


        swan_task = SwanTask()
        swan_task.save()
        swan_task.hash = swan_task.getHash()
        swan_task.save()

        for i in swan_params.keys():
            swan_vel = swan_params[i]['velocity']
            swan_dir = swan_params[i]['direction']
            
            vel_ = swan_vel
            dir_ = swan_dir

            swan_subtask = SwanSubTask(vel=vel_, dir=dir_,swan_task=swan_task)
            swan_subtask.save()

        results = get_swan_matrixes(swan_task)

        return JsonResponse(results,json_dumps_params={'ensure_ascii': False})#{'status': 200, 'data': results}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'status': 999, 'message': 'Not valid parametrs'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def get_matrixes_with_auth(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            # NOTE: We are only support basic authentication for now.
            #
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).decode("ascii").split(':')
                user = authenticate(username=uname, password=passwd)
                if user is not None:
                    if user.is_active:
                        return get_matrixes(request)

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basci Auth Protected"
    return response


# Расчет Свана с проверкой токена
class TokenView(APIView):
    def post(self, request):
        return get_matrixes(request)

    def get(self, request):
        return JsonResponse( table_SWAN(), json_dumps_params={'ensure_ascii': False})