from question.models import *
from question.forms import *
from django.shortcuts import *

def add(request):
    if request.method == 'POST':
        form = SingleChoiceQuestionForm()
        return render_to_response("question/add_single_choice_question.html", locals(), context_instance = RequestContext(request))
    else:
        form = SingleChoiceQuestionForm()
    return render_to_response("question/add_single_choice_question.html", locals(), context_instance = RequestContext(request))
    


    
