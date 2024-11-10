from django.urls import path

from studentapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('studentupdate/<int:id>/',views.studentupdate,name='studentupdate'),
    path('studentdelete/<int:id>/',views.studentdelete,name='studentdelete'),
    path('enrollment_student',views.enrollment_student,name='enrollment_student'),
    path('viewstudent_enrollment',views.viewstudent_enrollment,name='viewstudent_enrollment'),
    path('updatestdntenroll/<int:id>/',views.updatestdntenroll,name='updatestdntenroll'),
    path('enrollmentdelete/<int:id>/',views.enrollmentdelete,name='enrollmentdelete'),
    path('enrollment_history/<int:student_id>/',views.enrollment_history,name='enrollment_history'),
    path('addclass',views.addclass,name='addclass'),
    path('viewclass',views.viewclass,name='viewclass'),
    path('add_subject',views.add_subject,name='add_subject'),
    path('view_subject',views.view_subject,name='view_subject'),
    path('list_students',views.list_students,name='list_students'),
    path('view_student_subject/<class_assigned>/',views.view_student_subject,name='view_student_subject'),



]