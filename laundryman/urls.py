
from django.contrib import admin
from django.urls import path, include
from orders import views
from django.views.generic import TemplateView

from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path(('users/'), include('users.urls')),

    path('orders-list/', views.OrdersList, name = "orders-list"),
    path('orders-detail/<str:pk>', views.OrdersDetail, name = "orders-detail"),
    path('orders-create/', views.OrdersCreate, name = "orders-create"),
    path('orders-update/<str:pk>', views.OrdersUpdate, name = "orders-update"),
    path('orders-delete/<str:pk>/', views.OrdersDelete, name = "orders-delete"),

    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path("djangoflutterwave/", include("djangoflutterwave.urls", namespace="djangoflutterwave"))
]
