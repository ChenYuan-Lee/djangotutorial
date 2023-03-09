from django.http import HttpResponse

from .models import Question


def index(request) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    return HttpResponse(output)

def detail(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
