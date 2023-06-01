from typing import Any, Dict
from django import http
from django.views.generic import TemplateView


class ProjectNewSummaryView(TemplateView):
    template_name = 'hakusai/project_new_summary.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    # POST送信を受け取る
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        # メモ(最終的には消してね)
        # postで値送信を受け取り(request.POSTを要確認)、それを使ってDBに新規プロジェクトを作成する。
        # 新規作成されたプロジェクトのidを使ってreturnでステップ登録ページに遷移する
        return super().get(request, *args, **kwargs)

