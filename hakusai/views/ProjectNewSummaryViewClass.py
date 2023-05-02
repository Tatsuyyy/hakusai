from django.views.generic import TemplateView


class ProjectNewSummaryView(TemplateView):
    template_name = 'hakusai/project_new_summary.html'