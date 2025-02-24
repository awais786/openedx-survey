
# lint-amnesty, pylint: disable=missing-module-docstring
import factory
from django.contrib import auth
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from factory.django import DjangoModelFactory
from lms.djangoapps.survey.models import SurveyAnswer, SurveyForm
from pytz import UTC

User = auth.get_user_model()

USER_PASSWORD = "password"


class UserFactory(factory.django.DjangoModelFactory):
    """
    Test factory for the `User` model.
    """
    id = factory.Sequence(lambda n: n + 1)
    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    is_superuser = False

    class Meta:
        model = User


class SurveyFormFactory(factory.django.DjangoModelFactory):  # lint-amnesty, pylint: disable=missing-class-docstring
    class Meta:
        model = SurveyForm

    name = 'Test Survey Form'
    form = '<form>First name:<input type="text" name="firstname"/></form>'


class SurveyAnswerFactory(factory.django.DjangoModelFactory):  # lint-amnesty, pylint: disable=missing-class-docstring
    class Meta:
        model = SurveyAnswer

    user = factory.SubFactory(UserFactory)
    form = factory.SubFactory(SurveyFormFactory)
