from django.shortcuts import render
from .models import GeneralInformation, Activity

def home(request):
    data = (("Groupements", GeneralInformation.objects.count()),
            ("Activities", Activity.objects.count()))
    
    return render(request, "hatvp/index.html", locals())
