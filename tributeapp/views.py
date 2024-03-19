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

def process_directory(directory: str) -> dict[str, list[str]]:
    # dictionary to store folder names as keys and JSON file names as values
    folder_json_mapping: dict[str, list[str]] = {"dirs": []}

    # Traverse through the directory
    for root, _, files in os.walk(directory):
        # Extract folder name
        folder_name: str = os.path.basename(root)
        # Initialize list for JSON files
        json_files: list[str] = []
        # Iterate through files in current directory
        for file in files:
            # Check if file is a JSON file
            if file.endswith(".json"):
                # Add JSON file name without extension to list
                json_files.append(os.path.splitext(file)[0])
        # Add folder name and corresponding JSON files to dictionary
        folder_json_mapping[folder_name] = json_files
        # Add folder name to "dirs" list
        if folder_name != os.path.basename(directory):
            folder_json_mapping["dirs"].append(folder_name)

    return folder_json_mapping

def root(request: HttpRequest):
    directories: dict[str, list[str]] = process_directory("data")

    # Formatting the context dictionary
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
#     return render(request, 'static_test/test.html', {})

def profile(request: HttpRequest, occupation: str, filename: str):
    print(occupation, filename)

    file_path = os.path.join("data", occupation, f"{filename}.json")

    print(file_path)

    try:
        with open(file_path, "r") as file:
            context = json.load(file)
    except FileNotFoundError:
        return render(request, 'templates/404.html', {})

    return render(request, 'templates/profile.html', context)
