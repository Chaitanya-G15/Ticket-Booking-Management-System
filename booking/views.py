from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Show
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Booking


class HomeView(View):
    def get(self, request):
        shows = Show.objects.all().order_by('date', 'time')
        return render(request, 'booking/home.html', {'shows': shows})

class RegisterView(View):
    def get(self, request):
        return render(request, 'booking/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'booking/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        messages.error(request, "Invalid credentials.")
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class ShowListAdminView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        shows = Show.objects.all()
        return render(request, 'booking/show_list_admin.html', {'shows': shows})

class ShowCreateView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return render(request, 'booking/show_form.html')

    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        Show.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            time=request.POST['time'],
            available_seats=request.POST['available_seats']
        )
        return redirect('admin-show-list')

class ShowEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        show = Show.objects.get(pk=pk)
        return render(request, 'booking/show_form.html', {'show': show})

    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        show = Show.objects.get(pk=pk)
        show.title = request.POST['title']
        show.description = request.POST['description']
        show.date = request.POST['date']
        show.time = request.POST['time']
        show.available_seats = request.POST['available_seats']
        show.save()
        return redirect('admin-show-list')

class ShowDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        Show.objects.get(pk=pk).delete()
        return redirect('admin-show-list')

class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'booking/show_list.html', {'shows': shows})

class ShowBookView(LoginRequiredMixin, View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'booking/book_show.html', {'show': show})

    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        seats = int(request.POST['seats'])

        if seats <= 0 or seats > show.available_seats:
            messages.error(request, "Invalid seat number.")
            return redirect('show-book', pk=pk)

        Booking.objects.create(user=request.user, show=show, seats_booked=seats)
        show.available_seats -= seats
        show.save()

        messages.success(request, f"🎉 You booked {seats} seat(s) for {show.title}!")
        return redirect('booking-history')

class BookingHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
        for booking in bookings:
            booking.total_cost = booking.seats_booked * booking.show.ticket_price
        return render(request, 'booking/booking_history.html', {'bookings': bookings})

class CancelBookingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        booking = Booking.objects.get(pk=pk, user=request.user)
        show = booking.show
        show.available_seats += booking.seats_booked
        show.save()
        booking.delete()
        messages.success(request, "Booking cancelled successfully.")
        return redirect('booking-history')

class MakePaymentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # In real life, integrate with payment gateway
        messages.success(request, "✅ Payment successful! (Simulated)")
        return redirect('booking-history')
