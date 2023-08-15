from typing import Any, Dict
from django import http
from django.views.generic import TemplateView
from django.db.models import Max
from hakusai.models import Projects, Steps, Actions
from django.shortcuts import redirect

class ProjectEditView(TemplateView):
    template_name = 'hakusai/project_edit.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        current_project_id = self.kwargs['project_id'] # 編集中のprojectのid
        current_project = Projects.objects.get(id=current_project_id)
        context = super().get_context_data(**kwargs)
        context['title'] = 'プロジェクト編集'
        context['project_name'] = current_project.name
        context['project_url'] = current_project.url
        context['steps'] = Steps.objects.filter(project_id=current_project_id) # Stepsからproject_idが一致するレコードのみ取得
        context['actions'] = Actions.objects.values_list('name', flat=True)
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        print(request.POST)
        # メモ(最終的には消してね)
        # postで値送信を受け取り(request.POSTを要確認)、それを使ってstepsを更新する
        # その後returnでプロジェクト一覧にページ遷移する
        current_project_id = self.kwargs['project_id'] # 編集中のprojectのid

        # 更新前のstep数
        before_step_count = Steps.objects.filter(project_id=current_project_id).aggregate(Max('exec_order'))['exec_order__max']
        # 更新後のstep数
        after_step_count = sum(1 for key in request.POST if key.endswith('xpath'))
        # 更新前後のstep数を比較し、大きいほうをループ回数用変数に代入
        # loop_count = after_step_count if after_step_count >= before_step_count else before_step_count
        loop_count = after_step_count

        for i in range(1, loop_count + 1):
            # stepの更新または追加の処理
            # if i <= after_step_count:
                action = Actions.objects.get(name=request.POST.get(f'step{i}-action-name'))  # action名からレコードを取得
                # project_idと順序でレコードを検索してヒットすれば上書き、なければ追加
                Steps.objects.update_or_create(project_id=current_project_id, exec_order=i, defaults={'xpath': request.POST.get(f'step{i}-xpath'), 'action_str': request.POST.get(f'step{i}-action-str'), 'action_id': action.id})
            # 使わなくなったstepを初期化する処理
            # else:
                # 使わなくなったレコードの内容をNoneで初期化
                # Steps.objects.filter(project_id=current_project_id, exec_order=i).update(xpath=None, action_str=None, action_id=None)

        current_project = Projects.objects.get(id=current_project_id)
        submit_type = request.POST.get('submit-type')
        if submit_type == 'cancel':
            current_project.delete_flag = True
            current_project.draft_flag = False
        elif submit_type == 'draft':
            current_project.delete_flag = False
            current_project.draft_flag = True
        elif submit_type == 'submit':
            current_project.delete_flag =False
            current_project.draft_flag = False
        current_project.save()
        return redirect('hakusai:project_list')
