# documentation for testApi 

now used host : http://127.0.0.1:8080/
,but in production you need to use your IP-adres or domen

## Get active polls

for get active poll 
```
http://127.0.0.1:8080/api/v1/poll/
```
you will get list of active poll , like that: 
```json
[
    {
        "id": 1,
        "title": "about country",
        "start_date": "2020-11-27",
        "end_date": "2020-12-04"
    },
    {
        "id": 2,
        "title": "about money",
        "start_date": "2020-11-27",
        "end_date": "2020-12-04"
    }
]
```
save id of poll , to get questions.

## Get question in poll

to get questions from poll , you need to send get request  to :

```
http://127.0.0.1:8080/api/v1/poll/{id}

id is id of poll
id must be integer
```
you get json like that: 

```json
{
    "id": 1,
    "title": "about country",
    "questions": [
        {
            "id": 1,
            "title": "Where u live?",
            "question_type": "text_answer",
            "test_answers": []
        },
        {
            "id": 2,
            "title": "type of goverment",
            "question_type": "one_answer",
            "test_answers": [
                {
                    "title": "president",
                    "id": 1
                },
                {
                    "title": "parlament",
                    "id": 2
                },
                {
                    "title": "monarch",
                    "id": 3
                }
            ]
        },
        {
            "id": 3,
            "title": "which politican force u have?",
            "question_type": "many_answers",
            "test_answers": [
                {
                    "title": "liberal",
                    "id": 4
                },
                {
                    "title": "comunicm",
                    "id": 5
                },
                {
                    "title": "democratic",
                    "id": 6
                },
                {
                    "title": "left",
                    "id": 7
                },
                {
                    "title": "right",
                    "id": 8
                }
            ]
        }
    ],
    "start_date": "2020-11-27",
    "end_date": "2020-12-04"
}
```


in key 'questions' you have list of questions.

question will be element of list questions.

in key 'question_type' of question ,  you have type of question.

in key 'test_answers' of question ,  you have list of variant of test.

in question , you need to save id of questions and id of test_answers.


## Asking poll

to respond poll , you need send POST request to the url:

```
http://127.0.0.1:8080/api/v1/ask/
```

with json like that:

```json
{
	"user_id" : 4,
	"answer_date" : "2020-11-22",
	"pool": 1,
	"answers" : [{
		"question": 1,
		"text_answer":"Moscow"
		          } ,
		         {
		"question": 2,
		"answer_choosed":2
				},
				{
		"question": 3,
		"answer_choosed":[5,7]
				}]

}
```
required field is 'user_id' and 'pool'.

The type of feild 'answer'  must list.

if type of question is "one_answer" , the 'answer_choosed' must be integer and  must be include test answer , otherwise will not accept your answer.

if type of question is "many_answers" , the 'answer_choosed' must be list od integer and must be include test answer , otherwise will not accept your answer.

## Information about answers

to get your your answer request to url :
```
http://127.0.0.1:8080/api/v1/userpoll/{user_id}
```

user_is is your user id

requset'll return you dictionary , in key 'data' will be all inforamation , 
like that :

```json
{
    "status": 1,
    "responseCode": 200,
    "data": {
        "poll_information": [
            {
                "information": {
                    "user_id": 89,
                    "answer_date": "2020-11-22",
                    "pool": {
                        "id": 1,
                        "title": "about country",
                        "start_date": "2020-11-27",
                        "end_date": "2020-12-04"
                    }
                },
                "user_answers": [
                    {
                        "question": {
                            "title": "Where u live?",
                            "question_type": "text_answer"
                        },
                        "answer_choosed": [],
                        "text_answer": "Moscow"
                    },
                    {
                        "question": {
                            "title": "type of goverment",
                            "question_type": "one_answer"
                        },
                        "answer_choosed": [
                            {
                                "title": "parlament",
                                "id": 2
                            }
                        ],
                        "text_answer": null
                    },
                    {
                        "question": {
                            "title": "which politican force u have?",
                            "question_type": "many_answers"
                        },
                        "answer_choosed": [
                            {
                                "title": "comunicm",
                                "id": 5
                            },
                            {
                                "title": "left",
                                "id": 7
                            }
                        ],
                        "text_answer": null
                    }
                ]
            }
        ]
    }
}
```
in poll_information will be list of asked polls .

asked_poll will be element of poll_information.
in key 'poll'  in asked_poll you will get information about poll.
in key 'user_answers'  in asked_poll you will get information about asked questions .
in user_answers will be list .
in each element of list you will meet key 'question' and 'answer_choosed' 'text_answer' ,about information in each one .
