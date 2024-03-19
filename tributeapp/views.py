from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

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

def profile(request: HttpRequest):
    context = {
        "name": {
            "title": "Ramanujan Srinivasan",
            "underlined": "Srinivasa Iyengar",
            "colored": "Ramanujan",
        },
        "category": "Mathematician",
        "tagline": "The Man Who Knew Infinity",
        "wikipedia": "https://en.wikipedia.org/wiki/Srinivasa_Ramanujan",
        "image": {
            "main": {
                "src": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Srinivasa_Ramanujan-Add._MS_a94_version2.jpg",
                "alt": "Ramanujan in 1920",
                "is_static": False,
            },
        },
        "data": {
            "summary": {
                "p1": "Srinivasa Ramanujan FRS was an Indian mathematician who lived during the British Rule in India. Though he had almost no formal training in pure mathematics, he made substantial contributions to mathematical analysis, number theory, infinite series, and continued fractions, including solutions to mathematical problems considered to be unsolvable.",
                "p2": "Ramanujan initially developed his own mathematical research in isolation; it was quickly recognized by Indian mathematicians. Seeking mathematicians who could better understand his work, in 1913 he began a postal partnership with the English mathematician G. H. Hardy at the University of Cambridge, England. Recognizing the extraordinary work sent to him as samples, Hardy arranged travel for Ramanujan to Cambridge. In his notes, Hardy commented that Ramanujan had produced groundbreaking new theorems, including some that Hardy stated had defeated him and his colleagues, in addition to rediscovering recently proven but highly advanced results."
            }
        },
        "life_awards_and_achievements": [
            {
                "title": "Fellow of the Royal Society",
                "year": 1918,
                "description": "The fellowship of the Royal Society is a fellowship awarded to individuals who have made a substantial contribution to the improvement of natural knowledge, including mathematics.",
                "links": {
                    "button": [
                        {
                            "text": "Test 1",
                            "src": "https://www.example.com",
                        }
                    ],
                    "reference": [
                        {
                            "text": "Test 2",
                            "src": "https://www.google.com",
                        }
                    ]
                },
                "image": {
                    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Srinivasa_Ramanujan_1962_stamp_of_India.jpg/300px-Srinivasa_Ramanujan_1962_stamp_of_India.jpg",
                    "alt": "Royal Society Logo",
                    "is_static": False
                }
            },
            {
                "title": "Fellow of Trinity College, Cambridge",
                "year": 1918,
                "description": "Trinity College is a constituent college of the University of Cambridge in England. With around 600 undergraduates, 300 graduates, and over 180 fellows, it is the largest college in either of the Oxbridge universities by number of undergraduates.",
                "links": {
                    "button": [
                        {
                            "text": "Test 1",
                            "src": "https://www.example.com",
                        },
                        {
                            "text": "Test 2",
                            "src": "https://www.google.com",
                        }
                    ],
                    "reference": [
                        {
                            "text": "Test 2",
                            "src": "https://www.google.com",
                        }
                    ]
                },
                "image": {
                    "src": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Srinivasa_Ramanujan-Add._MS_a94_version2.jpg",
                    "alt": "Trinity College, Cambridge Coat of Arms",
                    "is_static": False
                }
            },
            {
                "title": "Fellow of the Indian Academy of Sciences",
                "year": 1930,
                "description": "The Indian Academy of Sciences, Bangalore was founded by C. V. Raman, and was registered as a society on 24 April 1934. Inaugurated on 31 July 1934, it began with 65 founding fellows. The first general meeting of Fellows, held on the same day, elected Professor Raman as President, and adopted the constitution of the Academy.",
                "links": {
                    "button": [
                        {
                            "text": "Test 1",
                            "src": "https://www.example.com",
                        }
                    ],
                    "reference": [
                        {
                            "text": "Test 2",
                            "src": "https://www.google.com",
                        },
                        {
                            "text": "Test 3",
                            "src": "https://www.google.com",
                        }
                    ]
                },
                "image": {
                    "src": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Srinivasa_Ramanujan-Add._MS_a94_version2.jpg",
                    "alt": "Indian Academy of Sciences Logo",
                    "is_static": False
                }
            }
        ]
    }

    print(request.get_full_path_info())

    return render(request, 'profile/index.html', context)