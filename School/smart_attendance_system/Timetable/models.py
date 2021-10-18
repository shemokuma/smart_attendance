from django.db import models

# Create your models here.

#class Instructor(models.Model):
#    id=models.AutoField(primary_key=True)
#    #admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)#
 #   name=models.CharField(max_length=255)
#    email=models.CharField(max_length=255)
#    password=models.CharField(max_length=255)
#    address=models.TextField()#
#    created_at=models.DateTimeField(auto_now_add=True)
#    update_at=models.DateTimeField( auto_now_add=True)
#    objects=models.Manager()
#class Departments(models.Model):
#    id=models.AutoField(primary_key=True)
#    department_name=models.CharField(max_length=255)
#    created_at=models.DateTimeField(auto_now_add=True)
#    updated_at=models.DateTimeField(auto_now_add=True)
#    objects=models.Manager()

#class Course(models.Model):
   # id=models.AutoField(primary_key=True)
   # course_name=models.CharField(max_length=255)
    #max_number_of_student=models.IntegerField()
   # department_id=models.ForeignKey(Departments,on_delete=models.CASCADE,default=1)
    #created_at=models.DateTimeField(auto_now_add=True)
   # updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.Manager()

#class Rooms(models.Model):
    #id=models.AutoField(primary_key=True)
    #room_name=models.CharField(max_length=255)
    #room_capacity=models.IntegerField()
    #created_at=models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.Manager() 
#class MeetingTime(models.Model):
    #id=models.AutoField(primary_key=True)
    #meeting_time_time=models.DateTimeField(auto_now_add=True)
    #day=models.TextField()
    #room_id=models.ForeignKey(Rooms,on_delete=models.CASCADE,default=1)
    #subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE,default=1)
    #created_at=models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.Manager() 
#class Section(models.Model):
    #id=models.AutoField(primary_key=True)
    #section_id=models.IntegerField()
    #num_class_in_week=models.IntegerField()
    #subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE,default=1)
   #created_at=models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.Manager()
