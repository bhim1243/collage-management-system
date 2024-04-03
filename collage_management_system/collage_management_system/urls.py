"""
URL configuration for collage_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, student_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.base_view, name='base'),
                  path('', views.LOGIN, name='login'),
                  path('dologin', views.dologin, name='dologin'),
                  path('dologout', views.dologout, name='logout'),

                  # this is profile
                  path('profile', views.PROFILE, name='profile'),
                  path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  # this is HOD panel url
                  path('HOD/Home', hod_views.HOME, name='hod_home'),
                  path('Hod/student/add', hod_views.ADD_STUDENT, name='add_student'),
                  path('hod/student/view', hod_views.VIEW_STUDENT, name='view_student'),
                  path('hod/student/edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
                  path('hod/student/update/', hod_views.UPDATE_STUDENT, name='update_student'),
                  path('hod/student/delete/<str:admin>', hod_views.DELETE_STUDENT, name='delete_student'),

                  # this is staff panel
                  path('hod/staff/add', hod_views.ADD_STAFF, name='add_staff'),
                  path('hod/staff/view', hod_views.VIEW_STAFF, name='view_staff'),
                  path('hod/staff/edit/<str:id>', hod_views.EDIT_STAFF, name='edit_staff'),
                  path('hod/staff/update/', hod_views.UPDATE_STAFF, name='update_staff'),
                  path('hod/staff/delete/<str:admin>', hod_views.DELETE_STAFF, name='delete_staff'),

                  path('hod/course/add', hod_views.ADD_COURSE, name='add_course'),
                  path('hod/course/view', hod_views.VIEW_COURSE, name='view_course'),
                  path('hod/course/edit/<str:id>', hod_views.EDIT_COURSE, name='edit_course'),
                  path('hod/course/update', hod_views.UPDATE_COURSE, name='update_course'),
                  path('hod/course/delete/<str:id>', hod_views.DELETE_COURSE, name='delete_course'),

                  path('hod/subject/add', hod_views.ADD_SUBJECT, name='add_subject'),
                  path('hod/subject/view', hod_views.VIEW_SUBJECT, name='view_subject'),
                  path('hod/subject/edit/<str:id>', hod_views.EDIT_SUBJECT, name='edit_subject'),
                  path('hod/subject/update', hod_views.UPDATE_SUBJECT, name='update_subject'),
                  path('hod/subject/delete/<str:id>', hod_views.DELETE_SUBJECT, name='delete_subject'),

                  path('hod/session/add', hod_views.ADD_SESSION, name='add_session'),
                  path('hod/session/view', hod_views.VIEW_SESSION, name='view_session'),
                  path('hod/session/edit/<str:id>', hod_views.EDIT_SESSION, name='edit_session'),
                  path('hod/session/update', hod_views.UPDATE_SESSION, name='update_session'),
                  path('hod/session/delete/<str:id>', hod_views.DELETE_SESSION, name='delete_session'),
                  path('hod/staff/send_notification', hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
                  path('hod/staff/save_notification', hod_views.SAVE_STAFF_NOTIFICATION, name='save_staff_notification'),


                   # this is HOD panel url

                   path('staff/home',staff_views.HOME,name='staff_home'),
                   path('staff/notification',staff_views.NOTIFICATION,name='notification'),
                   path('staff/mark_as_done/<str:status>', staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),

                  path('staff/apply_leave', staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),











              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
