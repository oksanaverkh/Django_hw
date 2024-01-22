from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, telephone: {self.telephone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    receipt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, available quantity: {self.quantity}'

    
class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
 
    
    
    def __str__(self):
        
        return f'Order: customer: {self.customer}, total price: {self.total_price}, order date: {self.order_date}\n'