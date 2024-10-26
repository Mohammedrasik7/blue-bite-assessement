from django.db import models

# Model representing a batch of objects
class Batch(models.Model):
    batch_id = models.CharField(max_length=255, unique=True) 

    def __str__(self):
        return self.batch_id

# Model representing an object within a batch
class Object(models.Model):
    object_id = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='objects')

    def __str__(self):
        return self.object_id

# Model representing key-value data associated with an Object
class ObjectData(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='data')
    key = models.CharField(max_length=255)
    value = models.JSONField(null=True, blank=True)  # Allow null for values

    def __str__(self):
        return f"{self.key}: {self.value}"

