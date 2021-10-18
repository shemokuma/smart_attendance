
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from Attendance.forms import AddStudentForm,EditStudentForm,AddStaffForm,EditStaffForm
from Attendance.models import CustomUser,Courses,Subjects,Staffs,Students,Courses,Subjects,SessionYearModel,FeedbackStaff,FeedbackStudent, LeaveReportStudent,LeaveReportStaff,Departments,Rooms,Section,MeetingTime
#timetable
import random as rnd 
POPULATION_SIZE=9
NUMB_OF_ELITE_SCHEDULES=1
TOURNAMENT_SELECTION_SIZE=3
MUTATION_RATE=0.05


def admin_home(request):
    return render(request,"AdminHodTemplates/home_content.html")
def staff(request):
    staffs=Staffs.objects.all()
    return render(request,"AdminHodTemplates/staff.html",{"staffs":staffs})
def Addstaff(request):
    form=AddStaffForm()
    return render(request,"AdminHodTemplates/Addstaff.html",{"form":form})
def Addstaff_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        form=AddStaffForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            username=form.cleaned_data["username"]
            address=form.cleaned_data["address"]
            try:
                user=CustomUser.objects.create_user(password=password,email=email,last_name=last_name,first_name=first_name,username=username,user_type=2)
                user.staffs.address = address
                user.save()
                messages.success(request,"successfully added staff")
                return HttpResponseRedirect(reverse("staff"))
            except:
                messages.error(request,"failed to add staff")
                return HttpResponseRedirect(reverse("Addstaff"))
        else:
            form=AddStaffForm(request.POST)
            return render(request,"AdminHodTemplates/Addstaff.html",{"form":form})
def Editstaff(request,staff_id):
    request.session['staff_id']=staff_id
    staff=Staffs.objects.get(admin=staff_id)
    form=EditStaffForm()
    form.fields['email'].initial=staff.admin.email
    form.fields['first_name'].initial=staff.admin.first_name
    form.fields['last_name'].initial=staff.admin.last_name
    form.fields['username'].initial=staff.admin.username
    form.fields['address'].initial=staff.address
    return render(request,"AdminHodTemplates/Editstaff.html",{"form":form,"id":staff_id,"username":staff.admin.username})
def Editstaff_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("method not allowed")
    else:
        staff_id=request.session.get("staff_id")
        if staff_id==None:
            return HttpResponseRedirect(request,"/staff")
        form=EditStaffForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            address =form.cleaned_data["address"]
            try:
                user=CustomUser.objects.get(id=staff_id)
                user.first_name=first_name
                user.last_name=last_name
                user.email=email
                user.username=username
                user.save()
                staff_model=Staffs.objects.get(admin=staff_id)
                staff_model.address=address
                staff_model.save()
                messages.success(request,"successfully edited staff")
                return HttpResponseRedirect(reverse("Editstaff",kwargs={"staff_id":staff_id}))
            except:
                messages.error(request,"Failed to edit staff")
                return HttpResponseRedirect(reverse("Editstaff", kwargs={"staff_id":staff_id}))
        else:
            form=EditStaffForm(request.POST)
            staff=Staffs.objects.get(admin=staff_id)
            return render(request,"AdminHodTemplates/Editstaff.html",{"form":form,"id":staff_id,"username":staff.admin.username})
def student(request):
    students = Students.objects.all()
    return render(request,"AdminHodTemplates/student.html",{"students":students})
def Addstudent(request):
    form=AddStudentForm()
    return render(request,"AdminHodTemplates/Addstudent.html",{"form":form})
def Addstudent_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("method not allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_year_id=form.cleaned_data["session_year_id"]
            course_id=form.cleaned_data["course"]
            gender=form.cleaned_data["gender"]
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.students.address = address
                course_obj=Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                session_year=SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id=session_year
                user.students.gender=gender
                user.students.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"successfully added student")
                return HttpResponseRedirect(reverse("student"))
            except:
                messages.error(request,"failed to add student")
                return HttpResponseRedirect(reverse("Addstudent"))
        else:
            form=AddStudentForm(request.POST)
            return render(request,"AdminHodTemplates/Addstudent.html",{"form":form})
