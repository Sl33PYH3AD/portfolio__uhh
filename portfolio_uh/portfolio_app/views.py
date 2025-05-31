from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import UserInformation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def index(request):
    try:
        context = { 'username' : request.user.username }
        return render(request, 'portfolio_uh/index3.html', context)         
    except AttributeError as e:
        return render(request, 'portfolio_uh/index3.html')


def feedback(request):
    if request.method == 'POST':
        user_info = request.POST.get('user-info')
        platform_select = request.POST.get('platform-select')
        print(user_info)

        if user_info:
            user = UserInformation(nickname=user_info, send_date=timezone.now(), platform=platform_select)
            user.save()
            print(f"Получен email/nickname: {user_info}")
            return JsonResponse({'status': 'success', 'message': 'Email/nickname получен'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Email/nickname не получен'})
        
            
    return render(request, 'portfolio_uh/index3.html')

# @
# def auth(request):
#     body = json.loads(request.body)
#     # print(body)
#     if body["type"] == "registration":
#         if database.check_login(body["login"]) == True:
#             return HttpResponse(Json.dumps({'error':'User already exist'}))
#         database.add_user(body["name"], body["login"], body["password"])
#         request.session[body["login"]] = body["password"]
#         return HttpResponse(json.dumps({"redirect_url": url+"?profile"+body["login"]}))
# from django.contrib import admin


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('test1')
            login(request, user)
            print(f'login: {username}, password: {password}')
            return JsonResponse({'status': 'error', 'message': 'OK'})
        else:
            print('test2')
            return JsonResponse({'status': 'error', 'message': 'Неверный логин и пароль'})
    return render(request, 'portfolio_uh/auth.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')

        # создаётся пользователь

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)

    return render(request, 'portfolio_uh/reg.html')

def acc(request):
    try:
        context = {
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'username' : request.user.username,
            'email' : request.user.email,
            'date_joined' : request.user.data_joined
        }
        return render(request, 'portfolio_uh/acc.html', context)
    except AttributeError as e:
        return render(request, 'portfolio_uh/acc.html')
    
def works(request):
        try:
            context = { 'username' : request.user.username }
            return render(request, 'portfolio_uh/works.html', context)         
        except AttributeError as e:
            return render(request, 'portfolio_uh/works.html')