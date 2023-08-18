from typing import Any, Dict
from django.views.generic import TemplateView
from hakusai.models import Projects


class ProjectListView(TemplateView):
    template_name = 'hakusai/project_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'プロジェクト一覧'
        context['projects'] = Projects.objects.all() # Projectsの全レコードをセット
        return context
