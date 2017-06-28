from django.conf.urls import url
from . import views

urlpatterns = [
    # Return index for empty request
       url(r'^$', views.upload, name='uplink'),
       url(r'^applicant$', views.applicant),
       url(r'^download$', views.download),
       
   ]
