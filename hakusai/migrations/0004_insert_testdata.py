
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('hakusai', '0001_initial'),
        ('hakusai', '0002_initial_insert'),
    ]

    insert_sql = """
    INSERT INTO projects(name, url, draft_flag) VALUES('サンプルプロジェクト1', 'http://localhost:8000', false);
    INSERT INTO projects(name, url, draft_flag) VALUES('サンプルプロジェクト2', 'http://localhost:8000', false);
    INSERT INTO projects(name, url, draft_flag) VALUES('サンプルプロジェクト3', 'http://localhost:3000', false);
    INSERT INTO projects(name, url, draft_flag) VALUES('サンプルプロジェクト4', 'http://localhost:8888', true);

    INSERT INTO steps(xpath, action_id, exec_order, project_id) VALUES('sample/div/ul/li[2]/button', 1, 1, 1);
    INSERT INTO steps(xpath, action_id, action_str, exec_order, project_id) VALUES('sample/div/ul/li[2]/input', 2, 'sample', 2, 1);
    INSERT INTO steps(xpath, action_id, exec_order, project_id) VALUES('sample/div/button', 1, 3, 1);

    INSERT INTO exhibitions(name, memo, created_date_time) VALUES('サンプル展示1', 'メモメモメモ', date('2000-09-18'));
    INSERT INTO exhibitions(name, memo, created_date_time) VALUES('サンプル展示2', 'メモメモメモ2', date('2000-09-18'));
    INSERT INTO exhibitions(name, memo, created_date_time) VALUES('サンプル展示3', 'メモメモメモ3', date('2000-09-18'));

    INSERT INTO exhibition_settings(exhibition_id, project_id, repeat, exec_order) VALUES(1, 1, 1, 1);
    INSERT INTO exhibition_settings(exhibition_id, project_id, repeat, exec_order) VALUES(1, 2, 2, 2);
    INSERT INTO exhibition_settings(exhibition_id, project_id, repeat, exec_order) VALUES(1, 3, 1, 3);
    """

    reverse_sql = """
    DELETE FROM steps WHERE project_id IN (1);
    DELETE FROM projects WHERE name IN ('サンプルプロジェクト1', 'サンプルプロジェクト2', 'サンプルプロジェクト3', 'サンプルプロジェクト4');
    DELETE FROM exhibition_settings WHERE exhibition_id IN (1);
    DELETE FROM exhibitions WHERE name IN ('サンプル展示1', 'サンプル展示2', 'サンプル展示3');
    """

    operations = [
        migrations.RunSQL(insert_sql, reverse_sql),
    ]
