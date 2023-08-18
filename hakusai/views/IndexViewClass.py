from typing import Any, Dict
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'hakusai/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'トップ'
        return context
