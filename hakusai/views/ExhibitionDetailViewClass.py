from django.views.generic import TemplateView


class ExhibitionDetailView(TemplateView):
    template_name = 'hakusai/exhibition_detail.html'