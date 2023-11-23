import json
import threading
import time
from typing import Any, Dict
from django import http
from django.views.generic import TemplateView
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, InvalidArgumentException
from hakusai.models import Exhibitions, VExhibitionList, VProjectSteps
from hakusai.scraping.DriverClass import Driver

class ExhibitionRunView(TemplateView):
    template_name = 'hakusai/exhibition_run.html'
    stop_event = threading.Event()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "展示"
        id = kwargs["exhibition_id"]
        context["project_urls"] = [item.url for item in VExhibitionList.objects.filter(exhibitions_id=id)]
        context["exhibition"] = Exhibitions.objects.filter(id=id).first()
        return context

    # POST送信を受け取ったときの処理
    def post(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        data = json.loads(request.body)
        if (data["operation"] == 'start'):
            id = kwargs["exhibition_id"]
            projects = [
                item for item in VExhibitionList.objects.filter(exhibitions_id=id).order_by('exec_order')]
            scraping_thread = threading.Thread(
                target=lambda: self.scraping_start(projects), daemon=True)
            scraping_thread.start()
        elif (data["operation"] == 'stop'):
            self.scraping_stop()
        return http.JsonResponse({"res": data["operation"]})

    def scraping_start(self, projects):
        self.stop_event.clear()

        driver = Driver()
        while True:
            try:
                for project in projects:
                    steps = VProjectSteps.objects.filter(project_id=project.project_id).order_by('exec_order')        
                    driver.access_url(project.url)
                
                    for step in steps:
                        # stepの処理
                        if self.stop_event.is_set():
                            driver.end()
                            break
                        elif driver.translate_action_name(step.action_name) == 'click':
                            driver.click(step.xpath)
                        elif driver.translate_action_name(step.action_name) == 'insert':
                            driver.insert_data(step.xpath, step.action_str)
                        elif driver.translate_action_name(step.action_name) == 'insert_and_enter':
                            driver.insert_and_enter(step.xpath, step.action_str)
                        elif driver.translate_action_name(step.action_name) == 'wait':
                            driver.wait(int(step.action_str))
                        elif driver.translate_action_name(step.action_name) == 'scroll':
                            driver.scrollByElem(step.xpath)
                        else:
                            pass
                        # 2秒待機
                        time.sleep(2)

                    if self.stop_event.is_set():
                        # 終了ボタンが押されたら無限ループから抜け出す
                        break
                else:
                    continue
                break
            except NoSuchElementException:
                print(f"{step.xpath}は存在しません")
                driver.end()
                self.stop_event.set()
                break

            except InvalidArgumentException:
                print(f"{step.url}は存在しないか、起動されていません。")
                driver.end()
                self.stop_event.set()
                break

            except NoSuchWindowException:
                self.stop_event.set()
                break

    def scraping_stop(self):
        self.stop_event.set()