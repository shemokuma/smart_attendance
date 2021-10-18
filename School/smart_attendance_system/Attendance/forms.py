
from django import forms
from Attendance.models import SessionYearModel ,Courses
class DateInput(forms.DateInput):
	input_type="date"
class AddStudentForm(forms.Form):
	email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
	password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
	username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	COURSE=Courses.objects.all()
	course_list=[]
	for course in COURSE:
		small_course=(course.id,course.course_name)
		course_list.append(small_course)

	sessions=SessionYearModel.objects.all()
	session_list=[]
	for session in sessions:
		small_session=(session.id,str(session.session_start_year)+" To "+str(session.session_End_year))
		session_list.append(small_session)
	gender_list=(
		("Male","Male"),
		("Female","Female")
	)
	course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
	gender=forms.ChoiceField(label="Gender",choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))
	session_year_id=forms.ChoiceField(label="Session year",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
	profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
	email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
	username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	COURSE=Courses.objects.all()
	course_list=[]
	for course in COURSE:
		small_course=(course.id,course.course_name)
		course_list.append(small_course)
		
	sessions=SessionYearModel.objects.all()
	session_list=[]
	for session in sessions:
		small_session=(session.id,str(session.session_start_year)+" To "+str(session.session_End_year))
		session_list.append(small_session)
	gender_list=(
		("Male","Male"),
		("Female","Female")
	)
	course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
	gender=forms.ChoiceField(label="Gender",choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))
	session_year_id=forms.ChoiceField(label="Session year",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
	profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)



class AddStaffForm(forms.Form):
	email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
	password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	
class EditStaffForm(forms.Form):
	email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
	first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
	