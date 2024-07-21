from django.shortcuts import render
from django.http import JsonResponse

def endpoint1(request):
    print("Endpoint 1 was called")
    return JsonResponse({"message": "Hello from endpoint 1"})

def endpoint2(request):
    print("Endpoint 2 was called")
    return JsonResponse({"message": "Hello from endpoint 2"})

def home(request):
    print("Home API was called")
    return JsonResponse({"message": "Welcome to the API"})
