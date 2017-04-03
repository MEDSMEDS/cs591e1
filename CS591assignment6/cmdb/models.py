from django.db import models

# Create your models here.
class users(models.Model):
    User_ID  = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    PassWord = models.CharField(max_length=50)
    FirstName= models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

class tests(models.Model):
    Test_ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(users, on_delete=models.CASCADE)
    problem = models.CharField(max_length=50)
    Score   = models.IntegerField()

class IndividualProblemResults(models.Model):
    ID = models.AutoField(primary_key=True)
    Test_ID   = models.ForeignKey(tests, on_delete=models.CASCADE)
    ProblemNo = models.IntegerField()
    Operand1  = models.IntegerField()
    Operand2  = models.IntegerField()
    Operation = models.CharField(max_length=2)
    AnsweredCorrectly=models.BooleanField()