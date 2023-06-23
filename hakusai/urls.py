from django.urls import path

from hakusai.views import IndexView, ExhibitionListView, ExhibitionDetailView, ExhibitionRunView, ExhibitionNewView, ProjectListView, ProjectNewSummaryView, ProjectNewStepView, ProjectEditView


app_name = 'hakusai'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('exhibitions', ExhibitionListView.as_view(), name="exhibition_list"),
    path('exhibitions/<int:exhibition_id>', ExhibitionDetailView.as_view(), name="exhibition_detail"),
    path('exhibitions/<int:exhibition_id>/run', ExhibitionRunView.as_view(), name="exhibition_run"),
    path('exhibitions/new', ExhibitionNewView.as_view(), name="exhibition_new"),

    path('projects', ProjectListView.as_view(), name="project_list"),
    path('projects/new/summary', ProjectNewSummaryView.as_view(), name="project_new_summary"),
    path('projects/new/<int:project_id>/steps', ProjectNewStepView.as_view(), name="project_new_step"),
    path('projects/edit/<int:project_id>', ProjectEditView.as_view(), name="project_edit"),
]