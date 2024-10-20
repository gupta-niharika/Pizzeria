from django.db import models
from django.utils.translation import gettext_lazy as _

class SizePrice(models.Model):
    class SizeChoices(models.TextChoices):
        SMALL = 'small', _('Small')
        MEDIUM = 'medium', _('Medium')
        LARGE = 'large', _('Large')

    size = models.CharField(max_length=6, choices=SizeChoices.choices, verbose_name=_('Size'), help_text=_('Select the size of the pizza.'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'), help_text=_('Enter the price for the selected size.'))

    def __str__(self):
        return f"{self.size} - ${self.price}"

class PizzaMenu(models.Model):
    class DietaryTypeChoices(models.TextChoices):
        VEG = 'veg', _('Vegetarian')
        NOVEG = 'noveg', _('Non-Vegetarian')

    class CrustChoices(models.TextChoices):
        THIN = 'thin', _('Thin')
        HAND_TOSSED = 'hand_tossed', _('Hand Tossed')
        FRESH_PAN = 'fresh_pan', _('Fresh Pan')
        CHEESE_BURST = 'cheese_burst', _('Cheese Burst')

    class SauceChoices(models.TextChoices):
        MARINARA = 'marinara', _('Marinara')
        TOMATO = 'tomato', _('Tomato')
        BBQ = 'bbq', _('BBQ')
        PESTO = 'pesto', _('Pesto')
        MAKANI = 'makhani', _('Makhani')
        PERI_PERI = 'peri_peri', _('Peri-Peri')

    class ToppingChoices(models.TextChoices):
        MUSHROOM = 'mushroom', _('Mushroom')
        BABY_CORN = 'baby_corn', _('Baby Corn')
        SWEET_CORN = 'sweet_corn', _('Sweet Corn')
        JALAPENOS = 'jalapenos', _('Jalapeños')
        PEPPERS = 'peppers', _('Peppers')
        ONION = 'onion', _('Onion')
        TOMATO = 'tomato', _('Tomato')
        PINEAPPLE = 'pineapple', _('Pineapple')
        BBQ_CHICKEN = 'bbq_chicken', _('BBQ Chicken')
        CHICKEN_SAUSAGE = 'chicken_sausage', _('Chicken Sausage')
        SHRIMP = 'shrimp', _('Shrimp')
        PEPPERONI = 'pepperoni', _('Pepperoni')

    id = models.AutoField(primary_key=True, verbose_name=_('Pizza ID'), help_text=_('Unique identifier for each pizza entry.'))
    dietary_type = models.CharField(max_length=6, choices=DietaryTypeChoices.choices, verbose_name=_('Dietary Type'), help_text=_('Select whether the pizza is vegetarian or non-vegetarian.'))
    pizza_name = models.CharField(max_length=100, verbose_name=_('Pizza Name'), help_text=_('Enter the name of the pizza.'))
    size_price = models.ForeignKey(SizePrice, on_delete=models.CASCADE, verbose_name=_('Size and Price'), help_text=_('Select the size and price for the pizza.'))
    toppings = models.CharField(max_length=50, choices=ToppingChoices.choices, verbose_name=_('Toppings'), help_text=_('Select toppings for the pizza.'), blank=True)
    crust = models.CharField(max_length=12, choices=CrustChoices.choices, verbose_name=_('Crust Type'), help_text=_('Select the type of crust for the pizza.'))
    sauce = models.CharField(max_length=10, choices=SauceChoices.choices, default=SauceChoices.TOMATO, verbose_name=_('Sauce Type'), help_text=_('Select the type of sauce for the pizza.'))
    gluten_allergen_info = models.TextField(blank=True, verbose_name=_('Gluten/Allergen Info'), help_text=_('Provide gluten and allergen information (optional).'))

    class Meta:
        db_table = 'pizza_menu'

    def __str__(self):
        return f"{self.pizza_name} - {self.size_price.size} - {self.dietary_type}"
