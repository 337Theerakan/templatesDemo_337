from django.shortcuts import render

def renderTemplate(request):
    myDict = {"name": "Rei"}  
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)  

def renderEmployee(request):
    myDict = {"id":123, "name":"Rei","salary":000}  
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict) 
