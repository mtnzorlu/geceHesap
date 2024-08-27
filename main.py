from datetime import datetime, timedelta

# Kullanıcıdan akşam ve imsak vakitlerini al
maghrib_time = input("Akşam namazı vakti --:-- (HH:MM): ")
fajr_time = input("İmsak vakti --:-- (HH:MM): ")

# Namaz vakitlerini datetime formatına çevir
maghrib = datetime.strptime(maghrib_time, "%H:%M")
fajr = datetime.strptime(fajr_time, "%H:%M")

# Eğer sabaha karşı vakit bir sonraki günse, 24 saat ekleyin
if fajr < maghrib:
    fajr += timedelta(days=1)

# Gece süresini hesapla
night_duration = fajr - maghrib

# Son üçte birini hesapla
last_third_duration = night_duration / 3

# Son üçte birin başlangıç zamanını hesapla
last_third_start = fajr - last_third_duration

# Zamanları formatla ve yazdır
print("Akşam başlangıç zamanı:", maghrib_time)
print("İmsak başlangıç zamanı:", fajr_time)
print("Gece’nin son üçte birinin başlangıç zamanı:", last_third_start.strftime("%H:%M"))
