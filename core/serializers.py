from rest_framework import serializers
from .models import Product, ContactMessage, SocialLinks, UserEmail, SiteInfo,Big_slider, Small_slider, Categories, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = '__all__'

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'

class BigSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Big_slider
        fields = '__all__'

class SmallSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Small_slider
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
