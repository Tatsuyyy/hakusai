from typing import Any, Dict
from django import http
from django.views.generic import TemplateView
from hakusai.models import Projects
from django.shortcuts import redirect


class ProjectNewSummaryView(TemplateView):
    template_name = 'hakusai/project_new_summary.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = '新規プロジェクト'
        return context
    
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        new_project = Projects(name=request.POST["project-name"], url=request.POST["project-url"])
        new_project.save()
        return redirect('hakusai:project_new_step', project_id=new_project.id)
