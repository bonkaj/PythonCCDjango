from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, '/Users/bonkers/PycharmProjects/PythonWebProject/learning_logs/templates/index.html')

