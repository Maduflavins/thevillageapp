from plans.models import Booking
from django.core import mail
import datetime as DT
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def notify_user():
    bookings = Booking.objects.all()
    now = DT.datetime.now()
    expire_date = bookings.expiresDate
    support = 'booking@village.ng'
    if((DT.datetime.combine(expire_date, DT.time(0)) - DT.datetime.combine(now, DT.time(0))).days == 0):
        for booking in bookings:
            name = booking.firstname + " " + booking.lastname
            email = booking.email
            phone = booking.phone
            plan = booking.plan
            message1 = (
                    'Booking Expired',
                    'Dear ' + name + ' your plan, ' + plan + ' with us at thevillage just expired. You can reach us immediately at 07089996339 for to renew',
                    'booking@village.ng',
                    [email]
                )

            message2 = (
                'Expired plan',
                'Please call ' + name + ' at ' + phone + ' their plan ' + plan + ' has expired',
                'booking@village.ng',
                ['maduabuchiokonkwo@gmail.com']
            )
            mail.send_mass_mail((message1, message2), fail_silently=False)
sched.start()

            

        




