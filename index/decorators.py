from django.shortcuts import redirect

def isLoggedIn(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if not request.session.get("student_id") and not request.session.get("admin"):     
            # quick test
            return redirect("/")            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func

def isStudent(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if not request.session.get("student_id"):     
            # quick test
            return redirect("/access-denied/")            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func

def isAdmin(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if not request.session.get("admin"):     
            # quick test
            return redirect("/access-denied/")            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func

def isNotLoggedIn(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if request.session.get("student_id"):     
            return redirect("/student/student-mainpage/")  
        elif request.session.get("admin"):
            return redirect("/university-admin/admin-mainpage/")
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func

def isStudentLogin(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if request.session.get("student_id"):     
            # quick test
            return redirect("/student/student-mainpage/")            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func

def isAdminLogin(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if request.session.get("admin"):     
            # quick test
            return redirect("/university-admin/admin-mainpage/")            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func