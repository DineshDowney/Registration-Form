from django.shortcuts import render
from AppOne.forms import FormClass2,FormClass1
from AppOne.models import AccessRec

# Create your views here.

def index(request):
    name_list=AccessRec.objects.order_by('RollNumber')
    name_dict={"Access_Records":name_list}
    return render(request,"records.html",context=name_dict)

def FormFunc(request):
    FormObj2=FormClass2()
    FormObj1=FormClass1()
    if request.method=='POST':
        FormObj2=FormClass2(request.POST)
        if FormObj2.is_valid():
            FormObj2.save(commit=True)
            #return FormFunc(request)
        FormObj1=FormClass1(request.POST)
        if FormObj1.is_valid():
            FormObj1.save(commit=True)
            
    context={"FormKey2":FormObj2,"FormKey1":FormObj1}   #"Name":Name,"Roll Number":RollNumber
    return render(request,"page1.html",context)