from django.shortcuts import render,redirect
from collage_management_app.models import Staff,Staff_Notification

def HOME(request):

    return render(request,'staff/home.html')


def NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for staff in staff:
        staff_id = staff.id
        notifications = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {'notifications':notifications}
    return render(request,'staff/notification.html', context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id =status)
    notification.status = 1
    notification.save()
    return redirect('notification')