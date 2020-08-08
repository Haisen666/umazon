from django.urls import path
from . import views
import contact.views


app_name = 'contact'

urlpatterns = [
        path('contact_form/', views.contact_form, name='contact_form'),  # フォーム
        path('contact_form/contact/complete/', views.complete, name='complete'),  # 完了画面
]