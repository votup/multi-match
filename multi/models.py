from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


# Create your models here.
    
class Candidate(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    #contest = models.ForeignKey('Contest', models.SET_NULL, blank = True, null=True)
    profile_photo = models.ImageField(upload_to='survey/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True, default=date.today)
    AFFILIATION_CHOICES = (
        ("D", "Democratic"),
        ("R", "Republican"),
        ("U", "Unafilliated"),
        ("L", "Libertarian"),
        ("N", "nonpartisan")
        )
    affiliation = models.CharField(
        max_length = 1,
        choices = AFFILIATION_CHOICES,
        blank = True,
        null = True)
    city = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    cand_website = models.URLField(max_length=200, blank=True, null=True)
    cand_facebook = models.URLField(max_length=200, blank=True, null=True)
    cand_twitter = models.URLField(max_length=200, blank=True, null=True)
    cand_insta = models.URLField(max_length=200, blank=True, null=True)
    camp_finance = models.URLField(max_length=200, blank=True, null=True)
    about_cand = RichTextField(blank=True, null=True)
    
    class Meta: 
        ordering = ['f_name', 'l_name',]
    
    def full_name(self):
        return '%s %s' % (self.f_name, self.l_name)

    def calculate_age(self):
        # import datetime
        return int((date.today() - self.birth_date).days / 365.25)
    age = property(calculate_age)

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
        return f"{self.candidate}: {self.response}"

class Cand_response(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='responses', blank = True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    cand_response = models.ForeignKey(Response, on_delete=models.CASCADE)
    #this is the candidate long response
    cand_long_response = RichTextField(blank=True, null=True)
    
    

class Voter(models.Model):
    #use automatically generated ID to return a page with responses and matches?
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_id = models.PositiveIntegerField('response id', blank=True, null=True)
    