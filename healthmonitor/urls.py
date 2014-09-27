from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'healthmonitor.weight.views.home', name='home'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login',
        {'template_name': 'core/login.html'},
        name='login')
)
