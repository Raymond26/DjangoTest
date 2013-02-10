from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice

def vote(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except Poll.DoesNotExist:
        raise Http404
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data.  This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))