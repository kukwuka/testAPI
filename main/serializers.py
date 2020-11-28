from rest_framework import serializers
from .models import Answer, Question , Poll , Asked_Questions , Asked_Pools
import datetime
import os


class AnswerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Answer
		fields = ("title", "id")

class QuestionListSerializer(serializers.ModelSerializer):
	test_answers = AnswerListSerializer(many=True, read_only=True)

	class Meta:
		model = Question
		fields = ("id" , "title" , "question_type", "test_answers" )








class PollListSerializer(serializers.ModelSerializer):
	

	
	class Meta:
		model = Poll
		fields = ("id" , "title" ,  "start_date" , "end_date")






class PollDetailSerializer(serializers.ModelSerializer):
	

	questions = QuestionListSerializer( many=True)
	class Meta:
		model = Poll
		fields = ("id" , "title" , "questions", "start_date" , "end_date")


#Asked




class QuestionTitleSerializer(serializers.ModelSerializer):


	class Meta:
		model = Question
		fields = ("title" ,"question_type" )



class Asked_QuestionSerializer(serializers.ModelSerializer):

	question = QuestionTitleSerializer()
	answer_choosed  = AnswerListSerializer(many = True)
	class Meta:
		model = Asked_Questions
		fields = ("question" , "answer_choosed", "text_answer")



class Asked_PoolsSerializer(serializers.ModelSerializer):
	
	"""id = fields.ReadOnlyField()
	object_poll = Asked_Pools.objects.get (id = id) 
	question_data = Asked_Questions.objects.filter( asked_pool = object_poll)
	serializer_question = sked_QuestionSerializer(question_data, many=True)"""
	pool = PollListSerializer()
	class Meta:
		model = Asked_Pools
		fields = ("user_id" ,  "answer_date" , "pool",)













#create
class Asked_Pools_CreateSerializer(serializers.ModelSerializer):
	
	"""id = fields.ReadOnlyField()
	object_poll = Asked_Pools.objects.get (id = id) 
	question_data = Asked_Questions.objects.filter( asked_pool = object_poll)
	serializer_question = sked_QuestionSerializer(question_data, many=True)"""

	class Meta:
		model = Asked_Pools
		fields = ("user_id" , "answer_date" , "pool", )


	def create(self, validated_data):
		print("inserializerpoll")
		
		user_id = validated_data["user_id"]
		answer_date = validated_data["answer_date"]
		
		pool = validated_data["pool"]

		
		#print( validated_data )
		new_asked_poll = Asked_Pools(user_id = user_id, answer_date = answer_date , pool = pool)
		

		new_asked_poll.save()
			
		os.environ["asked_pool_id"] = str(new_asked_poll.id)
			
		return new_asked_poll
		


class Asked_Question_CreateSerializer(serializers.ModelSerializer):

	answers = serializers.JSONField()
	class Meta:
		model = Asked_Questions
		fields = ("answers" , )



	def create(self, validated_data):
		print("data")
		print( validated_data['answers'])
		
		all_answers = validated_data['answers']
		for answer in all_answers:

			print('')
			print(answer)

			question = None
			answer_choosed = None
			text_answer = None
			asked_pool = None


			question = Question.objects.get(id = answer['question'])

			answer_choosed = answer['answer_choosed']
			
			text_answer = answer['text_answer']
			asked_pool = Asked_Pools.objects.get(id = answer['asked_pool'])		


			new_asked_question = Asked_Questions(
					question =  question,
					text_answer = text_answer,
					asked_pool = asked_pool,
					)
				
			
			new_asked_question.save()
			test_variant = []
			if isinstance(answer_choosed,list) :
				print('list')

			if 	new_asked_question.question.question_type == 'text_answer':
				continue


			for ans in new_asked_question.question.test_answers.all():
				test_variant.append(ans.id)
			print('')
			print(answer_choosed)


			check = True
			if isinstance(answer_choosed,int) :
				check = (answer_choosed in test_variant) and check
			else :
				for answer_check in answer_choosed:
					check = (answer_check in test_variant) and check

				



			


			

			if check:

				if 	new_asked_question.question.question_type == 'one_answer':
					el_choosed = Answer.objects.get(id = answer_choosed)
					new_asked_question.answer_choosed.add(el_choosed)
					print('one_answer')
				elif new_asked_question.question.question_type == 'many_answers':
					print('many_answers_start')
					for variant in answer_choosed:
						print('variant')
						print(variant)
						el_choosed = Answer.objects.get(id = variant) 
						new_asked_question.answer_choosed.add(el_choosed)
						print('many_answers')


			else: 
				new_asked_question.delete()
				continue

			
			new_asked_question.save()
			



			


				
		return new_asked_question





"""
		 validated_data["answers"]
		print("creating")

		for el in question_list:


			el_answer_choosed = None
			el_text_answer = None

			el_question = el["question_id"]
			try:
				el_answer_choosed = el["answer_choosed_id"]
			except Exception as e:
				el_text_answer = el["text_answer"]

			print(el_question)
			print(el_question)

			new_asked_question = Asked_Questions(
				question =  Question.objects.get(id = el_question) ,
				answer_choosed = Answer.objects.get(id = el_answer_choosed) ,
				text_answer = el_text_answer,
				asked_pool = new_asked_poll,
				)










class Asked_PoolsSerializer(serializers.ModelSerializer):
	

	questions = Asked_QuestionSerializer( many=True)




	class Meta:
		model = Asked_Pools
		fields = ("user_id" ,  "answer_date" , "pool", "questions")
	




	def create(self, validated_data):
		user_id = validated_data["user_id"]
		answer_date = datetime.strptime( validated_data["answer_date"], "%Y-%m-%d").date()
		pool = Poll.ovalidated_dataobjects.get(id = ["pool"] )
		
		new_asked_poll = Asked_Pools(user_id = user_id, answer_date = answer_date , pool = pool)

		new_asked_poll.save()

		question_list  = validated_data["questions"]

		for el in question_list:



			el_question = el["question"]
			el_answer_choosed = el["answer_choosed"]
			el_text_answer = el["text_answer"]



			new_asked_question = Asked_Questions(
				question =  el_question ,
				answer_date = el_answer_date,
				text_answer = el_text_answer,
				asked_pool = new_asked_poll
				)"""











