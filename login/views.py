from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def index(request):
    return render(request, 'login/index.html')
   

def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_name'] = username
                    message = '欢迎'
                    return redirect('/index/')
                else:
                    message = '密码错误！'
            except:
                message = '用户不存在！请联系工作人员'
        return render(request, 'login/login.html', locals())
    
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")