from typing import Any, Dict
from django.views.generic import TemplateView

class ProjectListView(TemplateView):
    template_name = 'hakusai/project_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'プロジェクト一覧'
        return context
