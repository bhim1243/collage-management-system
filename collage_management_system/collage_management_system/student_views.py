from django.shortcuts import render,redirect
from collage_management_app.models import Student_Notification,Student,Student_Feedback,Student_Leave
from django.contrib import messages
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


def STUDENT_FEEDBACLK(request):
    student_id = Student.objects.get(admin =request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id = student_id)
    context ={
        'feedback_history':feedback_history,
    }

    return render(request,'student/feedback.html',context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        student = Student.objects.get(admin=request.user.id)
        feedback = request.POST.get('feedback')
        feedback = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",

        )
        feedback.save()

    return redirect('student_feedback')


def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id= student)

    context = {
        'student_leave_history': student_leave_history
    }

    return render(request,'student/apply_leave.html',context)


def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student = Student.objects.get(admin=request.user.id)
        leave = Student_Leave(
            student_id=student,
            date=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Send')
    return redirect('student_apply_leave')