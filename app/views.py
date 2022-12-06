from django.shortcuts import render
from .models import myemployee

# Create your views here.
def index(request):
    return render(request,"index.html")

def create(request):
    emp_dict={}
    try:
        name=request.POST['fname']
        address=request.POST['fadd']
        emplist=myemployee(ename=name,eadd=address)
        emplist.save()
        emp_dict['message']="employee successfully added"
        return render(request,"index.html",emp_dict)

    except Exception as e:
        print(e)
        emp_dict['message']="employee not added"
        return render(request,"index.html",emp_dict)

def read(request):
    empd=myemployee.objects.all()
    return render(request,"index.html",{'empkey':empd})

def delete(request):
    try:
        name2=request.POST['delname']
        emp1=myemployee.objects.filter(ename=name2)
        emp1.delete()
        return render(request,"index.html",{'msg1':'data deleted successfully'})
    
    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg1':'data not deleted'})

def update(request):
    try:
        old=request.POST['oldname']
        new=request.POST['newname']
        myemployee.objects.filter(ename=old).update(ename=new)
        ad1=request.POST['oldad']
        ad2=request.POST['newad']
        myemployee.objects.filter(eadd=ad1).update(eadd=ad2)
        return render(request,"index.html",{'ms2':'the data updated successfully'})
    except Exception as e:
        print(e)
        return render(request,"index.html",{'ms2':'the data not updated'})

