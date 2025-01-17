from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from .models import Question,Choice

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list':latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # context = {
    #     'latest_question_list':latest_question_list,
    # }
    # return render(request,'polls/index.html',context)

# def detail(request, question_id):
#     question =get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/details.html', {'question':question})
#
# def results(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,'polls/results.html',
#                   {'question':question,})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/details.html',
                      {
                          'question':question,
                          'error_message': "No choice selected",
                      })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """return last 05 published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    def get_queryset(self):
        """filter questions that have yet to be published"""
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
