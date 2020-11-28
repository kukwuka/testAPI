from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os
from datetime import datetime

from .models import Answer, Question , Poll , Asked_Questions , Asked_Pools
from .serializers import PollListSerializer , PollDetailSerializer , Asked_PoolsSerializer , Asked_QuestionSerializer , Asked_Pools_CreateSerializer ,Asked_Question_CreateSerializer



class PollListView(APIView):
    def get(self, request):
        polls = Poll.objects.filter(end_date__gte = datetime.now())
        serializer = PollListSerializer(polls , many=True)
        return Response(serializer.data)



class PollDetailView(APIView):
    def get(self, request , pk):
        poll = Poll.objects.get(id = pk , end_date__gte = datetime.now())
        serializer = PollDetailSerializer(poll)
        return Response(serializer.data)


class Asked_PoolsListView(APIView):
    def get(self, request , pk):
        asked_poll = Asked_Pools.objects.filter( user_id = pk)
        
        ids = []
        for el_poll in asked_poll:
            
            serializer_poll = Asked_PoolsSerializer(el_poll)
            question_data = Asked_Questions.objects.filter(asked_pool = el_poll)
            serializer_question = Asked_QuestionSerializer(question_data, many = True)
            full_data = {
            'information' : serializer_poll.data , 
            'user_answers' : serializer_question.data , 
            }
            ids.append(full_data)

        ids = {'poll_information':ids}


        content = {
            'status': 1, 
            'responseCode' : status.HTTP_200_OK, 
            'data': ids,

        }
        return Response(content)



class Asked_PoolsCreateView(APIView):
    """Добавление отзыва к фильму"""
    def post(self, request):
        
        #Сериализатор
            data = request.data
            asked_poll = Asked_Pools_CreateSerializer( data = data)
            
                    
            if asked_poll.is_valid():
                asked_poll.save()
                

                asked_pool_id = int(os.environ["asked_pool_id"])
                data_question = []
                for  el in data['answers']:

                    el['asked_pool'] = asked_pool_id
                    if not ('text_answer' in el) :
                        el['text_answer'] = None
                        
                    else:
                        el['answer_choosed'] = None
                    data_question.append(el)

                data_for_serializer = {'answers':data_question}

                    #Сериализатор
                
                asked_question = Asked_Question_CreateSerializer( data = data_for_serializer )
                if asked_question.is_valid():
                    asked_question.save()
                    print(True)
                else:
                    print(False)
                



                return Response(status=201)



        







"""
class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)


class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})"""