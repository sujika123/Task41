from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from studentapp.forms import studentaddform, enrollmentform, addclassform, addsubjectform
from studentapp.models import Student, Enrollment, Class, Subject


# Create your views here.
def home(request):
    return render(request,'adminhome/dash.html')


def addstudent(request):
    form = studentaddform()
    u = request.user
    if request.method=='POST':
        form = studentaddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewstudent')
    return render(request,'adminhome/add_student.html',{'form':form})


def viewstudent(request):
    data = Student.objects.all()
    return render(request,'adminhome/view_student.html',{'data':data})


def studentupdate(request,id):
    user = Student.objects.get(id=id)
    form = studentaddform(instance=user)
    if request.method == "POST":
        form = studentaddform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewstudent')
    return render(request, 'adminhome/update_student.html', {'form': form})


def studentdelete(request,id):
    data = addstudent.objects.get(id=id)
    data.delete()
    return redirect('viewstudent')


# Enrollment

def enrollment_student(request):
    form = enrollmentform()
    u = request.user
    if request.method=='POST':
        form = enrollmentform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewstudent_enrollment')
    return render(request,'adminhome/add_student_enroll.html',{'form':form})



def viewstudent_enrollment(request):
    # value_list = Enrollment.objects.values_list('class_assigned', flat=True).distinct()
    # attend = {}
    # for value in value_list:
    #     attend[value] = Enrollment.objects.filter(class_assigned=value)
    # return render(request, 'adminhome/view_attendance.html', {'attend': attend})

    data = Enrollment.objects.all()

    return render(request,'adminhome/view_student_enroll.html',{'data':data})


# def viewstudent_enrollment(request):
#     data = Student.objects.all().select_related('Enrollment__class_assigned').prefetch_related('enrollments__subject')
#     query = request.GET.get('query')
#     if query:
#         data = Student.filter(
#             Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(enrollments__class_assigned__name__icontains=query)
#         )
#     return render(request, 'adminhome/view_student_enroll.html', {'data': data})


def view_student_subject(request,class_assigned):
    sub = Enrollment.objects.filter(class_assigned=class_assigned)

    context={
        'sub': sub,
        'class_assigned': class_assigned
    }
    return render(request,'adminhome/view_stdsubject.html',context)



# def view_student_subject(request,id):
#     c = Class.objects.get(id=id)
#     std = Student.objects.all
#     data = Subject.objects.filter()
#     return render(request,'adminhome/view_stdsubject.html',{'data':data})




def enrollmentdelete(request,id):
    data = Enrollment.objects.get(id=id)
    data.delete()
    return redirect('viewstudent_enrollment')


def updatestdntenroll(request,id):
    data = Enrollment.objects.get(id=id)
    form = enrollmentform(instance=data)
    if request.method == "POST":
        form = enrollmentform(request.POST or None, request.FILES, instance=data or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewstudent_enrollment')
    return render(request, 'adminhome/update_studentenrollment.html', {'form': form})


def enrollment_history(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    enrollments = student.enrollments.all()
    return render(request, 'adminhome/enrollment_history.html', {'student': student, 'enrollments': enrollments})





# def enrollment_history(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     enrollments = student.enrollments.all()
#     return render(request, 'students/enrollment_history.html', {'student': student, 'enrollments': enrollments})
#



def addclass(request):
    form = addclassform()
    u = request.user
    if request.method=='POST':
        form = addclassform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewclass')
    return render(request,'adminhome/add_class.html',{'form':form})


def viewclass(request):
    data = Class.objects.all()
    return render(request,'adminhome/view_class.html',{'data':data})


def add_subject(request):
    form = addsubjectform()
    u = request.user
    if request.method=='POST':
        form = addsubjectform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_subject')
    return render(request,'adminhome/add_subject.html',{'form':form})


def view_subject(request):
    data = Subject.objects.all()
    return render(request,'adminhome/view_subject.html',{'data':data})




# Searching

def list_students(request):
    query = request.GET.get('query', '')  # Capture the search query from the URL parameters
    students = Student.objects.all().select_related('enrollments__class_assigned').prefetch_related('enrollments__subjects')

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |  # Search by first name
            Q(last_name__icontains=query) |   # Search by last name
            Q(enrollments__class_assigned__name__icontains=query)  # Search by class name
        ).distinct()

    return render(request, 'adminhome/search.html', {'students': students, 'query': query})




def searching(request):
    prodd=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prodd = Student.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,"adminhome/search.html",{'qr':query,'prs':prodd})



# def searching(request):
#     prodd=None
#     query=None
#     if 'q' in request.GET:
#         query=request.GET.get('q')
#         prodd=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
#     return render(request,"search.html",{'qr':query,'prs':prodd})