def Editstudent(request,student_id):
    request.session['student_id']=student_id
    student=Students.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['gender'].initial=student.gender
    form.fields['session_year_id'].initial=student.session_year_id
    #form.fields['session_start_year'].initial=student.session_start_year
    #form.fields['session_End_year'].initial=student.session_End_year
    return render(request,"AdminHodTemplates/Editstudent.html",{"form":form,"id":student_id,"username":student.admin.username})
def Editstudent_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(request,"/student")

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            address =form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
        
            if request.FILES.get("profile_pic",False):
                profile_pic=request.FILES['profile_pic']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None
            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.email=email
                user.username=username
                user.save()
                student_model=Students.objects.get(admin=student_id)
                student_model.address=address
                session_year = SessionYearModel.objects.get(id=session_year_id)
                student_model.session_year_id = session_year
                student_model.gender=gender
                student_model.profile_pic=profile_pic_url
                course=Courses.objects.get(id=course_id)
                student_model.course_id=course
                student_model.save()
                del request.session['student_id']
                messages.success(request,"successfully edited student")
                return HttpResponseRedirect(reverse("Editstudent",kwargs={"student_id":student_id}))
            except:
                messages.error(request,"Failed to edit student")
                return HttpResponseRedirect(reverse("Editstudent",kwargs={"student_id":student_id}))
        else:
            form=EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"AdminHodTemplates/Editstudent.html",{"form":form,"id":student_id,"username":student.admin.username})
def Department(request):
    departments=Departments.objects.all()
    return render(request,"AdminHodTemplates/Department.html",{"departments":departments})
def AddDepartment(request):
    return render(request,"AdminHodTemplates/AddDepartment.html")
def AddDepartment_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        department=request.POST.get("department")
        try:
            department_model=Departments(department_name=department)
            department_model.save()
            messages.success(request,"successfuly added department")
            return HttpResponseRedirect(reverse("Department"))
        except:
            messages.error(request,"Failed to add department")
            return HttpResponseRedirect(reverse("AddDepartment"))
def EditDepartment(request,department_id):
    department=Departments.objects.get(id=department_id)
    return render(request,"AdminHodTemplates/EditDepartment.html",{"department":department,"id":department_id})
def EditDepartment_save(request):
    if request.method!="POST":
        return HttpResponse("method Not allowed")
    else:
        department_id=request.POST.get("department_id")
        department_name = request.POST.get("department")
        try:
            department=Departments.objects.get(id=department_id)
            department.department_name=department_name
            department.save()
            messages.success(request, "successfuly Edited department")
            return HttpResponseRedirect(reverse("Department",kwargs={"department_id":department_id}))
        except:
            messages.error(request, "Failed to Edit department")
            return HttpResponseRedirect(reverse("EditDepartment",kwargs={"department_id":department_id}))
def course(request):
    courses=Courses.objects.all()
    return render(request,"AdminHodTemplates/course.html",{"courses":courses})
def Addcourse(request):
    departments=Departments.objects.all()
    return render(request,"AdminHodTemplates/addcourse.html",{"departments":departments})
def Addcourse_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        course=request.POST.get("course")
        max_number_of_student=request.POST.get("max_number_of_student")
        department_id=request.POST.get("department")
        department=Departments.objects.get(id=department_id)
        try:
            course_model=Courses(course_name=course,max_number_of_student=max_number_of_student,department_id=department)
            course_model.save()
            messages.success(request,"successfuly added course")
            return HttpResponseRedirect(reverse("course"))
        except:
            messages.error(request,"Failed to add course")
            return HttpResponseRedirect(reverse("Addcourse"))
def Editcourse(request,course_id):
    course=Courses.objects.get(id=course_id)
    departments=Departments.objects.all()
    return render(request,"AdminHodTemplates/Editcourse.html",{"course":course,"id":course_id,"departments":departments})
