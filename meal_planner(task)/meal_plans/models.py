from django.db import models

class Day(models.Model):

    name_of_day = models.CharField(max_length=10)

    def __str__(self):
        return self.name_of_day
    
class TypeMeal(models.Model):

    meal_type = models.CharField(max_length=10)

    def __str__(self):
        return self.meal_type

class Dish(models.Model):

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    type_meal = models.ForeignKey(TypeMeal, on_delete=models.CASCADE)

    meal_descript = models.TextField()

    def __str__(self):
        return f"{self.meal_descript[:50]}..."

