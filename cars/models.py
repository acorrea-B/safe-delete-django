from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE


class Line(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE
    name = models.CharField(max_length=100)

class Car(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    name = models.CharField(max_length=100)
    line = models.ManyToManyField(Line)