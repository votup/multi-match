from django.contrib import admin

# Register your models here.
from .models import Candidate, Question, Response



@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'candidate', 'response', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('number', 'question',)

