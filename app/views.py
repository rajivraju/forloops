from django.shortcuts import render

# Create your views here
def forcon(request):
    d={'name':'rajiv raju'}
    return render(request,'forcon.html',d)