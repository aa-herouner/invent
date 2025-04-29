from django.db import models

from users.models import User


# class Supplier(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, unique=True)
#     address = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Season(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     description = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    size = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField(null=True)
    created_date = models.DateField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self.quantity and self.unit_price:
            self.total_price = self.quantity * self.unit_price  # Calculate total price
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('complete', 'Complete'),
    )
    Delivery_Choice = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField(null=True)
    price = models.IntegerField()
    delivery = models.CharField(max_length=10, choices=Delivery_Choice)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # design = models.CharField(max_length=50)
    # color = models.CharField(max_length=50)
    # season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    



    def __str__(self):
        return self.product.name


# class Delivery(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     courier_name = models.CharField(max_length=120)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.courier_name