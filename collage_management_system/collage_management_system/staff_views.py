from django.shortcuts import render, redirect
from collage_management_app.models import Staff, Staff_Notification, Staff_Leave, Staff_Feedback, Subject, Session_year,Student,Attendance,Attendance_Repory
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'staff/home.html')


@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for staff in staff:
        staff_id = staff.id
        notifications = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {'notifications': notifications}
    return render(request, 'staff/notification.html', context)


@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
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
        staff = Staff.objects.get(admin=request.user.id)
        leave = Staff_Leave(
            staff_id=staff,
            date=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Send')
    return redirect('staff_apply_leave')


def STAFF_FEEDBACLK(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'staff/staff_feedback.html', context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)
        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",

        )
        feedback.save()

    return redirect('staff_feedback')


def ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff_id)
    session_years = Session_year.objects.all()
    action = request.GET.get('action')

    get_session_year =None
    get_subject =None
    students =None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id =subject_id)
            get_session_year = Session_year.objects.get(id=session_year_id)
            subjects = Subject.objects.filter(id =subject_id )
            for subject in subjects:
                student_id = subject.course.id
                students = Student.objects.filter(course_id =student_id)
                print(students)
    context = {
        'subjects': subjects,
        'session_years': session_years,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'students':students,
        'action': action,

    }

    return render(request,'staff/attendance.html',context)


def ATTENDANCE_REPORT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        date = request.POST.get('date')  # Changed variable name to follow PEP8
        student_ids = request.POST.getlist('student_id')  # Changed to getlist to get all student_ids

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_year.objects.get(id=session_year_id)

        attendance= Attendance(
            subject_id=get_subject,
            date= date,
            session_year_id=get_session_year,
        )
        attendance.save()

        for student_id in student_ids:
            int_student_id = int(student_id)
            p_student = Student.objects.get(id=int_student_id)

            attendance_report = Attendance_Repory(
                student_id=p_student,
                Attendance_id= attendance
            )
            attendance_report.save()

    return redirect('staff_attendance')


def VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff_id=staff_id)
    session_years = Session_year.objects.all()
    action = request.GET.get('action')

    get_subject =None
    get_session_year =None
    date=None
    attendance_reports=None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            date = request.POST.get('date')

            get_subject = Subject.objects.get(id= subject_id)
            get_session_year = Session_year.objects.get(id=session_year_id)

            attendance = Attendance.objects.filter(subject_id=get_subject, date=date)


            for attendance in attendance:
                attendance_id = attendance.id
                attendance_reports = Attendance_Repory.objects.filter(Attendance_id=attendance_id)

    context= {
        'subjects':subjects,
        'session_years':session_years,
         'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'date':date,
        'attendance_reports':attendance_reports,
    }

    return render(request,'staff/view_attendance.html',context)


def STTAF_ADD_RESULT(request):
    staff = Staff.objects.get(admin= request.user.id)
    subjects = Subject.objects.filter(staff_id = staff)
    session_years = Session_year.objects.all()
    action = request.GET.get('action')

    get_subject =None
    get_session =None
    students= None

    if action is not None:
        if request.method == "POST":

            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id= subject_id)
            get_session = Session_year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for subject in subjects:
                student_id = subject.course.id
                students = Student.objects.filter(course_id = student_id)




    context= {
        'subjects':subjects,
        'session_years':session_years,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }
    return render(request,'staff/add_result.html',context)