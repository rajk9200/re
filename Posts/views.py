from django.shortcuts import render,redirect,HttpResponse
from .forms import PostForm
from .linksdata import getResults
# Create your views here.
from .models import ResultLink
def add_post(request):
    form =PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context ={
        'form':form
    }

    return render(request, 'addpost.html',context)


def addResultsList(request):
    data =getResults()
    for mydata in data:
        for i in mydata:
            # print(i, mydata[i])
            ResultLink.objects.create(link_text=mydata[i],link_tag=i)
    return HttpResponse('data aa gya')