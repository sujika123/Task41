from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class Class(models.Model):
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} - {self.section}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    class_assigned = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='subjects')

    def __str__(self):
         return self.subject_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrollments')
    student_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
         return self.student



