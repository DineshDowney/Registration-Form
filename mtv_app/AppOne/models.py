from django.db import models

class Roll_Number(models.Model):
    Roll_Num=models.IntegerField(unique=True,null=True)
    def __str__(self):
       return str(self.Roll_Num)

class AccessRec(models.Model):
    Name=models.CharField(max_length=512,null=True)
    RollNumber=models.ForeignKey(Roll_Number,on_delete="",null=True)
    message=models.CharField(max_length=512,null=True)
    def __str__(self):
        return str(self.message)
