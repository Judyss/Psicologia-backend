"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from planillas.resources.city import CityViewSet
from planillas.resources.people import PeopleViewSet
from planillas.resources.academicUnit import AcademicUnitViewSet
from planillas.resources.account import AccountViewSet
from planillas.resources.academicMethod import AcademicMethodViewSet
from planillas.resources.semester import SemesterViewSet
from planillas.resources.specialty import SpecialtyViewSet
from planillas.resources.student import StudentViewSet
from planillas.resources.account import LoginView, LogoutView, AccountDetailViewSet
from emiForms.resources.form import FormViewSet
from emiForms.resources.question import QuestionViewSet, FormQuestionViewSet
from emiForms.resources.answer import AnswerViewSet, AnswerDetailViewSet
from emiForms.resources.form_enabled import FormEnabledViewSet
from emiForms.resources.send_list import SendListViewSet
# from emiForms.resources.question import QuestionFormApiView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'AcademicMethod', AcademicMethodViewSet)
router.register(r'AcademicUnit', AcademicUnitViewSet)
router.register(r'Account', AccountViewSet)
router.register(r'AccountDetail', AccountDetailViewSet)
router.register(r'City', CityViewSet)
router.register(r'People', PeopleViewSet)
router.register(r'Semester', SemesterViewSet)
router.register(r'Specialty', SpecialtyViewSet)
router.register(r'Student', StudentViewSet)

routerForms = routers.DefaultRouter()
routerForms.register(r'Form', FormViewSet, base_name='Form')
routerForms.register(r'Question', QuestionViewSet, base_name='Question')
routerForms.register(r'FormEnabled', FormEnabledViewSet, base_name='FormEnabled')
routerForms.register(r'FormQuestion', FormQuestionViewSet, base_name='FormQuestion')
routerForms.register(r'Answer', AnswerViewSet, base_name='Answer')
routerForms.register(r'AnswerDetail', AnswerDetailViewSet, base_name='AnswerDetail')
routerForms.register(r'SendList', SendListViewSet, base_name='SendList')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^Forms/', include(routerForms.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^Login/', LoginView.as_view(), name="login"),
    url(r'^Logout/', LogoutView.as_view(), name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
