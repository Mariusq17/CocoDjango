from django.db import models
from django.db.models import SET_NULL, ForeignKey


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25, default="user1234")
    start_date = models.DateField(auto_now_add=True)
    position = models.CharField(max_length=50, default="Noob")
    my_buddy = models.ForeignKey('self', on_delete=SET_NULL, null=True, blank=True)
    available = models.BooleanField(default=False)
    # last_time_online = models.DateTimeField(auto_now=True, null=True)
    last_time_online = models.DateTimeField(null=True, blank=True)
    salary = models.IntegerField(default=2000)

    def __str__(self):
        return self.name


class Language(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# În Django, comportamentul on_delete asociat cu un câmp ForeignKey definește ce se întâmplă
# atunci când obiectul la care se face referință este șters. La nivel general, iată cum funcționează:
#
# on_delete=models.CASCADE:
#
# Când obiectul referit (de exemplu, un Employee sau un Language) este șters, toate instanțele
# din tabela care conține ForeignKey (în cazul tău, LangaugesUsed) care fac referință la obiectul
# respectiv vor fi, de asemenea, șterse. Acest lucru se aplică doar pentru tabela LangaugesUsed,
# nu pentru tabelele originale Employee sau Language.
# Trigger-ul:
#
# Trigger-ul are loc atunci când o instanță dintr-o tabelă este ștearsă. Dacă un Employee este
# șters din tabela Employee, toate intrările corespunzătoare din LangaugesUsed care au același
# employee vor fi șterse.
# Astfel, dacă ștergi un Employee, vor dispărea și toate înregistrările din LangaugesUsed care
# se referă la acel Employee. Similar, dacă ștergi un Language, vor fi șterse toate intrările din
# LangaugesUsed care se referă la acel Language.
#
# Dacă ai nevoie de mai multe detalii sau de un alt tip de comportament (spre exemplu,
# SET_NULL sau PROTECT), comunică-mi, și te pot ajuta cu explicații suplimentare!

class LanguagesUsed(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('employee', 'language'),)

    def __str__(self):
        return f"{self.employee.name} - {self.language.title}"
