# 14. Oziq-ovqat yetkazib berish

class Delivery:
    def __init__(self, name, order_amount, distance_km, rate_per_km):
        self.name = name                # buyurtma nomi (Pizza, Sushi...)
        self.order_amount = order_amount  # buyurtma summasi ($)
        self.distance = distance_km     # masofa (km)
        self.rate = rate_per_km         # tarif ($/km)

    def total_cost(self):
        """Jami to‘lov = buyurtma summasi + yetkazib berish (masofa × tarif)"""
        delivery_fee = self.distance * self.rate
        return self.order_amount + delivery_fee

    def __str__(self):
        total = self.total_cost()
        delivery_fee = self.distance * self.rate
        return (f"{self.name:12} | {self.order_amount:6.2f}$ | "
                f"{self.distance:4.1f} km | {self.rate:4.2f}$/km | "
                f"yetk. {delivery_fee:5.2f}$ | jami {total:6.2f}$")


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class FoodDelivery(Delivery):
    def __str__(self):
        total = self.total_cost()
        delivery_fee = self.distance * self.rate
        return (f"🍔 {self.name:10} → {self.order_amount:5.2f}$ + "
                f"{delivery_fee:4.2f}$ ( {self.distance} km ) = {total:5.2f}$")


class GroceryDelivery(Delivery):
    def __str__(self):
        total = self.total_cost()
        delivery_fee = self.distance * self.rate
        return (f"🛒 {self.name:10} → {self.order_amount:5.2f}$ + "
                f"{delivery_fee:4.2f}$ ( {self.distance} km ) = {total:5.2f}$")


# --------------------------------------------------
# Yetkazib berish xarajatlarini chiqarish
# --------------------------------------------------

def show_delivery_orders(orders):
    print("\n" + "═" * 75)
    print("   OZIq-OVQAT / MAHSULOT YETKAZIB BERISH — XARAJATLAR   ".center(75))
    print("═" * 75)
    print("Buyurtma       | Mahsulot narxi | Masofa | Tarif/km | Yetk. haqi | Jami to‘lov")
    print("─" * 75)

    total_all = 0
    total_delivery = 0

    for order in orders:
        print(order)
        total_all += order.total_cost()
        total_delivery += (order.distance * order.rate)

    print("─" * 75)
    print(f"Jami yetkazib berish haqi:                    {total_delivery:8.2f}$")
    print(f"Umumiy to‘lov (mahsulot + yetkazish):        {total_all:8.2f}$")
    print("═" * 75 + "\n")


# Test ma'lumotlari
buyurtmalar = [
    FoodDelivery("Pizza Margherita", 22.50, 4.8, 0.60),
    FoodDelivery("Sushi Set", 18.90, 2.5, 0.60),
    GroceryDelivery("Sabzavot & meva", 35.00, 6.2, 0.45),
    FoodDelivery("Burger + kartoshka", 14.80, 1.2, 0.60),
    GroceryDelivery("Sut mahsulotlari", 28.40, 3.9, 0.45),
]

show_delivery_orders(buyurtmalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol buyurtmalaringiz:\n")
misol_buyurtmalar = [
    FoodDelivery("Pizza", 20, 5, 0.5),
    FoodDelivery("Sushi", 15, 3, 0.5),
]

show_delivery_orders(misol_buyurtmalar)
