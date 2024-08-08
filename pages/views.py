from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def customer_service_center(request):
    return render(request, 'pages/customer_service_center.html')

def existing_product(request):
    return render(request, 'pages/existing_product.html')