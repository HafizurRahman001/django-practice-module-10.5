from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    data = {'name':'hafiz','age':20,'date':datetime.datetime.now(),'profession':'', 'sentence':"hello guys whats up", 'lst':['a','b','c'], 'course':[
        {
            'id':1,
            'name':'python'
        },
        {
            'id':2,
            'name':'Javascript'
        },
        {
            'id':3,
            'name':'Django'
        },
    ]}
    return render(req,"first_app/home.html",data)