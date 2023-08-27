from django.shortcuts import render


# Create your views here.

def home_component(request):
    return render(request , 'home.html' , {})



def site_header_component(request):
    return render(request , "shared/site_header_component.html" , {})



def site_footer_component(request):
    return render(request , "shared/site_footer_component.html" , {})