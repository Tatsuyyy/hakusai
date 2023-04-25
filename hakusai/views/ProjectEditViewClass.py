from django.views.generic import TemplateView


class ProjectEditView(TemplateView):
    template_name = 'hakusai/project_edit.html'