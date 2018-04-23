from django.conf.urls import url
from mail import views

app_name = 'mail'
urlpatterns = [
  # The home view ('/mail/')
  url(r'^$', views.home, name='home'),
  # Explicit home ('/mail/home/')
  url(r'^home/$', views.home, name='home'),
  # Redirect to get token ('/mail/gettoken/')
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
  # Mail view ('/mail/mail/')
  url(r'^mail/$', views.mail, name='mail'),

  # Events view ('/tutorial/events/')
  url(r'^events/$', views.events, name='events'),

  # Contacts view ('/tutorial/contacts/')
  url(r'^contacts/$', views.contacts, name='contacts'),
]
