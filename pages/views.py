from django.shortcuts import render

from django.http import HttpResponse


def my_first(request):
    return render(request, 'pages/index.html')


def my_second(request):
    return render(request, 'pages/indexrent.html')


def my_third(request):
    return render(request, 'pages/indexrepair.html')


def my_fourth(request):
    return render(request, 'pages/indexstore.html')


def my_fifth(request):
    return render(request, 'pages/indexservice.html')


def my_sixth(request):
    return render(request, 'pages/indexdelivery.html')


def my_seventh(request):
    return render(request, 'pages/indexcontact.html')

