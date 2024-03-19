import os
import json

from django.shortcuts import render
from django.http import HttpRequest #, HttpResponse

from typing import Any
from helpers import process_directory, replace_value

parsed_base64_images = {}

with open("data/images_b64.json", "r") as file:
    parsed_base64_images = json.load(file)

def serve_root(request: HttpRequest):
    directories: dict[str, list[str]] = process_directory("data")

    context = {
        'categories': [
            {'name': folder, 'names': directories[folder]} for folder in directories['dirs']
        ]
    }

    return render(request, 'static/templates/index.html', context)

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
#     return HttpResponse("This is a test view.")

def serve_tribute_profile(request: HttpRequest, occupation: str, filename: str):
    def predicate(value: Any) -> bool:
        if isinstance(value, str):
            return value.startswith("json:")
        return False

    def transformer(value: str) -> str:
        return parsed_base64_images[value.removeprefix("json:")]
    
    def key_predicate(key: str) -> bool:
        return key == "src" or key == "href"

    print(occupation, filename)

    file_path = os.path.join("data", occupation, f"{filename}.json")

    print(file_path)

    try:
        with open(file_path, "r") as file:
            context = json.load(file)
    except FileNotFoundError:
        return render(request, 'templates/404.html', {})

    replace_value(context, predicate, transformer, key_check=True, key_predicate=key_predicate)

    return render(request, 'templates/profile.html', context)
