from django.db import models

# Dukaan ke samaan ke liye model - maine khud banaya hai
class KiranaItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField(default=0)
    selling_price = models.FloatField()
    cost_price = models.FloatField(default=0)
    category = models.CharField(max_length=50, default="General")

    def __str__(self):
        return f"{self.item_name}"

# Roz ka sale ka hisab
class DailySale(models.Model):
    item = models.ForeignKey(KiranaItem, on_delete=models.CASCADE)
    qty_sold = models.IntegerField()
    sold_on = models.DateTimeField(auto_now_add=True)

    def profit(self):
        return (self.item.selling_price - self.item.cost_price) * self.qty_sold

    def __str__(self):
        return f"{self.item.item_name} - {self.qty_sold} sold"