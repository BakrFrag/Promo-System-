import sys;
from django.http import HttpResponse;
class CatchOperationalError(object):
    '''
    custom middleware check connection of database 
    before processing any request
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request);

    def process_exception(self, request, exception): 
        exc_info=sys.exc_info()[1];
        name=exception.__class__.__name__;
        if type(exception).__name__ == 'OperationalError':
            return HttpResponse("Database Connection Error",status=503);