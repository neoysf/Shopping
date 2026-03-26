from .models import SiteInfo
from .models import SocialLinks

def site_info(request):
    site_info = SiteInfo.objects.first()
    return {'site_info': site_info}

def social_links(request):
    social_links = SocialLinks.objects.first()
    return {'social_links': social_links}