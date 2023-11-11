
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('hakusai', '0001_initial'),
    ]
    action_insert_sql = """
    INSERT INTO actions(name) VALUES('クリック');
    INSERT INTO actions(name) VALUES('文字入力');
    INSERT INTO actions(name) VALUES('文字入力後Enter');
    INSERT INTO actions(name) VALUES('待つ');
    INSERT INTO actions(name) VALUES('スクロール');
    """

    action_insert_reverse_sql = """
    DELETE FROM actions WHERE name IN ('クリック', '文字入力', '文字入力後Enter', '待つ', 'スクロール');
    """

    operations = [
        migrations.RunSQL(action_insert_sql, action_insert_reverse_sql),
    ]
