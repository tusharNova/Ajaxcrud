from django.shortcuts import render
from .forms import UserRegistertions
from .models import infodata
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = UserRegistertions()
    users = infodata.objects.all().values
    return render(request , 'enroll/home.html' , { 'form' : form , 'users' : users})

def saveUser(request):
    if request.method == 'POST':
        form = UserRegistertions(request.POST)
        if form.is_valid():
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if id == "":
                urs = infodata(name = name , email = email , password = password)
            else:
                urs = infodata(id = id ,name = name , email = email , password = password)
            urs.save()
            users = infodata.objects.values()
            print(users)
            userlist = list(users) 
            return JsonResponse({'status' : 'Save' , 'userlist' : userlist})
        else:
            return JsonResponse({'status' : 'Fail'})
    return render( request , 'home')


def deleteUser(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        urs  = infodata.objects.get(pk=id)
        urs.delete()
        return JsonResponse({ 'status' : 1})
    else:
        return JsonResponse({ 'status' : 0})


def editUser(request):
    if request.method == "POST":
        uid = request.POST.get('sid')
        print(uid)
        usr = infodata.objects.get(pk=uid)
        data = {"name" : usr.name , "email" : usr.email , "password" : usr.password}
        return JsonResponse(data)
    else:
        return JsonResponse({ 'data' : 0})
