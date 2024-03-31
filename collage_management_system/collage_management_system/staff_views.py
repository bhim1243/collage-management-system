from django.shortcuts import render,redirect
from collage_management_app.models import Staff,Staff_Notification

def HOME(request):

    return render(request,'staff/home.html')


def NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for staff in staff:
        staff_id = staff.id
        notification = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {
            'notification': notification
        }
    return render(request, 'staff/notification.html',context)
