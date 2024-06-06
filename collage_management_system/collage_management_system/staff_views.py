from django.shortcuts import render,redirect
from collage_management_app.models import Staff,Staff_Notification,Staff_Leave,Staff_Feedback,Subject,Session_year,Student,Attendance,Attendance_Report
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


def STAFF_FEEDBACLK(request):
    staff_id = Staff.objects.get(admin= request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

    context ={
        'feedback_history':feedback_history,
    }
    return render(request,'staff/staff_feedback.html',context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)
        feedback = Staff_Feedback(
           staff_id= staff,
           feedback =feedback,
           feedback_reply ="",

        )
        feedback.save()

    return redirect('staff_feedback')


def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff_id)
    session_years = Session_year.objects.all()
    action = request.GET.get('action')

    get_subject =None
    get_session_year= None
    students= None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id= subject_id)
            get_session_year = Session_year.objects.get(id = session_year_id)
            students= Subject.objects.filter(id = subject_id)
            for subject in subjects:
                student_id= subject.course.id
                students = Student.objects.filter(course_id = student_id)

    context = {
        'subjects': subjects,
        'session_years': session_years,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
         'action':action,
        'students':students,
    }
    return render(request, 'staff/take_attendance.html', context)


def STAFF_SAVE_ATTENDANCE(request):
    if request.method== "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        Attendance_date = request.POST.get('Attendance_date')
        student_id = request.POST.get('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_year.objects.get(id=session_year_id)

        attendance= Attendance(
            subject_id =get_subject,
            Attendance_date = Attendance_date,
            session_year_id = get_session_year

        )
        attendance.save()

        for student_id in student_id:

            int_student_id = int(student_id)

            p_students = Student.objects.get(id=int_student_id)
            print(p_students)
            attendance_report = Attendance_Report(
                    student_id=p_students,
                    Attendance_id=attendance
                )
            attendance_report.save()

    return redirect('staff_take_attendance')