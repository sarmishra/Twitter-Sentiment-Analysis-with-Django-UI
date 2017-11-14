from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from login.logic import *


def twitter(request):
    template_name = "login/h.html"
    if request.method == 'POST':
        input = request.POST['textfield']
        input = input.lower().split()
        print(input)
        output = classifier.classify(extract_features(input))
        return render(request, template_name, {'predicted_data': output})
    else:
        return render(request, template_name)

