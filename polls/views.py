from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list':latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question =get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/details.html', {'question':question})

def results(request,question_id):
    return HttpResponse(question_id)
def vote(request,question_id):
    return HttpResponse(question_id)