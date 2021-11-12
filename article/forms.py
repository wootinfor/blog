from os import truncate
from django import forms
from article.models import Article

class LoginForm(forms.Form):
    username=forms.CharField(
        label='姓名',
        required=True,
        min_length=1,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}),
        error_messages={
            'required':'用户名不能为空',
            'min_length':'长度不能小于1',
            'max_length':'长度不能大于10'
        }
    )
    password=forms.CharField(
        label='密码',
        required=True,
        min_length='5',
        max_length='30',
        widget=forms.PasswordInput(attrs={'class':'form-control mb-0','placeholder':'请输入密码'}),
        error_messages={
            'required':'用户名不能为空',
            'min_length':'长度不能少于5个',
            'max_length':'长度不能超过30',
        }
    )


    # email = forms.CharField(
    #     label='邮箱',
    #     required=True,
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'class':'form-control'}),
    #     error_messages={
    #         'required':'邮箱不能为空',
    #         'max_length':'长度不能大于50'
    #     }
        
    # )
    
class UploadFileForm(forms.Form):
    # id=forms.ModelMultipleChoiceField(queryset=Article.objects.all())
    file = forms.FileField()

class UserComment(forms.Form):
    text=forms.CharField(widget=forms.Textarea)