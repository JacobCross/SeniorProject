from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import posts
from forms import dataform
from django.core.context_processors import csrf
from django.template import RequestContext



# Create your views here.
def home(request):
    posts1 = posts.objects.all()[:10]
    return render_to_response('index.html', {'posts' : posts1})

def form(request):
    return render_to_response('form.html')

def newform(request):
    return render(request,'newform.html')

def thanks(request):
    return render('thanks.html')

def submit_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dataform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            b = RequestContext(request, form)
            f_name = form.cleaned_data['fname']
            l_name = form.cleaned_data['lname']
            _school = form.cleaned_data['school']
            row = dataform(fname='f_name',l_name='l_name',school='_school')
            row.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks.html')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = dataform()
    params = {}
    params.update(csrf(request))
    return render(request,'thanks.html', params)
    #Learn Django's Template Language, and implement
    #return render_to_response(request,)

def newformv2(request):
    return render_to_response('newformv2.txt')


