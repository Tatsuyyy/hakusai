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

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        new_project = Projects(name=request.POST.get('project-name'), url=request.POST.get('project-url')) # フィールドに値をセット
        new_project.save() # 新規プロジェクトを追加
        return redirect('hakusai:project_new_step', project_id=new_project.id) # 新規プロジェクトのstep登録ページへ
