from django.db import models

class CarChoices(models.TextChoices):
    RALLY = 'Rally', 'Rally'
    OPEN_WHEEL = 'Open-Wheel', 'Open-Wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'

