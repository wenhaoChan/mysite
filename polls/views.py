from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# IndexView DetailView ResultsView 为泛形视图
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """返回最近发布的5个问卷 """
        # 确保了查询的结果是在当前时间之前，而不包含将来的日期
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse("this is the index of pllos")
#     return render_to_response('polls/index.html', {'latest_question_list': latest_question_list, 'request': request})
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist""Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render_to_response('polls/detail.html', {'question': question, 'request': request})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render_to_response('polls/result.html', {'question': question, 'request': request})
    # return HttpResponse("You're looking at the result of question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # 当成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect
