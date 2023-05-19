from django.db import models


# all data related to the animal
class Animal(models.Model):
    GENDER_CHOICES = (("F", "Female"),("M", "Male")) # possible gender choices for gender variable
    identification = models.CharField(max_length=100) # any kind of animal identification (name, number, alias, etc)
    species = models.CharField(max_length=100) # bovine, equine, caprine, swine, etc
    breed = models.CharField(max_length=100) # red angus, mustang, boer, etc
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) # M -> male, F -> female
    category = models.CharField(max_length=100) # adult/cub form each species
    weight = models.FloatField() # animal weight in kilograms
    birth_date = models.DateField() # approximate birth date

    def __str__(self):
        return self.identification


# all data related to the animal health
class Health(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE) # animal id
    type = models.CharField(max_length=100) # vaccine, shot, procedure, etc
    description = models.CharField(max_length=100) # name or other relevant description (anti-rabies, vermifuge "X", castration, insemination, etc)
    date = models.DateField() # date it was performed
    comments = models.TextField() # any important comments related to the animal, the procedure or incidents

    def __str__(self) -> str:
        return str(self.animal)
