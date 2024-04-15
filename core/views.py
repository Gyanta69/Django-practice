from django.http import HttpResponse
def aboutUs(request):
    return HttpResponse('Welcome to the about us page!')
def courses(request):
    return HttpResponse('Welcome to the courses page!')