from django import http
from typing import Any, Dict
from django.views.generic import TemplateView
from hakusai.models import Projects, Exhibitions, ExhibitionSettings
from django.shortcuts import redirect

class ExhibitionNewView(TemplateView):
    template_name = 'hakusai/exhibition_new.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = '新規展示'
        context['projects'] = Projects.objects.filter(draft_flag=False, delete_flag=False)
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        # 新しい展示を作成し、変数に格納
        new_exhibition = Exhibitions.objects.create(name=request.POST.get('exhibition-name'), memo=request.POST.get('exhibition-memo'))

        exhibition_count = sum(1 for key in request.POST if key.endswith('repeat')) # 展示数を取得
        exhibition_settings = [] # 新しく追加する展示設定を格納する配列
        for i in range(1, exhibition_count + 1):
            # プロジェクト名からレコード取得
            project = Projects.objects.get(name=request.POST.get(f'exhibition{i}-project-name'))
            # フィールドに値をセット
            new_exhibition_setting = ExhibitionSettings(repeat=request.POST.get(f'exhibition{i}-repeat'), exec_order=i, exhibition_id=new_exhibition.id, project_id=project.id)
            exhibition_settings.append(new_exhibition_setting) # 配列にレコードを一時保存
        ExhibitionSettings.objects.bulk_create(exhibition_settings) # 配列保存されたレコードを一括追加

        return redirect('hakusai:exhibition_list') # 展示一覧ページへ遷移