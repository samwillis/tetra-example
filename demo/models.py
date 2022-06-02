from django.db import models


class ToDo(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    title = models.CharField(max_length=80)
    done = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
