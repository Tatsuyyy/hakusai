# Generated by Django 4.1.3 on 2023-05-04 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="アクション名")),
            ],
            options={"db_table": "actions",},
        ),
        migrations.CreateModel(
            name="Exhibitions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="展示名")),
                ("memo", models.CharField(max_length=300, verbose_name="メモ")),
                ("created_date_time", models.DateTimeField(verbose_name="作成日時")),
            ],
            options={"db_table": "exhibitions",},
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="プロジェクト名")),
                ("url", models.CharField(max_length=300)),
                (
                    "draft_flag",
                    models.BooleanField(default=False, verbose_name="下書きフラグ"),
                ),
            ],
            options={"db_table": "projects",},
        ),
        migrations.CreateModel(
            name="Steps",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("xpath", models.CharField(max_length=200, verbose_name="要素xpath")),
                (
                    "action_str",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="action用文字列"
                    ),
                ),
                ("exec_order", models.PositiveIntegerField(verbose_name="順序")),
                (
                    "action",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hakusai.actions",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hakusai.projects",
                    ),
                ),
            ],
            options={"db_table": "steps",},
        ),
        migrations.CreateModel(
            name="ExhibitionSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "repeat",
                    models.PositiveIntegerField(default=1, verbose_name="繰り返し回数"),
                ),
                ("exec_order", models.PositiveIntegerField(verbose_name="順序")),
                (
                    "exhibition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hakusai.exhibitions",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hakusai.projects",
                    ),
                ),
            ],
            options={"db_table": "exhibition_settings",},
        ),
    ]