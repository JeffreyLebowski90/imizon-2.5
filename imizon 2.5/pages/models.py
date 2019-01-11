from django.db import models

# Create your models here.

class Post(models.Model):
    m_equipment_type = models.CharField(max_length=100, default='empty')
    m_size = models.CharField(max_length=100, default='empty')
    m_bore = models.CharField(max_length=100, default='empty')
    m_pressure_rating = models.CharField(max_length=100, default='empty')
    m_end_connection = models.CharField(max_length=100, default='empty')
    m_vessel_material = models.CharField(max_length=100, default='empty')
    m_trim_material = models.CharField(max_length=100, default='empty')
    m_bolting = models.CharField(max_length=100, default='empty')
    m_operation = models.CharField(max_length=100, default='empty')
    m_design = models.CharField(max_length=100, default='empty')
    m_vessel_seal = models.CharField(max_length=100, default='empty')
    m_trim_seal = models.CharField(max_length=100, default='empty')
    m_leakage_class = models.CharField(max_length=100, default='empty')
    m_fire_safe = models.CharField(max_length=100, default='empty')
    m_nace_requirement = models.CharField(max_length=100, default='empty')
    m_option_one = models.CharField(max_length=100, default='empty')
    m_option_two = models.CharField(max_length=100, default='empty')
    shipping = models.CharField(max_length=100, default='empty')
    shipping_arr = models.CharField(max_length=100, default='empty')
    deliver = models.CharField(max_length=100, default='empty')
    def __str__(self):
        return "Post"