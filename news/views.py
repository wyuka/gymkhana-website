from news.models import News
from users.models import User
from django.http import HttpResponse
from django.template import Context
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import math

def index(request):
    loginerr = False
    logoutsuccess = False
    if request.GET.get("loginerr","false") == "true":
        loginerr = True
    if request.GET.get("logoutsuccess","false") == "true":
        logoutsuccess = True
    full_news_list = News.objects.all().order_by('-published_date')
    oldest_page =  math.ceil(len(full_news_list) / 6.0)

    user = None
    logged_in = request.session.get('logged_in', False)
    oldest_page_newsboard = 0
    if logged_in:
        user = User.objects.get(id=request.session.get('uid',0))
        oldest_page_newsboard = math.ceil(len(user.pinned_news.all()) / 6.0)

    c = Context({
        'loginerr': loginerr,
        'logoutsuccess': logoutsuccess,
        'logged_in': request.session.get('logged_in', False),
        'user': user,
        'oldest_page_mostrecent': oldest_page,
        'oldest_page_mostviewed': oldest_page,
        'oldest_page_newsboard': oldest_page_newsboard,
        'sidebarnews': full_news_list[:12],
    })
    c.update(csrf(request))

    return render_to_response("news.html", c)

def newspage(request):
    page = 1
    try:
        page = int(request.GET.get("page","1"))
    except ValueError:
        pass
    user = None
    logged_in = request.session.get('logged_in', False)
    if logged_in:
        user = User.objects.get(id=request.session.get('uid',0))

    newsorder = 'mostrecent'
    blanknewsboard = False
    try:
        newsorder = request.GET.get("newsorder", "mostrecent")
    except ValueError:
        pass
    full_news_list = []
    if newsorder == 'mostrecent':
        full_news_list = News.objects.all().order_by('-published_date')
    elif newsorder == 'mostviewed':
        full_news_list = News.objects.all().order_by('-views')
    elif newsorder == 'newsboard':
        if user != None:
            full_news_list = user.pinned_news.all().order_by('-published_date')
        else:
            blanknewsboard = True

    news_list = full_news_list[(page-1)*6:(page-1)*6 + 6]

    c = Context({
        'news_list': news_list,
        'logged_in': request.session.get('logged_in', False),
        'user': user,
        'page_no': page,
        'blanknewsboard': blanknewsboard,
    })
    return render_to_response("newspage.html",c)

def newsmodal(request):
    newsid = int(request.GET.get("newsid",0))
    wrongid = False
    if newsid == 0:
        wrongid = True
        news = None
    else:
        try:
            news = News.objects.get(id = newsid)
            news.views += 1
            news.save()
        except News.DoesNotExist:
            wrongid = True
            news = None

    user = None
    logged_in = request.session.get('logged_in', False)
    if logged_in:
        user = User.objects.get(id=request.session.get('uid',0))

    already_added = False
    if user != None and news != None:
        try:
            n = user.pinned_news.get(id = news.id)
            already_added = True
        except:
            pass

    c = Context({
        'news': news,
        'wrongid': wrongid,
        'logged_in': request.session.get('logged_in', False),
        'user': user,
        'already_added': already_added,
    })
    return render_to_response("newsmodal.html",c)

def pintoprofile(request):
    if (request.session.get('logged_in', False) == True):
        user = User.objects.get(id = request.session.get('uid',0))
        newsid = request.GET['newsid']
        user.pinned_news.add(News.objects.get(id=newsid))
        user.save()
    return HttpResponse("")

def unpinfromprofile(request):
    if (request.session.get('logged_in', False) == True):
        user = User.objects.get(id = request.session.get('uid',0))
        newsid = request.GET['newsid']
        user.pinned_news.remove(News.objects.get(id=newsid))
        user.save()
    return HttpResponse("")