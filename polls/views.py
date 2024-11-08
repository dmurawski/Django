from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print(latest_question_list)
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    return HttpResponse(f"question {id}")


def results(request, id):
    response = f"You're looking at the results of question {id}"
    return HttpResponse(response)


def vote(request, id):
    return HttpResponse(f"You are voting on question {id}")
