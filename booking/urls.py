from django.urls import path
from .views import (
    HomeView, RegisterView, LoginView, LogoutView, 
    ShowListAdminView,ShowCreateView, ShowEditView, ShowDeleteView,
    ShowListView, ShowBookView, BookingHistoryView,
    CancelBookingView ,MakePaymentView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/shows/', ShowListAdminView.as_view(), name='admin-show-list'),
    path('admin/shows/add/', ShowCreateView.as_view(), name='admin-show-add'),
    path('admin/shows/<int:pk>/edit/', ShowEditView.as_view(), name='admin-show-edit'),
    path('admin/shows/<int:pk>/delete/', ShowDeleteView.as_view(), name='admin-show-delete'),
    path('shows/', ShowListView.as_view(), name='show-list'),
    path('shows/<int:pk>/book/', ShowBookView.as_view(), name='show-book'),
    path('bookings/', BookingHistoryView.as_view(), name='booking-history'),
    path('bookings/<int:pk>/cancel/', CancelBookingView.as_view(), name='cancel-booking'),
    path('bookings/<int:pk>/pay/', MakePaymentView.as_view(), name='make-payment'),
]