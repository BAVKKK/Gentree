from django.db import models


class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    name = models.CharField(255)

class Node(models.Model):
    node_id = models.AutoField(primary_key=True)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, related_name='family', null=True)
    mother_id = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='mother', null=True)
    father_id = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='father', null=True)

class Marriages(models.Model):
    marr_id = models.AutoField(primary_key=True, default=1)
    husband_id = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='husband')
    wife_id = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='wife')