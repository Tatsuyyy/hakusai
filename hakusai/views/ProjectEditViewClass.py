from typing import Any, Dict
from django import http
from django.views.generic import TemplateView

class ProjectEditView(TemplateView):
    template_name = 'hakusai/project_edit.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        print(request.POST)
        # メモ(最終的には消してね)
        # postで値送信を受け取り(request.POSTを要確認)、それを使ってstepsを更新する
        # その後returnでプロジェクト一覧にページ遷移する
        return super().get(request, *args, **kwargs)
