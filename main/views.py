from django.shortcuts import render
from django.http import HttpRequest
from main.models import Pic, User, Comment
import random

# Create your views here.
def index(request):
    if 'logged_in_as' in request.COOKIES:
        u = User.objects.filter(username=request.COOKIES['logged_in_as'])
        if (u.__len__() > 0):
            if (u[0].settings_to_discover):
                return discover(request)
        else:
            return render(request, 'nfound.html', None)
    return render(request, 'hello.html', None)

def discover(request):
    i = random.randrange(0, Pic.objects.all().__len__())
    return perma(request, i)

def perma(request, intt):
    i = int(intt)
    if i < 0 or i >= Pic.objects.all().__len__():
        return render(request, 'nentry.html', None)
    context = {
        'c': Pic.objects.all()[i],
        'i': i,
        'host': request.get_host() + '/perma/' + str(i)
    }
    if 'comment' in request.POST:
        if request.POST['comment'] == '':
            return render(request, 'ncomment.html', None)
        Comment.objects.create(
            author = request.COOKIES['logged_in_as'],
            i = int(request.POST['i']),
            comment = request.POST['comment']
        )
    comments = []
    for c in Comment.objects.all():
        if (int(c.i) == i):
            comments.append(c)
    context['comments'] = comments
    if 'logged_in_as' in request.COOKIES:
        context['logged_in_as'] = request.COOKIES['logged_in_as']
    return render(request, 'discover.html', context)

def reg(request):
    usr = request.POST['usr']
    pwd = request.POST['pwd']
    User.objects.create(
        username = usr,
        password = pwd,
        desc = 'Hello!'
    )

    return render(request, 'regdone.html', {'usr': usr, 'pwd': pwd})

def auth(request):
    context = {}
    if 'logged_in_as' in request.COOKIES:
        context['logged_in_as'] = request.COOKIES['logged_in_as']
    if 'usr' not in request.POST or 'pwd' not in request.POST:
        return render(request, 'login.html', context)
    else:
        usr = request.POST['usr']
        pwd = request.POST['pwd']
        
        scookies = {}

        context['success'] = False
        
        exist = False
        for c in User.objects.all():
            if (c.username == usr):
                # Attempt login 
                if (c.password == pwd):
                    # Login success 
                    scookies['logged_in_as'] = usr
                    context['success'] = True
                else:
                    # Login failure 
                    pass
                exist = True
                break
        
        if (not exist):
            # Register 
            return reg(request)
        
        response = render(request, 'login.html', context)
        for key in scookies.keys():
            response.set_cookie(key, scookies[key])
        return response

def new(request):
    if 'logged_in_as' in request.COOKIES:
        return render(request, 'new.html', {'usr': request.COOKIES['logged_in_as']})
    else:
        return render(request, 'nlogged.html', None)

def upload(request):
    if 'name' not in request.POST or 'desc' not in request.POST or 'f' not in request.FILES:
        return render(request, 'ncomplete.html', None)
    Pic.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc'],
        f = request.FILES['f'],
        author = request.COOKIES['logged_in_as']
    )
    con = {
        'usr': request.COOKIES['logged_in_as'],
    }
    return render(request, 'supload.html', con)

def users(request, uname):
    for c in User.objects.all():
        if (c.username == uname):
            if (c.settings_priv):
                return render(request, 'nallowed.html', None)
            return render(request, 'user.html', { 'q': c })
    return render(request, 'nfound.html', { 'usr': uname })

def u_settings(request):
    if 'logged_in_as' not in request.COOKIES:
        return render(request, 'nlogged.html', None)
    con = {}
    if 'pwd' in request.POST and 'desc' in request.POST and 'usr' in request.POST:
        u = User.objects.filter(username=request.POST['usr'])
        if (u.__len__() <= 0):
            return render(request, 'nfound.html', None)
        u.update(password=request.POST['pwd'])
        u.update(desc=request.POST['desc'])
        u.update(settings_to_discover=('rtd' in request.POST))
        u.update(settings_priv=('priv' in request.POST))
        
        con['msuccess'] = True
    for c in User.objects.all():
        if (c.username == request.COOKIES['logged_in_as']):
            con['c'] = c
            return render(request, 'settings.html', con)
    return render(request, 'nlogged.html', None)

def nexist(request):
    return render(request, 'nexist.html', None)

def logout(request):
    if 'logged_in_as' in request.COOKIES:
        response = render(request, 'slogout.html', None)
        response.delete_cookie('logged_in_as')
    else:
        response = render(request, 'nlogout.html', None)
    return response
