from django.shortcuts import render,redirect
from .models import Course,Description
from django.contrib import messages

def index(request):
    try:
        x = Course.objects.all()
    except:
        x = ''
    context = {
        'courses':x,
    }
    # if not "error" in request.session:
    #     request.session['error']=[]
    return render(request,'course_app/index.html',context)

def process(request):
    if request.method != 'POST':
        return redirect('/')

    res={
    'name': request.POST['name'],
    'description': request.POST['description'],
    }
    result = Course.coursemanager.validate(res)
    if 'error' in result:
        messages.error(request, result['error'])
    else:
        messages.success(request, 'Successfully added user')
    return render(request,'course_app/index.html')

        #
        #
        # if result[0]:
        #     return redirect ('/')
        #
        # else: #result[0] is false
        #     messages.error(request, result[1])
        #     return redirect ('/')
        #

def remove(request,id):
    x = Course.objects.get(id=id)
    context={
        'course':x
    }
    return render(request,'course_app/removed.html',context)

def destroy(request,id):
    Course.objects.get(id=id).delete()
    return redirect ('/')
