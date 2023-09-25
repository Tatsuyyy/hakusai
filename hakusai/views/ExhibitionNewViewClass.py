from django import http
from typing import Any, Dict
from django.views.generic import TemplateView

class ExhibitionNewView(TemplateView):
    template_name = 'hakusai/exhibition_new.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        # メモ(最終的には消してね)
        # postで値送信を受け取り(request.POSTを要確認)、送信された値を使ってExihibitionを新規作成する
        # その後returnで展示一覧にページ遷移する
        return super().get(request, *args, **kwargs)