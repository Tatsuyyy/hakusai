from django.views.generic import TemplateView
from typing import Any, Dict
from django import http
from hakusai.models import Projects, Actions, Steps
from django.shortcuts import redirect


class ProjectNewStepView(TemplateView):
    template_name = 'hakusai/project_new_step.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        new_project = Projects.objects.get(id=self.kwargs['project_id'])
        context = super().get_context_data(**kwargs)
        context['title'] = 'ステップ登録'
        context['project_name'] = new_project.name
        context['project_url'] = new_project.url
        context['actions'] = Actions.objects.values_list('name', flat=True)  # Actionsからactionのリストを取得しcontextにセット
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        new_project_id = self.kwargs['project_id']  # urlからprojectのidを取得

        step_count = sum(1 for key in request.POST if key.endswith('xpath'))  # request.POST(QueryDict)のkeyからxpathが出た分カウントしてstep数を取得
        new_steps = []  # 登録するstepを格納する配列
        for i in range(1, step_count + 1):
            action = Actions.objects.get(name=request.POST.get(f'step{i}-action-name'))  # action名からレコードを取得
            # それぞれのフィールドに値をセット
            new_step = Steps(xpath=request.POST.get(f'step{i}-xpath'), action_str=request.POST.get(f'step{i}-action-str'),exec_order=i,action_id=action.id,project_id=new_project_id)
            new_steps.append(new_step)
        Steps.objects.bulk_create(new_steps) # ループで格納したレコードを一括追加

        new_project = Projects.objects.get(id=new_project_id) # 新しいプロジェクトのレコードを取得してセット
        submit_type = request.POST.get('submit-type') # ボタンの状態を取得
        # 削除して戻るの処理
        if submit_type == 'cancel':
            new_project.delete_flag = True
            new_project.draft_flag = False
        # 下書き保存の処理
        elif submit_type == 'draft':
            new_project.delete_flag = False
            new_project.draft_flag = True
        # 作成の処理
        elif submit_type == 'submit':
            new_project.delete_flag = False
            new_project.draft_flag = False
        new_project.save() # 新しいprojectのレコードを上書き保存

        return redirect('hakusai:project_list')  # プロジェクトリストのページへ
