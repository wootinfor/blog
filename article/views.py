import django
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
import article
from article.forms import LoginForm
from article.models import Users,Article,ModelWithFileField
from django.shortcuts import render
from django.views import View
from django.urls import path
from django.contrib.auth import authenticate,login,logout as django_logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import StreamingHttpResponse

@login_required
def article_list(request):
    articles=Article.objects.all()
    newarticles=Article.objects.order_by("-publish_date")
    return render(request,'articles_list.html',{'articles':newarticles})

class LoginFormView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',{'form':LoginForm()})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            # email=form.cleaned_data['password']
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/article/')
            else:
                messages.add_message(request,messages.WARNING,'用户名密码不对')
        return render(request,'login.html',{'form':form})

    #         return HttpResponse(f'用户名:{username},邮箱:{email}')
    #     else:
    #         return render(request,'login.html',{'form':form})
    # pass

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/article/login')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request,article_id):
    id=article_id
    ig=article_id
    ig=str(ig)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            art=Article.objects.all()[article_id-1]
            instance = ModelWithFileField(file_field=request.FILES['file'],article_id=art)
            instance.save()
            url='/article/article/'+ig
            return HttpResponseRedirect(url)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form,'id':id})

def success_upload(request):
    html=f'<html><body>成功</body></html>'
    return HttpResponseRedirect('/article')
    # return HttpResponse(html)

def content(request,article_id):
    articles=Article.objects.all()
    # files=ModelWithFileField.objects.all()
    files=[]
    for file in ModelWithFileField.objects.all():
        if file.article_id==articles[article_id-1]:
            files.append(file)
    article_id=article_id-1
    article=articles[article_id]
    title=article.title
    content=article.content
    user=article.user
    publish_date=article.publish_date
    id=article.id
    return render(request,'content.html',{'title':title,'content':content,'user':user,'publish_date':publish_date,'id':id,'files':files,})

def download(request,file_id):
    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break
    file_id=file_id-1            
    file_path = ModelWithFileField.objects.all()[file_id].file_field.name
    response = StreamingHttpResponse(down_chunk_file_manager(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_path)
 
    return response