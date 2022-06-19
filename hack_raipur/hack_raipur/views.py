
from django.http import HttpResponse
 
def hello_geek (request) :
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")