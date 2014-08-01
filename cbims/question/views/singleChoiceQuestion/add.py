from question.models import *
from question.forms import *
from django.shortcuts import *
import datetime

def add(request):
    if request.method == 'POST':
        form = SingleChoiceQuestionForm(request.POST)
        if form.is_valid():
            scq = form.save(commit = False)
            scq.save()

            question = Question()
            question.status = 2
            question.content_object = scq
            question.author = request.user
            question.last_modify = datetime.datetime.now()
            question.save()      
            return HttpResponseRedirect("/question/edit_single_choice_question/" + str(scq.id))
        
    else:
        form = SingleChoiceQuestionForm()
        return render_to_response("question/add_single_choice_question.html", locals(), context_instance = RequestContext(request))

            


    
