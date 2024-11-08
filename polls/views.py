from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.db.models import F
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,)),
        )
