from question.models import *
from question.forms import *
from django.shortcuts import *

def add(request):
    form = QuestionForm()
    return render_to_response("question/add_question.html", locals(), context_instance = RequestContext(request))
    
    
