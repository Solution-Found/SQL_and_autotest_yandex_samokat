# Работа с базой данных

## Задание 1:

**SQL-запрос:**

```sql
SELECT c.login "Курьер",
       COUNT(*) "Заказы"
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;
```

**Тот же запрос для консоли:**

```sql
SELECT c.login "Курьер", COUNT(*) "Заказы" FROM "Couriers" c JOIN "Orders" o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
```

---

## Задание 2:

**SQL-запрос:**

```sql
SELECT track "Трекер",
       CASE 
           WHEN finished = true THEN 2
           WHEN canсelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END "Статусы"
FROM "Orders";
```

**Тот же запрос для консоли:**

```sql
SELECT track "Трекер", CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END "Статусы" FROM "Orders";
```