def Editcourse_save(request):
    if request.method!="POST":
        return HttpResponse("method Not allowed")
    else:
        course_id=request.POST.get("course_id")
        course_name = request.POST.get("course")
        max_number_of_student=request.POST.get("max_number_of_student")
        department_id=request.POST.get("department")
        try:
            course=Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.max_number_of_student=max_number_of_student
            department=Departments.objects.get(id=department_id)
            course.department_id=department
            course.save()
            messages.success(request, "successfuly Edited course")
            return HttpResponseRedirect(reverse("Editcourse",kwargs={"course_id":course_id}))
        except:
            messages.error(request, "Failed to Edit course")
            return HttpResponseRedirect(reverse("Editcourse",kwargs={"course_id":course_id}))
def subject(request):
    subjects=Subjects.objects.all()
    return render(request,"AdminHodTemplates/subject.html",{"subjects":subjects})
def Addsubject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"AdminHodTemplates/Addsubject.html",{"staffs":staffs,"courses":courses})
def Addsubject_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)
        try:
            subject=Subjects(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"successfuly add subject")
            return HttpResponseRedirect(reverse("subject"))
        except:
            messages.error(request,"Failed to add subject")
            return HttpResponseRedirect(reverse("Addsubject"))
def Editsubject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"AdminHodTemplates/Editsubject.html",{"subject":subject,"staffs":staffs,"courses":courses,"id":subject_id})
def Editsubject_save(request):
    if request.method!="POST":
        return HttpResponse("method not alllowed")
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")
        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff=CustomUser.objects.get(id=staff_id)
            course=Courses.objects.get(id=course_id)
            subject.staff_id=staff
            subject.course_id=course
            subject.save()
            messages.success(request, "successfuly Edited subject")
            return HttpResponseRedirect(reverse("Editsubject",kwargs={"subject_id":subject_id}))
        except:
            messages.error(request, "Failed to Edit subject")
            return HttpResponseRedirect(reverse("Editsubject",kwargs={"subject_id": subject_id}))
def Room(request):
    rooms = Rooms.objects.all()
    return render(request, "AdminHodTemplates/Room.html", {"rooms": rooms})
def AddRoom(request):
    return render(request, "AdminHodTemplates/AddRoom.html")
def AddRoom_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        room_name = request.POST.get("room_name")
        room_capacity=request.POST.get("room_capacity")
        try:
            room_model = Rooms(room_name=room_name,room_capacity=room_capacity)
            room_model.save()
            messages.success(request, "successfuly added Room")
            return HttpResponseRedirect(reverse("Room"))
        except:
            messages.error(request, "Failed to add Room")
            return HttpResponseRedirect(reverse("AddRoom"))
def EditRoom(request,room_id):
    room = Rooms.objects.get(id=room_id)
    return render(request, "AdminHodTemplates/EditRoom.html", {"room": room, "id":room_id})
def EditRoom_save(request):
    if request.method != "POST":
        return HttpResponse("method Not allowed")
    else:
        room_id = request.POST.get("room_id")
        room_name = request.POST.get("room")
        room_capacity=request.POST.get("room_capacity")
        try:
            room = Rooms.objects.get(id=room_id)
            room.room_name = room_name
            room.room_capacity=room_capacity
            room.save()
            messages.success(request, "successfuly Edited Room")
            return HttpResponseRedirect(reverse("Room", kwargs={"room_id": room_id}))
        except:
            messages.error(request, "Failed to Edit Room")
            return HttpResponseRedirect(reverse("EditRoom", kwargs={"room_id": room_id}))
def leave(request):
    return render(request,"AdminHodTemplate/leave.html")
def notification(request):
    return render(request,"AdminHodTemplates/notification.html")
def Session(request):
    pass
 #   session=SessionYearModel.objects.all()
  #  return render(request,"AdminHodTemplates/Session.html",{"session":session})
def AddSession(request):
    return render(request,"AdminHodTemplates/AddSession.html")
def AddSession_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        session_start_year=request.POST.get("session_start_year")
        session_End_year=request.POST.get("session_End_year")
        try:
            sessionyear=SessionYearModel(session_start_year=session_start_year,session_End_year=session_End_year)
            sessionyear.save()
            messages.success(request,"successfuly added session")
            return HttpResponseRedirect(reverse("AddSession"))
        except:
            messages.error(request,"Failed to add session")
            return HttpResponseRedirect(reverse("AddSession"))
