from django.shortcuts import render
from .models import User
from django import forms
from django.http import JsonResponse



# Create your views here.
from .forms import StudentRegistration

def home(request):
    form=StudentRegistration()
    stud = User.objects.all()
    return render(request,'myapp/home.html',{'form':form,'stu':stud})


def save_data(request):
    if request.method == "POST" :
        form=StudentRegistration(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            Book_name=request.POST['Book_name']
            available_stock=request.POST['available_stock']
            writter=request.POST['writter']
            if(sid==""): 
              usr=User(Book_name=Book_name, available_stock = available_stock, writter = writter)
            else:
                usr=User(id=sid ,Book_name=Book_name, available_stock = available_stock, writter = writter)
            usr.save_data()
            stud=User.objects.values()
            student_data=list(stud)
            return JsonResponse({'status':'save' , 'student_data':student_data})
        else:
            JsonResponse({'status':0})
    
    
def delete_data(request):
    if request.method == "POST" :
        id =request.POST.get('sid')
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else :
        return JsonResponse({'status':0})
    
    
def edit_data(request):
    if request.method == "POST" :
        id =request.POST.get('sid')
        book=User.objects.get(pk=id)
        book_data={"id":book.id,"  Book_name":book.Book_name, 
            "available_stock":book.available_stock ,"writter":book.writter}   
        return JsonResponse(book_data) 
    