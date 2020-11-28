import datetime
import django.utils.timezone
from django.db import models
from django.conf import settings

class Answer(models.Model):
    title = models.CharField(max_length=4096)
   

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=4096)
    type_list = (      

   
        ('one_answer', 'one answer'),
        ('many_answers', 'many answers'),
        ('text_answer', 'text answer'),


    )
    question_type = models.CharField(max_length = 15 ,  choices = type_list , default = 1)
    test_answers = models.ManyToManyField(Answer, blank = True)

    

    def __str__(self):
        return self.title

class Poll(models.Model):


	title = models.CharField(max_length=4096)
	questions = models.ManyToManyField(Question)
	start_date = models.DateField(default = django.utils.timezone.now)
	end_date = models.DateField(default = datetime.date.today() + datetime.timedelta(days = 7))

	def __str__(self):
		return self.title



class Asked_Pools(models.Model):
	user_id = models.PositiveIntegerField()
	answer_date = models.DateField(default =  django.utils.timezone.now)
	pool = models.ForeignKey(Poll , on_delete = models.DO_NOTHING)
	
	def __str__(self):
		return str(self.pool) + str(self.id)





class Asked_Questions(models.Model):
	question = models.ForeignKey(Question , on_delete=models.DO_NOTHING )
	answer_choosed = models.ManyToManyField(Answer , default = django.utils.timezone.now)
	text_answer = models.TextField( blank = True , null =True)
	asked_pool = models.ForeignKey(Asked_Pools , on_delete=models.DO_NOTHING )
	
	def __str__(self):
		return str(self.question.title) + str(self.id)




