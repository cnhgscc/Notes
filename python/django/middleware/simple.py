class SimpleMiddleware:


    def process_request(self, request):
        """
        Parameters
        ----------
        request: WSGIRequest object ...example: <WSGIRequest: GET '/'>

        Return
        ----------
        None
        """

        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        Parameters
        ----------
        request: WSGIRequest object ...example: <WSGIRequest: GET '/'>
        callback: View Function
        callback_args: View Function args
        callback_kwargs: View Function kwargs

        Return
        ----------
        None or HttpResponse object
        """

        pass

    def process_response(self, request, response):
        """
        Parameters
        ----------
        request: WSGIRequest ...example: <WSGIRequest: GET '/'>
        response: HttpResponse object

        Return
        ----------
        HttpResponse object
        """

        return response

    def process_exception(self, request, exception):
        """request is an HttpRequest object. exception is an Exception 
        object raised by the view function.


        Parameters
        ----------
        request: WSGIRequest ...example: <WSGIRequest: GET '/'>
        exception: raised by the view function
        
        Return
        ----------
        None or HttpResponse object
        """
    
        pass