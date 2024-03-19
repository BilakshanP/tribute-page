from django.shortcuts import render
from django.http import HttpRequest #, HttpResponse

import os
import json

# def root(request: HttpRequest):
#     return HttpResponse("""
#                         <span style="font-size: 20px; font-family: 'Arial'; font-weight: bold; color: #333;">
#                             This is the root route, and is undefined.
#                         </span>

#                         <br><br>

#                         """
#                         +
                        
#                         # <a href="/route/a/">Route A</a>
#                         # <br>
#                         # <a href="/route/b/">Route B</a>
#                         # <br>
#                         # <a href="/example/">Example</a>
#                         # <br>
#                         # <a href="/test/">Test</a>
#                         # <br>

#                         """
#                         <a href="/tribute/profile/">Test 2</a>
#                         """)

def root(request: HttpRequest):
    return render(request, 'static/templates/index.html', {})

# def route_a(request: HttpRequest):
#     context = {
#         'example': 'This is route A.'
#     }
#     return render(request, 'static/templates/route_a.html', context)

# def route_b(request: HttpRequest):
#     context = {
#         'example': 'This is route B.'
#     }
#     return render(request, 'static/templates/route_b.html', context)

# def example_view(request: HttpRequest):
#     context = {
#         'user': {'username': 'John Doe'},
#         'items': ['Apple', 'Banana', 'Orange'],
#         'is_authenticated': True,
#     }
#     return render(request, 'static/templates/profile.html', context)

# def test(request: HttpRequest):
#     return render(request, 'static_test/test.html', {})

def profile(request: HttpRequest, occupation: str, filename: str):
    print(occupation, filename)

    file_path = os.path.join("data", occupation, f"{filename}.json")

    print(file_path)

    try:
        with open(file_path, "r") as file:
            context = json.load(file)
    except FileNotFoundError:
        return render(request, 'profile/404.html', {})

    return render(request, 'profile/index.html', context)
