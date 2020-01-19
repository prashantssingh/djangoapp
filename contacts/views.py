from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'last_contact': latest_question_list}
    return render(request, 'contact/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Contact does not exist")
    return render(request, 'contact/detail.html', {'question': question})
