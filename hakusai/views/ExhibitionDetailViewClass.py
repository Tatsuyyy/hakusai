from typing import Any, Dict
from django import http
from django.views.generic import TemplateView
from hakusai.models import Exhibitions, ExhibitionSettings
from django.shortcuts import redirect


class ExhibitionDetailView(TemplateView):
    template_name = 'hakusai/exhibition_detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        current_exhibition = Exhibitions.objects.get(id=self.kwargs['exhibition_id'])
        context = super().get_context_data(**kwargs)
        context['title'] = '展示詳細'
        context['exhibition_name'] = current_exhibition.name
        context['exhibition_projects'] = ExhibitionSettings.objects.filter(exhibition_id=current_exhibition.id)
        return context

    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        print(request.POST)

        return redirect('hakusai:exhibition_list')