from django.shortcuts import render
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request,"stock/index.html")
    
index= IndexView.as_view()
