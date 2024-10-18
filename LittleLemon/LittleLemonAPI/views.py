from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    return Response(items.values())