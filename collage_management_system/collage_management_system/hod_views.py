from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from collage_management_app.models import Course, Session_year, CustomUser, Student,Staff,Subject,Staff_Notification,Staff_Leave
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all() .count()
    course_count = Course.objects.all().count
    subject_count = Subject.objects.all().count

    student_gender_male = Student.objects.filter(gender='male').count()
    student_gender_female = Student.objects.filter(gender='female').count()


    context= {
        'student_count':student_count,
        'staff_count': staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,

    }


    return render(request, 'hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    courses = Course.objects.all()  # Corrected variable name
    session_years = Session_year.objects.all()  # Corrected variable name

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        # Check if username is provided
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_year.objects.get(id=session_year_id)

            # Create Student instance
            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request,user.first_name + "   " + user.last_name + "are successfully added ! ")
            return redirect('add_student')

    context = {
        'courses': courses,
        'session_years': session_years,
    }
    return render(request, 'hod/add_student.html', context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    students = Student.objects.all()  # Retrieve all instances of Student
    context = {
        'students': students,  # Rename 'student' to 'students' for clarity
    }
    return render(request, 'hod/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id).first()
    courses = Course.objects.all()
    session_years =Session_year.objects.all()

    context = {
        'student': student,
        'courses': courses,
        'session_years':session_years,
    }

    return render(request, 'hod/edit_student.html', context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user. username= username



        if password !=None and password != "":
         user.set_password(password)
        if profile_pic !=None and profile_pic != "":
         user.profile_pic =profile_pic

        user.save()

        student =Student.objects.get(admin = student_id)
        student.address =address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student .course_id = course

        session_year = Session_year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record Are Successfully update !')
        return redirect('view_student')


    return render(request,'hod/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Record Are Successfully Delete !')
    return redirect('view_student')

@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        course = Course(name=course_name)
        course.save()
        messages.success(request, 'Course Are Successfully Created !')
        return redirect('add_course')

    return render(request,'hod/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request,'hod/view_course.html', context)

@login_required(login_url='/')
def EDIT_COURSE(request ,id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }

    return  render(request,'hod/edit_course.html',  context)
@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        course.name = name  # Update the 'name' attribute, not 'course_name'
        course.save()
        messages.success(request, 'Course Successfully Updated!')
        return redirect('view_course')

@login_required(login_url='/')
def DELETE_COURSE( request,id):
   course = Course.objects.get(id=id)
   course.delete()
   messages.success(request, 'Course Successfully Delete!')
   return redirect('view_course')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken!')
            return redirect('add_staff')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken!')
            return redirect('add_staff')

        else:
            user = CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                user_type=2,
            )
            user.set_password(password)
            user.save()
            staff = Staff(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.success(request, ' Staff Are  Successfully Added!')
            return redirect('add_staff')
    return render(request,'hod/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }
    return render(request,'hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
 staff = Staff.objects.get(id=id)
 context = {
     'staff': staff,
 }
 return render(request,'hod/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name= first_name
        user.last_name = last_name
        user.email=email

        if password !=None and password != "":
           user.set_password(password)
        if profile_pic !=None and profile_pic != "":
           user.profile_pic =profile_pic

        user.save()

        staff =  Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address= address
        staff.save()
        messages.success(request,'Staff is Successfully update')
        return redirect('view_staff')
    return redirect('hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Staff Successfully Delete!')
    return redirect('view_staff')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    courses =Course.objects.all()
    staffs =Staff.objects.all()

    if request.method =='POST':
        subject_name =request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff =Staff.objects.get( id =staff_id)

        subject =Subject(
            name =subject_name,
            course = course,
            staff =staff
        )

        subject.save()
        messages.success(request,'Subject Are Successfully Added !')
        return redirect('add_subject')
    context ={
        'courses':courses,
        'staffs':staffs,
    }

    return render(request,'hod/add_subject.html',context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
   subjects = Subject.objects.all()

   context ={
      'subjects': subjects
   }
   return render(request, 'hod/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)

    courses = Course.objects.all()
    staffs = Staff.objects.all()

    context = {
        'subject': subject,
        'courses': courses,
        'staffs': staffs
    }


    return render(request,'hod/edit_subject.html', context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
   if request.method == 'POST':
      subject_id = request.POST.get('subject_id')
      subject_name = request.POST.get('subject_name')
      course_id = request.POST.get('course_id')
      staff_id = request.POST.get ('staff_id')

      course = Course.objects.get(id= course_id)
      staff = Staff.objects.get(id =staff_id)

      subject =Subject(
         id =subject_id,
         name = subject_name,
         course = course,
         staff = staff,
       )
      subject.save()
      messages.success(request ,'Subject Are Successfully Updated')
      return redirect('view_subject')


@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Subject Are Successfully Delete !')

    return redirect('view_subject')

@login_required(login_url='/')
def ADD_SESSION(request):
     if request.method == 'POST':
         session_year_start =request.POST.get('session_year_start')
         session_year_end  = request.POST.get('session_year_end')
         session =Session_year(
             session_start=session_year_start,
             session_end = session_year_end,
         )
         session.save()
         messages.success(request, 'Session Are Successfully Created !')
         return  redirect('add_session')
     return render(request,'hod/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):

    sessions =Session_year.objects.all()
    context={
         'sessions':sessions,
     }
    return render(request ,'hod/view_session.html' ,context)

@login_required(login_url='/')
def EDIT_SESSION(request, id):
    sessions= Session_year.objects.get(id=id)
    context = {'sessions': sessions,}
    return render(request, 'hod/edit_session.html', context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method =='POST':
        session_id = request.POST.get('session_id')
        session_year_start =request.POST.get('session_year_start')
        session_year_end  =request.POST.get('session_year_end')

        session =Session_year(
            id= session_id,
            session_start =session_year_start,
            session_end =session_year_end,

        )
        session.save()
        messages.success(request,'Session Are Successfully Update ! ')

    return redirect('view_session')

@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session =Session_year.objects.get(id=id)
    session.delete()
    messages.success(request, 'Session Are Successfully Delete ! ')
    return  redirect('view_session')

@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')
    context ={
         'staff':staff,
        'see_notification':see_notification,
     }
    return render(request,'hod/staff_notification.html',context)

@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        massage = request.POST.get('massage')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            massage=massage,  # Corrected 'massage' to 'message'
        )
        notification.save()
        messages.success(request, 'Notification Are Successfully Send !')
        return redirect('staff_send_notification')

@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()


    context ={
        'staff_leave':staff_leave,
    }

    return render(request,'hod/staff_leave_view.html',context)

@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id =id)
    leave.status =1
    leave.save()

    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()

    return redirect('staff_leave_view')