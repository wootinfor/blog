from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list),
    path("login/", views.LoginFormView.as_view()),
    path('logout/',views.logout),
    path('upload/<int:article_id>',views.upload_file),
    path('upload/success/',views.success_upload),
    path('article/<int:article_id>',views.content),
    path('download/<int:file_id>',views.download)
]
