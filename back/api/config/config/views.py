# back/api/config/config/views.py
from django.views.generic import TemplateView
from django.http import HttpResponse
import os

class FrontIndexView(TemplateView):
    template_name = "index.html"


    def get(self, request, *args, **kwargs):
        # Debug : vérifier si le fichier existe
        from django.conf import settings
        template_path = os.path.join(settings.BASE_DIR.parent.parent, "front", "index.html")
        print(f"Cherche le template à : {template_path}")
        print(f"Le fichier existe : {os.path.exists(template_path)}")
        return super().get(request, *args, **kwargs)