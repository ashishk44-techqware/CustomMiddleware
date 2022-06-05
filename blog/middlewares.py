# from urllib import response
from django.shortcuts import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Process one time initilization")

    def __call__(self, request):
        print("Process--call-- before")
        response = self.get_response(request)
        print("Process--call--")
        return response

    # ye sab same rakhna h function name bhi pre defined h ase hi rakhna h
    def process_view(request, *args, **kwargs):
        print("this is process view -- before view")
        # return HttpResponse("This is before view") # ye  http object return kare ga or view ko call nhi kare ga
        return None  # ye view ko call kare ka agar NONE hua to


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Except one time initilization")

    def __call__(self, request):
        print("Except--call-- before")
        response = self.get_response(request)
        print("Except--call--")
        return response

    # ye sab (Argument same rakhna h) (function name bhi pre defined h) ase hi rakhna h
    def process_exception(self, request, exception):
        # ye  http object return kare ga or view ko call nhi kare ga
        print("Exception occured")
        msg = exception
        print(msg)
        # is se hum us class ka pata kar sakte h jis ka error h
        class_name = exception.__class__.__name__
        print(class_name)

        return HttpResponse(msg)

# ye sab (Argument same rakhna h) (function name bhi pre defined h) ase hi rakhna h


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("temp one time initilization")

    def __call__(self, request):
        print("temp--call-- before")
        response = self.get_response(request)
        print("temp--call--")
        return response

    # ye sab same rakhna h function name bhi pre defined h ase hi rakhna h
    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'sonam'
        return response


# def my_middleware(get_response):
#     print("one time initilization")

#     def my_function(request):
#         print("this is before view")
#         response = get_response(request)
#         print("after view")
#         return response
#     return my_function


# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("one time initilization")

#     def __call__(self, request):
#         print("this is before view")
#         response = self.get_response(request)
#         print("after view")
#         return response
