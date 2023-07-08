from typing import Any, Dict
from django.views.generic import TemplateView
from hakusai.models import Exhibitions


class ExhibitionListView(TemplateView):
    template_name = 'hakusai/exhibition_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = '展示一覧'
        context['exhibitions'] = Exhibitions.objects.filter(delete_flag=False)
        return context