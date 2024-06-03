from django.shortcuts import render,redirect
from collage_management_app.models import Student_Notification,Student

def HOME(request):
    return render(request,'student/home.html')


def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for student in student:
        student_id = student.id
        notifications = Student_Notification.objects.filter(student_id=student_id)
        context = {
         'notifications': notifications}
    return render(request, 'student/notification.html', context )


def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()

    return redirect('student_notification')