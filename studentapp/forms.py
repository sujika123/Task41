from django import forms

from studentapp.models import Student, Enrollment, Subject, Class


class DateInput(forms.DateInput):
    input_type = "date"

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class studentaddform(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = Student
        fields = "__all__"


class addclassform(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"


class addsubjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class enrollmentform(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"