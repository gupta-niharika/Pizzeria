from django.db import models

class PizzaMenu(models.Model):
    class VegNonVegChoices:
        VEG = 'Veg'
        NON_VEG = 'Non-Veg'
        
        VEG_NON_VEG_CHOICES = [
            (VEG, 'Vegetarian'),
            (NON_VEG, 'Non-Vegetarian'),
        ]
    
    class SauceChoices:
        TOMATO = 'Tomato'
        BBQ = 'BBQ'
        MARINARA = 'Marinara'
        PESTO = 'Pesto'
        PERI_PERI = 'Peri-Peri'
        MAKHANI = 'Makhani'
        
        SAUCE_CHOICES = [
            (TOMATO, 'Tomato Sauce'),
            (BBQ, 'BBQ Sauce'),
            (MARINARA, 'Marinara Sauce'),
            (PESTO, 'Pesto Sauce'),
            (PERI_PERI, 'Peri-Peri Sauce'),
            (MAKHANI, 'Makhani Sauce'),
        ]
        
    class CrustChoices:
        THIN = 'Thin'
        FRESH_PAN = 'Fresh Pan'
        CHEESE_BURST = 'Cheese Burst'
        HAND_TOSSED = 'Hand Tossed'
        
        CRUST_CHOICES = [
            (THIN, 'Thin Crust'),
            (FRESH_PAN, 'Fresh Pan Crust'),
            (CHEESE_BURST, 'Cheese Burst Crust'),
            (HAND_TOSSED, 'Hand Tossed Crust'),
        ]
        
    class ToppingChoices:
        MUSHROOMS = 'Mushrooms'
        CAPSICUM = 'Capsicum'
        ONIONS = 'Onions'
        OLIVES = 'Olives'
        SPINACH = 'Spinach'
        PANEER = 'Paneer'
        BBQ_CHICKEN = 'BBQ Chicken'
        SAUSAGE_CHICKEN = 'Sausage Chicken'
        SHREDDED_CHICKEN = 'Shredded Chicken'
        SHRIMP = 'Shrimp'
        SWEET_CORN = 'Sweet Corn'
        CHERRY_TOMATO = 'Cherry Tomato'
        BABY_CORN = 'Baby Corn'
        JALAPEÑOS = 'Jalapeños'
        
        TOPPING_CHOICES = [
            (MUSHROOMS, 'Mushrooms'),
            (CAPSICUM, 'Capsicum'),
            (ONIONS, 'Onions'),
            (OLIVES, 'Olives'),
            (SPINACH, 'Spinach'),
            (PANEER, 'Paneer'),
            (BBQ_CHICKEN, 'BBQ Chicken'),
            (SAUSAGE_CHICKEN, 'Sausage Chicken'),
            (SHREDDED_CHICKEN, 'Shredded Chicken'),
            (SHRIMP, 'Shrimp'),
            (SWEET_CORN, 'Sweet Corn'),
            (CHERRY_TOMATO, 'Cherry Tomato'),
            (BABY_CORN, 'Baby Corn'),
            (JALAPEÑOS, 'Jalapeños'),
        ]

    id = models.AutoField(primary_key=True)
    veg_non_veg = models.CharField(
        max_length=10,
        choices=VegNonVegChoices.VEG_NON_VEG_CHOICES,
        default=VegNonVegChoices.VEG,
        verbose_name="Vegetarian/Non-Vegetarian",
        help_text="Select whether the pizza is vegetarian or non-vegetarian."
    )
    pizza_name = models.CharField(max_length=100, verbose_name="Pizza Name", help_text="Enter the name of the pizza.")
    price_small = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price (Small)", help_text="Enter the price for a small pizza.")
    price_medium = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price (Medium)", help_text="Enter the price for a medium pizza.")
    price_large = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price (Large)", help_text="Enter the price for a large pizza.")
    size = models.CharField(max_length=20, verbose_name="Size", help_text="Select the size of the pizza.")
    toppings = models.CharField(max_length=255, choices=ToppingChoices.TOPPING_CHOICES, verbose_name="Toppings", help_text="Select the toppings for the pizza.", blank=True)
    crust = models.CharField(max_length=20, choices=CrustChoices.CRUST_CHOICES, verbose_name="Crust Type", help_text="Select the type of crust.")
    sauce = models.CharField(max_length=20, choices=SauceChoices.SAUCE_CHOICES, verbose_name="Sauce Type", help_text="Select the type of sauce.")
    gluten_allergen_info = models.TextField(verbose_name="Gluten/Allergen Info", help_text="Provide allergen information.")

    class Meta:
        db_table = 'pizza_menu' 

    def __str__(self):
        return self.pizza_name
