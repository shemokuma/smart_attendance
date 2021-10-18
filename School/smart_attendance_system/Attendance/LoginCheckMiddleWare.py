from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                 if modulename == "Attendance.AdminHodView":
                     pass
                 elif modulename == "Attendance.views" or modulename == "django.views.static":
                       pass
                 else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "Attendance.StaffView":
                    pass
                elif modulename == "Attendance.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            else:
                if modulename == "Attendance.StudentView":
                    pass
                elif modulename == "Attendance.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views":
                pass
            else:
                return  HttpResponseRedirect(reverse("show_login"))
