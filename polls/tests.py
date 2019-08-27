import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import *

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        func: was_published_recently
        :return: False for questions whose pub_date >now()
        """
        time = timezone.now() +datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False
        for questions whose pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() return True
        for questions whose pub_date is within 1 day of now()
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text,days_num):
    """
    create a question with given question_text and
    published said question in days_num from now
    :param days_num: time offset (days) to publish the question
    :return: True if success
    """
    time = timezone.now() + datetime.timedelta(days= days_num)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
         if no question exists, display error message
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with pub_date <now() are display on the index
        :return:
        """
        create_question(question_text="Past Question",days_num= -2)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [
                '<Question: Past Question>'
            ]
        )

    def test_future_question(self):
        """
        Question with pub_date >now() is not displayed in index
        :return:
        """
        create_question(question_text="Future question",days_num=2)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_future_and_past_question(self):
        """
        only past question is displayed
        :return:
        """
        create_question("past", -2)
        create_question("future", 2)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [
                '<Question: past>'
            ]
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days_num=-30)
        create_question(question_text="Past question 2.", days_num=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        detail view of future questions return 404
        :return: Http404 if pub_date >now()
        """
        future_question = create_question("future", 2)
        url = reverse('polls:details', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        detail view of past questions return question text
        :return:
        """
        past_question = create_question('past', -2)
        url = reverse('polls:details', args= (past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)