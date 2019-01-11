from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name='result'),
    path('valve', views.valve, name='valve'),
    path('contact_', views.contact, name='contact_'),
    path('shipping', views.shipping, name='shipping'),
    path('shipping_arrangement', views.shipping_arrangement, name='shipping_arrangement'),
    path('deliver', views.deliver, name='deliver'),
    path('summary', views.summary, name='summary'),
    path('terms', views.terms, name='terms'),
    path('testing', views.testing, name='testing'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('download', views.download, name='download'),
]

