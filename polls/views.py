from .models import Question
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, id):
    # try:
    #     question = Question.objects.get(pk=id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # Skrót do tego co powyżej
    question = get_object_or_404(Question, pk=id)

    context = {
        "question": question,
    }
    return render(request, "polls/detail.html", context)


def results(request, id):
    response = f"You're looking at the results of question {id}"
    return HttpResponse(response)


def vote(request, id):
    return HttpResponse(f"You are voting on question {id}")
