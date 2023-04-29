from myapp.models import Person

person1 = Person.objects.create(first_name='Alice', last_name='Smith', email='alice.smith@example.com', age=25)
person2 = Person.objects.create(first_name='Bob', last_name='Jones', email='bob.jones@example.com', age=30)
