from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    data = {
        "shopping_date": datetime.datetime.now(),
        "shopping_items": [
            {
                'id': '1',
                'name': 'Apples',
                'categories': ['Fruits', 'Healthy'],
                'price': 2.5,
                'quantity': 3
            },
            {
                'id': '2',
                'name': 'Milk',
                'categories': ['Dairy', 'Essentials'],
                'price': 1.99,
                'quantity': 1
            },
            {
                'id': '3',
                'name': 'Bread',
                'categories': ['Bakery', 'Essentials'],
                'price': 2.0,
                'quantity': 2
            },
            {
                'id': '4',
                'name': 'Chicken',
                'categories': ['Meat', 'Protein'],
                'price': 5.99,
                'quantity': 1
            },
            {
                'id': '5',
                'name': 'Rice',
                'categories': ['Grains', 'Essentials'],
                'price': 3.5,
                'quantity': 1
            },
            {
                'id': '6',
                'name': 'Spinach',
                'categories': ['Vegetables', 'Healthy'],
                'price': 1.0,
                'quantity': 2
            },
            {
                'id': '7',
                'name': 'Eggs',
                'categories': ['Dairy', 'Protein'],
                'price': 2.99,
                'quantity': 1
            },
            {
                'id': '8',
                'name': 'Salmon',
                'categories': ['Fish', 'Protein'],
                'price': 8.5,
                'quantity': 1
            },
            {
                'id': '9',
                'name': 'Tomatoes',
                'categories': ['Vegetables', 'Healthy'],
                'price': 1.5,
                'quantity': 4
            },
            {
                'id': '10',
                'name': 'Cheese',
                'categories': ['Dairy', 'Essentials'],
                'price': 4.0,
                'quantity': 1
            }
        ]
    }
    for item in data["shopping_items"]:
        item["total_price"] = item["price"] * item["quantity"]
        
    return render(req, 'practiceapp/index.html', data)






