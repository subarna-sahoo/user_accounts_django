from django.contrib import admin
from django.urls import path, include#new2_include

from accounts import views#new1



urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home, name='home'),#new1

    path('signup/', views.signup, name='signup'),#new2
    
	path('accounts/', include('django.contrib.auth.urls')),#new3

	path('secret/', views.secret_page, name='secret'),#new4


	path('secret2/', views.SecretPage.as_view(), name='secret2'),#new5
]
