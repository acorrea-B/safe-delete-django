from django.utils import timezone
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Line(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)

class Car(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=100)
    line = models.ManyToManyField(Line)


class SoftDelete(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull = True)
    
    def get_deleted(self):
        return super().get_queryset().filter(deleted_at__isnull = False)

    def all_with_deleted(self):
        return super().get_queryset().filter()

class BaseModel(models.Model):

    deleted_at = models.DateTimeField(blank = True, null = True)
    objects = SoftDelete()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
       
class Line2(BaseModel):
    name = models.CharField(max_length=100)
    
class Car2(BaseModel):
    
    name = models.CharField(max_length=100)
    line = models.ManyToManyField(Line2)