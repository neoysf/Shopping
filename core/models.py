from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    stock_quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

class SocialLinks(models.Model):
    twitter = models.URLField(default="https://twitter.com/")
    facebook = models.URLField(default="https://facebook.com/")
    linkedin = models.URLField(default="https://linkedin.com/")
    instagram = models.URLField(default="https://instagram.com/")

    def __str__(self):
        return "Social Media Links"


class UserEmail(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class SiteInfo(models.Model):
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "Site Settings"

class Big_slider(models.Model):
    slider_image = models.ImageField()
    slider_title = models.CharField(max_length=100)
    slider_content = models.TextField(default="Default content")
    created_date = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.slider_title


class Small_slider(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    content = models.TextField(default="Default content")
    created_date = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Categories(models.Model):
    product_image = models.ImageField()
    product_name = models.CharField(max_length=100)
    product_count = models.IntegerField()

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} "
