from django.db import models
from uuid import uuid4

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True

class NameMixin(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        abstract = True

hobby_categories = (
    ('sport', 'sport'),
    ('coding', 'coding'),
    ('science', 'science'),
    ('art', 'art')
)

class HobbyCategory(UUIDMixin):
    name = models.CharField(max_length=30, choices=hobby_categories, blank=False, null=False)

    class Meta:
        db_table = 'hobby_category'
 
class Hobby(UUIDMixin, NameMixin):
    category_id = models.ForeignKey(HobbyCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hobby'

class Language(UUIDMixin, NameMixin):

    class Meta:
        db_table = 'language'

class Person(UUIDMixin, NameMixin):
    age = models.IntegerField(blank=True, null=True)
    hobbies = models.ManyToManyField(Hobby, through='PersonHobby')
    languages = models.ManyToManyField(Language, through='PersonLanguage')

    class Meta:
        db_table = 'person'

class PersonHobby(UUIDMixin):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'person_hobby'
        unique_together = ('person', 'hobby')

class PersonLanguage(UUIDMixin):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'person_language'
        unique_together = ('person', 'language')
