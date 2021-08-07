from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


from .models import Candidate, Question, Response, Voter

def index(request):
  candidate_list = Candidate.objects.all()
  question_list = Question.objects.all().order_by('number')
  response_list = Response.objects.all().order_by('description', 'response')
  template_name = 'multi/index.html'
  context = {
    'candidate_list': candidate_list,
    'question_list': question_list,
    'response_list': response_list,
    }
  return render(request, template_name, context)


def about(request):
    return render(request, 'about.html')    


class CandidateDetailView(DetailView):
  model = Candidate
  template_name = 'multi/candidate_detail.html'

  def get_context_data(self, **kwargs):
         context = super(CandidateDetailView, self).get_context_data(**kwargs)
         return context


