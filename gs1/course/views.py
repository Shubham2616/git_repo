from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ("Home page")

def learn_d(request):
    return HttpResponse("<h1> Hello Django </h1")

def learn_p(request):
    return HttpResponse("<h2> Hello Python </h2>")

def learn_a(request):
    a = 10 + 10
    return HttpResponse(a)
    
def learn_f(request):
    a = "Shubham"
    return HttpResponse(f"String Formating : {a}")

def learn_s(request):
    my_list = [{'id':101, 'name':'Shubham'},{'id':102, 'name':'vipul'}]
    my_list = [{'name':i['name'] } for i in my_list]
    print(my_list)