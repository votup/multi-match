from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


    

   
class Question(models.Model):
    topic = models.TextField(max_length=255, blank=True, null=True, default='')
    description = RichTextField(blank=True, null=True)
    number = models.PositiveIntegerField('number', blank=True, null=True)
    question = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        return f"{self.question}"


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_id = models.PositiveIntegerField('response id', blank=True, null=True)
    response = models.TextField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['response_id' ]
    
    def __str__(self):
        return f"{self.question}: {self.response}"


class Candidate(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    cand_link = models.URLField(max_length=200, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    cand_response = models.ForeignKey(Response, on_delete=models.CASCADE)
    #this is the candidate long response
    cand_long_response = RichTextField(blank=True, null=True)
    

    class Meta: 
        ordering = ['f_name', 'l_name',]
    
    def full_name(self):
        return '%s %s' % (self.f_name, self.l_name)



#class Voter(models.Model):
    #use automatically generated ID to return a page with responses and matches?
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    response_id = models.PositiveIntegerField('response id', blank=True, null=True)
    