from website.models import *
from website.forms import *
from django.shortcuts import *
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.save()
            return HttpResponse("success!")
    else:
        form = TagForm()
    return render_to_response("website/add_tag.html", locals(), context_instance=RequestContext(request))
