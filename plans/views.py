from django.shortcuts import render,get_object_or_404, redirect
from .models import Plan, Booking
from .forms import BookingForm
from django.core import mail
from django.utils import timezone

# Create your views here.

def plan_list(request):
    plan = Plan.objects.all()
    context = {
        'plans': plan
    }

    return render(request, 'plan/plans.html', context)


def plan_detail(request, plan_id, plan_title, plan_price):
    plans = get_object_or_404(Plan, id=plan_id)
    price = plans.price
    if request.method == 'POST':
        form = BookingForm(plan_title, plan_price, request.POST or None)
        if form.is_valid():
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            phone = request.POST['phone']
            price = plans.price
            plan = plans.title
            price_str = str(plans.price)
            plan_str = str(plans.title)
            form.save()

            message1 = (
                'Congratulations',
                'thank you for booking  a place with us' + plan_str + 'your price is  '  + price_str + ' please call in to make your payment',
                'maduabuchiokonkwo@village.ng',
            [email]
            )
            message2=(
                'a new signup',
                'a new client' + first_name + " " + last_name + " just signed up please call then on " + phone,
                'maduabuchiokonkwo@village.ng',
                ['maduabuchiokonkwo@gmail.com']
            )

            mail.send_mass_mail((message1, message2), fail_silently=False)
            return redirect('index')
    else:
        form = BookingForm(plan_title, plan_price)
    
    context = {
        'plan': plans,
        'form': form
    }

    return render(request, 'plan/plan_detail.html', context)



def expired_plan():
    bookings = Booking.objects.filter(isExpired=True)
    emails = bookings.email.all()
    







