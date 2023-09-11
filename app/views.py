from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import *
# Create your views here.

def Lib(request):
    LLO= LibraryForms()
    d={'LLO':LLO}
    if request.method=='POST':
        LLEP= LibraryForms(request.POST)

        if LLEP.is_valid():
            BookName= LLEP.cleaned_data['BookName']
            Author_Name= LLEP.cleaned_data['Author_name']
            Mail= LLEP.cleaned_data['Mail']
            Publish= LLEP.cleaned_data['Publish']

            LB= Library.objects.get_or_create(Book= BookName, Author= Author_Name, Gmail= Mail, Date= Publish)[0]
            LB.save()
        else:
            return HttpResponse('Invalid')
    return render(request, 'insert_lib.html', context= d)