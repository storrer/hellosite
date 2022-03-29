from django.shortcuts import render

from django.shortcuts import render
from django.views import View

class HelloWorldView(View):
    def get(self, request):
        return render(request = request, template_name='hello_world.html')
