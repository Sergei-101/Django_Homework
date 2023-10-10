from django.urls import path

from .views import user_form, many_fields_form, many_fields_form_widjet, add_user, upload_image

urlpatterns = [
 path('user_form/', user_form, name='user_form'),
 path('many_fields_form/', many_fields_form, name='many_fields_form'),
 path('many_fields_form_widget/', many_fields_form_widjet, name='many_fields_form_widjet'),
 path('add_user/', add_user, name='add_user'),
 path('upload/', upload_image, name='upload_image'),

]