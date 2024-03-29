from django.utils import timezone
from django.db import models
from django.db.models import Model

# Create your models here.
class Actions(Model):
    name = models.CharField(max_length=100, verbose_name='アクション名')

    class Meta:
        db_table = 'actions'

class Projects(Model):
    name = models.CharField(max_length=100, verbose_name='プロジェクト名')
    url = models.CharField(max_length=300)
    delete_flag = models.BooleanField(default=False, verbose_name='削除フラグ')
    draft_flag = models.BooleanField(default=False, verbose_name='下書きフラグ')

    class Meta:
        db_table = 'projects'

class Steps(Model):
    xpath = models.CharField(max_length=200, verbose_name='要素xpath')
    action = models.ForeignKey('actions', on_delete=models.CASCADE)
    action_str = models.CharField(max_length=100, null=True, blank=True, verbose_name='action用文字列')
    exec_order = models.PositiveIntegerField(verbose_name='順序')
    project = models.ForeignKey('projects', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'steps'

class Exhibitions(Model):
    name = models.CharField(max_length=100, verbose_name='展示名')
    memo = models.CharField(max_length=300, null=True, verbose_name='メモ')
    created_date_time = models.DateTimeField(verbose_name='作成日時')
    delete_flag = models.BooleanField(default=False, verbose_name='削除フラグ')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date_time = timezone.now()  # 新規作成時の時刻を保存
        return super(Exhibitions, self).save(*args, **kwargs)

    class Meta:
        db_table = 'exhibitions'

class ExhibitionSettings(Model):
    exhibition = models.ForeignKey(
        'exhibitions', on_delete=models.CASCADE)
    project = models.ForeignKey('projects', on_delete=models.CASCADE)
    repeat = models.PositiveIntegerField(verbose_name='繰り返し回数', default=1)
    exec_order = models.PositiveIntegerField(verbose_name='順序')

    class Meta:
        db_table = 'exhibition_settings'

# DBView
class VProjectSteps(Model):
    project_id = models.BigIntegerField(primary_key=True)
    exec_order = models.PositiveIntegerField()
    xpath = models.CharField(max_length=200)
    action_name = models.CharField(max_length=100)
    action_str = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'project_steps'

class VExhibitionList(Model):
    exhibitions_id = models.BigIntegerField(primary_key=True)
    project_id = models.BigIntegerField()
    project_name = models.CharField(max_length=100)
    repeat = models.PositiveIntegerField()
    url = models.CharField(max_length=300)
    exec_order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'exhibition_list'

