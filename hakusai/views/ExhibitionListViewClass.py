from django.views.generic import TemplateView


class ExhibitionListView(TemplateView):
    template_name = 'hakusai/exhibition_list.html'