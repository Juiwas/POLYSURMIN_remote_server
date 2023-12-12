from django.db import models
import uuid
import hashlib

class TaskStatus(models.Model):
    code = models.IntegerField(unique=True)
    text = models.CharField(max_length=256)

class SwanTask(models.Model):
    hash = models.CharField(max_length=128, unique=True)
    status = models.ForeignKey(TaskStatus, null=True, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_updated = models.DateTimeField(auto_now=True)

    def getHash(self):
        salt = 'SwanTask_'
        str2hash = salt + str(self.pk) + '_' + str(uuid.uuid4().hex)
        hash_ = hashlib.md5(str2hash.encode()).hexdigest()
        return hash_

class SwanSubTask(models.Model):
    vel = models.FloatField()
    dir = models.FloatField()
    swan_task = models.ForeignKey(SwanTask, on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(TaskStatus, null=True, on_delete=models.PROTECT)