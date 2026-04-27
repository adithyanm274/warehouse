from django.urls import path
<<<<<<< HEAD
from .views import login_page, logout_page, register_page   # correct function name
=======

from .views import login_page, logout_page
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
<<<<<<< HEAD
    path('register/', register_page, name='register'),
]
=======
]
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7
