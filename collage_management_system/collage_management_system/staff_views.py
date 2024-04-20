from django.shortcuts import render,redirect
from collage_management_app.models import Staff,Staff_Notification,Staff_Leave
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):

    return render(request,'staff/home.html')

@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for staff in staff:
        staff_id = staff.id
        notifications = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {'notifications':notifications}
    return render(request,'staff/notification.html', context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id =status)
    notification.status = 1
    notification.save()
    return redirect('notification')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    staff_leave_history = Staff_Leave.objects.filter(staff_id__in=[staff.id for staff in staff])

    context = {
        'staff_leave_history': staff_leave_history
    }

    return render(request, 'staff/apply_leave.html', context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin= request.user.id)
        leave = Staff_Leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request,'Leave Successfully Send')
    return redirect('staff_apply_leave')