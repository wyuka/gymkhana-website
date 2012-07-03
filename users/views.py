from users.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def login(request):
    try:
        uname = request.POST['username']
        passwd = request.POST['password']
        u = User.objects.get(username=uname, password=passwd)
        request.session['logged_in'] = True
        request.session['uid'] = u.id
        return HttpResponseRedirect('/')
    except (KeyError, User.DoesNotExist, User.MultipleObjectsReturned):
        return HttpResponseRedirect('/?loginerr=true')

def logout(request):
    try:
        del request.session['logged_in']
        del request.session['uid']
    except KeyError:
        pass
    return HttpResponseRedirect('/?logoutsuccess=true')

def about(request):
    c = Context({
        'logged_in': request.session.get('logged_in', False),
        'user': User.objects.get(id=1),
    })
    c.update(csrf(request))

    return render_to_response("about.html", c)

def profile(request):
    c = Context({
        'logged_in': request.session.get('logged_in', False),
        'user': User.objects.get(id=1),
    })
    c.update(csrf(request))
    return HttpResponse("haha")#render_to_response("profile.html", c)