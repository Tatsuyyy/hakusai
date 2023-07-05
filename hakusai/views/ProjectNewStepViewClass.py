from django.views.generic import TemplateView
from typing import Any, Dict
from django import http

class ProjectNewStepView(TemplateView):
    template_name = 'hakusai/project_new_step.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        # メモ(最終的には消してね)
        # postで値送信を受け取り(request.POSTを要確認)、それを使ってidに指定されたprojectsにstepsを新規作成する。
        # また、submit-typeがcancelの場合はdelete_flagを、draftの場合はdraft_flagをそれぞれtrueにする
        # その後returnでプロジェクト一覧にページ遷移する
        return super().get(request, *args, **kwargs)
