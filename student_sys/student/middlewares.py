# coding:utf-8
from __future__ import unicode_literals

import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, requets):
        self.start_time = time.time()
        return
    
    def process_view(self, requets, func, *args, **kwargs):
        if requets.path != reverse('index'):
            return None

        start = time.time()
        response = func(requets)
        costed =time.time() - start
        print('process view: {:2f}s'.format(costed))
        return response

    def process_exception(self, requets, exception):
        pass
    
    def process_template_response(self, requets, response):
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('process view: {:2f}s'.format(costed))
        return response
