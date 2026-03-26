from django.contrib import admin
from .models import (Product, ContactMessage, SocialLinks,
                     UserEmail, SiteInfo, Big_slider,
                     Small_slider, Categories, Comment)

admin.site.register(Product)
admin.site.register(SocialLinks)
admin.site.register(UserEmail)
admin.site.register(SiteInfo)
admin.site.register(Big_slider)
admin.site.register(Small_slider)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(ContactMessage)






