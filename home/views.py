from django.shortcuts import render
from .rabbitmq import publish_message
import random
from faker import Faker
fake = Faker()
import json
# Create your views here.


def index(request):
    message = f"Hello World! {random.randint(1, 100)}"
    name = [
        {'Name': fake.name(),'Address': fake.address()} for _ in range(10)
    ]
    name = json.dumps(name)
    publish_message(name)
    return render(request, 'index.html')
