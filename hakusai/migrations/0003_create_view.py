
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('hakusai', '0001_initial'),
    ]

    exhibition_list_sql = """
    CREATE VIEW exhibition_list AS
    SELECT exhibitions.id AS exhibitions_id, projects.id AS project_id, exhibition_settings.repeat, projects.url, exhibition_settings.exec_order
    FROM exhibition_settings
    LEFT OUTER JOIN exhibitions
    ON exhibition_settings.exhibition_id = exhibitions.id
    LEFT OUTER JOIN projects
    ON exhibition_settings.project_id = projects.id;
    """

    exhibition_list_reverse_sql = """
    DROP VIEW IF EXISTS exhibition_list;
    """

    project_step_sql = """
    CREATE VIEW project_steps AS
    SELECT projects.id AS project_id, steps.exec_order, steps.xpath, actions.name as action_name, steps.action_str 
    FROM steps
    LEFT OUTER JOIN actions
    ON steps.action_id = actions.id
    LEFT OUTER JOIN projects
    ON steps.project_id = projects.id;
    """

    project_step_reverse_sql = """
    DROP VIEW IF EXISTS project_steps;
    """

    operations = [
        migrations.RunSQL(exhibition_list_sql, exhibition_list_reverse_sql),
        migrations.RunSQL(project_step_sql, project_step_reverse_sql),
    ]
