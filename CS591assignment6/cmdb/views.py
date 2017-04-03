from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from cmdb import models
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
from django.db.models import Max
# Create your views here.

user_list=[
    {"user":"desheng zhang","pwd":"zala"},
    {"user":"haotian wu","pwd":"amazon"},
]
@csrf_exempt
def login(request):
    #body_unicode = request.body.decode('utf-8')
    #print(request.body)
    json_str = ((request.body).decode('utf-8'))
    body = json.loads(json_str)
    username = body['UserName']
    password = body['PassWord']
    #username = request.GET.get("name", None)
    #password = request.GET.get("password", None)
    userPassJudge = models.users.objects.filter(UserName=username, PassWord=password)
    print(userPassJudge.get(UserName=username).User_ID)
    if userPassJudge:
        return JsonResponse({'result': "true","UserID": userPassJudge.get(UserName=username).User_ID})
    else:
        return JsonResponse({'result': "false"})
    #return HttpResponse("hello sb!")
   # return JsonResponse({'name': username,'password':password})
@csrf_exempt
def create(request):
    json_str = ((request.body).decode('utf-8'))
    body = json.loads(json_str)
    data = models.users(UserName=body["UserName"],PassWord=body["PassWord"],FirstName=body["FirstName"],LastName=body["LastName"])
    data.save()
    return JsonResponse({'result': "true"})

@csrf_exempt
def top_5(request):
    data=models.tests.objects.values("User_ID").annotate(totalScore=Max("Score")).order_by("-totalScore").all()
    print(data)
    #data=models.tests.objects.order_by("-Score")
    len=min(data.__len__(),5)
    datas=[]
    for x in range(len):
        datas.append({"UserName":models.users.objects.get(User_ID=data[x]["User_ID"]).UserName, "Score":data[x]["totalScore"]})
    return JsonResponse({'result': "true","length" : len, "data" : datas } )

@csrf_exempt
def update(request):
    json_str = ((request.body).decode('utf-8'))
    body = json.loads(json_str)

    # result=models.tests.objects.filter(User_ID=body["User_ID"])
    # if result:
    #     instance1=result.get(User_ID=body["User_ID"])
    #     instance1.Score=instance1.Score+int(body["Score"])
    #     instance1.save()
    # else:
    instance=models.users.objects.filter(User_ID =  body["User_ID"] )
    data=models.tests(User_ID=instance.get(User_ID =  body["User_ID"]),problem=body["Problem"],Score=body["Score"])
    data.save()
    return JsonResponse({"result":"true","Test_ID":data.Test_ID})


@csrf_exempt
def update1(request):
    json_str = ((request.body).decode('utf-8'))
    body1 = json.loads(json_str)
    body=body1["data"]
    for x in range(0, 2):
        #print(body[x]["Test_ID"])
        instance = models.tests.objects.filter(Test_ID=body[x]["Test_ID"]).get(Test_ID=body[x]["Test_ID"])
        data=models.IndividualProblemResults(Test_ID=instance,ProblemNo=body[x]["ProblemNo"],Operand1=body[x]["Operand1"],
                                             Operand2=body[x]["Operand2"],Operation=body[x]["Operation"],AnsweredCorrectly=body[x]["AnswerCorrectly"])
        data.save()
    return JsonResponse({"result":"true"})

@csrf_exempt
def test(request):
    #print(models.tests.objects.values("User_ID").annotate(totalScore=Sum("Score")).order_by("-totalScore").all())
    #print(models.tests.objects.filter(User_ID=3).values_list("Score"))
    print(models.tests.objects.values("User_ID").annotate(MaxScore=Max("Score")).order_by("-MaxScore").all())
    return JsonResponse({"result":"true"})
#python manage.py runserver 192.168.0.100:80