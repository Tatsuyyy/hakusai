from django.views.generic import TemplateView


class ProjectListView(TemplateView):
    template_name = 'hakusai/project_list.html'