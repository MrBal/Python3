# Example 1: Flask Application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

# Example 2: HTML Form Handling with Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()

# Example 3: Django Application
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# Example 4: Django View
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Example 5: Django Model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

# Example 6: Django Template
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>This is a sample Django template.</p>
</body>
</html>

# Example 7: JavaScript Function
function greet(name) {
    console.log('Hello, ' + name + '!');
}

// Example 8: JavaScript Conditional Statement
let num = 10;

if (num > 0) {
    console.log('Positive number');
} else if (num < 0) {
    console.log('Negative number');
} else {
    console.log('Zero');
}
