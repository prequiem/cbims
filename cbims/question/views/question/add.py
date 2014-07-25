from question.models import *
from question.forms import *
from django.shortcuts import *

def add(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/question/add_single_choice_question')
    else:
        form = QuestionForm()
    return render_to_response("question/add_question.html", locals(), context_instance = RequestContext(request))
    


    
