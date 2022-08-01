from django.urls import path, re_path

from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView
from . import views



urlpatterns = [
	path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

     path('orders-list/', views.UserOrdersList, name = "user-orders-list"),
     path('orders-detail/<str:pk>', views.UserOrdersDetail, name = "orders-detail"),
     path('orders-update/<str:pk>', views.UserOrdersUpdate, name = "orders-update"),
     path('profile/', views.ProfileView, name = "user-profile"),


    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
]