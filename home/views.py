from django.shortcuts import render

# Create your views here.
from Posts.models import Posts, PostCot
from django.core.mail import EmailMessage

def home(request):
    cat_res = PostCot.objects.get(name="Results")
    resposts = Posts.objects.filter(title=cat_res).order_by('-id')[:5]

    cat_job = PostCot.objects.get(name="Latest Jobs")
    jobposts = Posts.objects.filter(title=cat_job).order_by('-id')[:5]

    cat_admtcard = PostCot.objects.get(name="Admit Card")
    jobadmtcards = Posts.objects.filter(title=cat_admtcard).order_by('-id')[:5]
    context = {
        'resposts': resposts,
        'jobposts': jobposts,
        'jobadmtcards': jobadmtcards,
    }
    return render(request, 'home.html', context)


def about(request):

    return render(request, 'about.html')

from .contactform import ContactForm
from django.core.mail import send_mail
from .models import ContactDetail
from django.contrib import messages
def contacts(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name =form.cleaned_data.get('name')
        email =form.cleaned_data.get('email')
        message =form.cleaned_data.get('message')
        print(name,email,message)
        cdata =f"Name:{name}message:{message}Email:{email}"

        # res =send_mail('my firt mail', cdata, 'rajdemo2022@gmail.com', [email,'raj.django@gmail.com'])
        res=0
        print('done')
        messages.add_message(request, messages.INFO, 'Mail successfuly send .')


        if res==1:
            ContactDetail.objects.create(name=name,email=email,me=message)
            print('mail send')

    data ={
        'form':form
    }
    return render(request, 'contacts.html',data)


def details(reqeust, slug=None):
    post = Posts.objects.get(slug=slug)

    data = {
        'post': post
    }
    return render(reqeust, 'details.html', data)


def result_page(request):
    cat_res = PostCot.objects.get(name="Results")
    resposts = Posts.objects.filter(title=cat_res)
    context = {
        'resposts': resposts
    }

    return render(request, 'resultpage.html', context)
