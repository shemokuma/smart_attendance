"""smart_attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from Attendance import views,AdminHodView,StaffView,StudentView
#from Timetable import views
from smart_attendance_system import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.showloginPage,name="show_login"),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user,name="logout_user"),
    path('dologin',views.dologin,name="do_login"),

    path('admin_home',AdminHodView.admin_home,name="admin_home"),

    path('staff',AdminHodView.staff,name="staff"),
    path('Addstaff',AdminHodView.Addstaff,name="Addstaff"),
    path('Addstaff_save',AdminHodView.Addstaff_save,name="Addstaff_save"),
    path('Editstaff/<str:staff_id>',AdminHodView.Editstaff,name="Editstaff"),
    path('Editstaff_save',AdminHodView.Editstaff_save,name="Editstaff_save"),

    path('student',AdminHodView.student,name="student"),
    path('Addstudent',AdminHodView.Addstudent,name="Addstudent"),
    path('Addstudent_save',AdminHodView.Addstudent_save,name="Addstudent_save"),
    path('Editstudent/<str:student_id>',AdminHodView.Editstudent,name="Editstudent"),
    path('Editstudent_save',AdminHodView.Editstudent_save,name="Editstudent_save"),

    path('Department',AdminHodView.Department,name="Department"),
    path('AddDepartment',AdminHodView.AddDepartment,name="AddDepartment"),
    path('AddDepartment_save',AdminHodView.AddDepartment_save,name="AddDepartment_save"),
    path('EditDepartment/<str:department_id>',AdminHodView.EditDepartment,name="EditDepartment"),
    path('EditDepartment_save',AdminHodView.EditDepartment_save,name="EditDepartment_save"),

    path('course',AdminHodView.course,name="course"),
    path('Addcourse',AdminHodView.Addcourse,name="Addcourse"),
    path('Addcourse_save',AdminHodView.Addcourse_save,name="Addcourse_save"),
    path('Editcourse/<str:course_id>',AdminHodView.Editcourse,name="Editcourse"),
    path('Editcourse_save',AdminHodView.Editcourse_save,name="Editcourse_save"),

    path('subject',AdminHodView.subject,name="subject"),
    path('Addsubject',AdminHodView.Addsubject,name="Addsubject"),
    path('Addsubject_save',AdminHodView.Addsubject_save,name="Addsubject_save"),
    path('Editsubject/<str:subject_id>',AdminHodView.Editsubject,name="Editsubject"),
    path('Editsubject_save',AdminHodView.Editsubject_save,name="Editsubject_save"),

    path('Room',AdminHodView.Room,name="Room"),
    path('AddRoom',AdminHodView.AddRoom,name="AddRoom"),
    path('AddRoom_save',AdminHodView.AddRoom_save,name="AddRoom_save"),
    path('EditRoom/<str:room_id>',AdminHodView.EditRoom,name="EditRoom"),
    path('EditRoom_save',AdminHodView.EditRoom_save,name="EditRoom_save"),

    path('leave',AdminHodView.leave,name="leave"),
    #path('feedback',AdminHodView.feedback,name="feedback"),
    path('notification',AdminHodView.notification,name="notification"),
    path('Session',AdminHodView.Session,name="Session"),
    path('AddSession',AdminHodView.AddSession,name="AddSession"),
    path('AddSession_save',AdminHodView.AddSession_save,name="AddSession_save"),
    path('check_email_exist',AdminHodView.check_email_exist,name="check_email_exist"),
    path('check_username_exist',AdminHodView.check_username_exist,name="check_username_exist"),
    path('student_feedback_message',AdminHodView.student_feedback_message,name="student_feedback_message"),
    path('student_feedback_message_replied',AdminHodView.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('staff_feedback_message',AdminHodView.staff_feedback_message,name="staff_feedback_message"),
    path('staff_feedback_message_replied',AdminHodView.staff_feedback_message_replied,name="staff_feedback_message_replied"),
    path('staff_leave_view',AdminHodView.staff_leave_view,name="staff_leave_view"),
    path('staff_approve_leave/<str:leave_id>',AdminHodView.staff_approve_leave,name="staff_approve_leave"),
    path('staff_disapprove_leave/<str:leave_id>',AdminHodView.staff_disapprove_leave,name="staff_disapprove_leave"),
    path('student_leave_view',AdminHodView.student_leave_view,name="student_leave_view"),
    path('student_approve_leave/<str:leave_id>',AdminHodView.student_approve_leave,name="student_approve_leave"),
    path('student_disapprove_leave/<str:leave_id>',AdminHodView.student_disapprove_leave,name="student_disapprove_leave"),
    path('admin_profile',AdminHodView.admin_profile,name="admin_profile"),
    path('admin_profile_save',AdminHodView.admin_profile_save,name="admin_profile_save"),

    #admin timetable begins here
    path('timetable',AdminHodView.timetable,name="timetable"),
    #staff urls begin here now let start
    path('staff_home',StaffView.staff_home,name="staff_home"),
    path('staff_take_attendance',StaffView.staff_take_attendance,name="staff_take_attendance"),
    path('staff_update_attendance',StaffView.staff_update_attendance,name="staff_update_attendance"),
    path('get_attendance_dates',StaffView.get_attendance_dates,name="get_attendance_dates"),
    path('get_attendance_student',StaffView.get_attendance_student,name="get_attendance_student"),
    path('get_students',StaffView.get_students,name="get_students"),
    path('save_attendance_data',StaffView.save_attendance_data,name="save_attendance_data"),
    path('save_updateattendance_data',StaffView.save_updateattendance_data,name="save_updateattendance_data"),
    path('staff_apply_leave',StaffView.staff_apply_leave,name="staff_apply_leave"),
    path('staff_apply_leave_save',StaffView.staff_apply_leave_save,name="staff_apply_leave_save"),
    path('staff_feedback',StaffView.staff_feedback,name="staff_feedback"),
    path('staff_feedback_save',StaffView.staff_feedback_save,name="staff_feedback_save"),
    path('staff_profile',StaffView.staff_profile,name="staff_profile"),
    path('staff_profile_save',StaffView.staff_profile_save,name="staff_profile_save"),
    #student urls begin here now lets start
    path('student_home',StudentView.student_home,name="student_home"),
    path('student_view_attendance',StudentView.student_view_attendance,name="student_view_attendance"),
    path('student_view_attendance_post',StudentView.student_view_attendance_post,name="student_view_attendance_post"),
    path('student_apply_leave',StudentView.student_apply_leave,name="student_apply_leave"),
    path('student_apply_leave_save',StudentView.student_apply_leave_save,name="student_apply_leave_save"),
    path('student_feedback',StudentView.student_feedback,name="student_feedback"),
    path('student_feedback_save',StudentView.student_feedback_save,name="student_feedback_save"),
    path('student_profile',StudentView.student_profile,name="student_profile"),
    path('student_profile_save',StudentView.student_profile_save,name="student_profile_save"),
    #timetable urls begin from here
    path('Meeting_Time',AdminHodView.Meeting_Time,name="Meeting_Time"),
    path('AddMeetingTime',AdminHodView.AddMeetingTime,name="AddMeetingTime"),
    path('AddMeetingTime_save',AdminHodView.AddMeetingTime_save,name="AddMeetingTime_save"),
    path('EditMeetingTime',AdminHodView.EditMeetingTime,name="EditMeetingTime"),
    path('EditMeetingTime_save',AdminHodView.EditMeetingTime_save,name="EditMeetingTime_save"),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)