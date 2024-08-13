from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def customer_service_center(request):
    return render(request, 'pages/customer_service_center.html')

def customer_3(request):
    return render(request, 'pages/customer_3.html')

def q_a(request):
    return render(request, 'pages/q_a.html')

def gaesipan(request):
    return render(request, 'pages/gaesipan.html')

def existing_product(request):
    return render(request, 'pages/existing_product.html')