@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(False)
    else:
        return HttpResponse(True)
@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(False)
    else:
        return HttpResponse(True)
def staff_feedback_message(request):
    feedbacks=FeedbackStaff.objects.all()
    return render(request,"AdminHodTemplates/staff_feedback.html",{"feedbacks":feedbacks})
@csrf_exempt
def staff_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")
    #try:
    feedback=FeedbackStaff.objects.get(id=feedback_id)
    feedback.feedback_reply=feedback_message
    feedback.save()
    return HttpResponse("True")
    #except:
    #    return HttpResponse("False")
def student_feedback_message(request):
    feedbacks=FeedbackStudent.objects.all()
    return render(request,"AdminHodTemplates/student_feedback.html",{"feedbacks":feedbacks})
@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")
    try:
        feedback=FeedbackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
def staff_leave_view(request):
    leaves=LeaveReportStaff.objects.all()
    return render(request,"AdminHodTemplates/staff_leave.html",{"leaves":leaves})
def staff_approve_leave(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))
def staff_disapprove_leave(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))
def student_leave_view(request):
    leaves=LeaveReportStudent.objects.all()
    return render(request,"AdminHodTemplates/student_leave.html",{"leaves":leaves})
def student_approve_leave(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))
def student_disapprove_leave(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))
def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"AdminHodTemplates/admin_profile.html",{"user":user})
def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("last_name")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()
            messages.success(request,"successfully updated profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request,"Failed to update profile")
            return HttpResponseRedirect(reverse("admin_profile"))



def Meeting_Time(request):
    meetingTimes=MeetingTime.objects.all()
    return render(request,"AdminHodTemplates/MeetingTime.html",{"meetingTimes":meetingTimes})
def AddMeetingTime(request):
    subjects=Subjects.objects.all()
    rooms=Rooms.objects.all()
    return render(request,"AdminHodTemplates/AddMeetingTime.html",{"subjects":subjects,"rooms":rooms})
def AddMeetingTime_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        meeting_time_time=request.POST.get("meeting_time")
        day=request.POST.get("day")
        room_id=request.POST.get("room")
        room=Rooms.objects.get(id=room_id)
        subject_id=request.POST.get("subject")
        subject=Subjects.objects.get(id=subject_id)
        try:
            meetingtimes=MeetingTime(meeting_time_time=meeting_time_time,day=day,room_id=room,subject_id=subject)
            meetingtimes.save()
            messages.success(request,"successfuly add meeting time")
            return HttpResponseRedirect(reverse("Meeting_Time"))
        except:
            messages.error(request,"Failed to add meeting time")
            return HttpResponseRedirect(reverse("AddMeetingTime"))
def EditMeetingTime(request,meetingTime_id):
    meetingTime=MeetingTime.objects.get(id=meetingTime_id)
    rooms=Rooms.objects.all()
    subjects=Subjects.objects.all()
    return render(request,"AdminHodTemplates/Edit_meeting_time.html",{"meetingTime":meetingTime,"id":meetingTime_id.id,"rooms":rooms,"subjects":subjects})
def EditMeetingTime_save(request):
    if request.method!="POST":
        return HttpResponse("method Not allowed")
    else:
        course_id=request.POST.get("course_id")
        course_name = request.POST.get("course")
        max_number_of_student=request.POST.get("max_number_of_student")
        department_id=request.POST.get("department")
        try:
            course=Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.max_number_of_student=max_number_of_student
            department=Departments.objects.get(id=department_id)
            course.department_id=department
            course.save()
            messages.success(request, "successfuly Edited course")
            return HttpResponseRedirect(reverse("Editcourse",kwargs={"course_id":course_id}))
        except:
            messages.error(request, "Failed to Edit course")
            return HttpResponseRedirect(reverse("Editcourse",kwargs={"course_id":course_id}))
def timetable(request):
    return render(request,"AdminHodTemplates/timetable.html",{})



