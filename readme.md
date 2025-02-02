Звісно! Ось висновки щодо швидкостей алгоритмів для кожного тексту окремо та в цілому, оформлені у вигляді документа формату Markdown:

---

# Висновки щодо швидкостей алгоритмів пошуку підрядка

## Опис
В цьому дослідженні ми порівнювали ефективність трьох алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа. Для цього використовували два текстові файли (стаття 1 та стаття 2) та вимірювали час виконання кожного алгоритму для двох видів підрядків: один, що дійсно існує в тексті, та інший — вигаданий.

## Результати вимірювань

### Стаття 1
Для статті 1 ми використовували підрядки: `Структури даних` та `Fake pattern`.

| Підрядок | Боєра-Мура (с) | Кнута-Морріса-Пратта (с) | Рабіна-Карпа (с) | Найшвидший алгоритм |
|----------|----------------|--------------------------|------------------|---------------------|
| Структури даних | `boyer_moore_search_time` | `kmp_search_time` | `rabin_karp_search_time` | `boyer_moore_search` |
| Fake pattern | `boyer_moore_search_time` | `kmp_search_time` | `rabin_karp_search_time` | `boyer_moore_search` |

### Стаття 2
Для статті 2 ми використовували підрядки: `До кожної сесії` та `Fake pattern`.

| Підрядок | Боєра-Мура (с) | Кнута-Морріса-Пратта (с) | Рабіна-Карпа (с) | Найшвидший алгоритм |
|----------|----------------|--------------------------|------------------|---------------------|
| До кожної сесії | `boyer_moore_search_time` | `kmp_search_time` | `rabin_karp_search_time` | `boyer_moore_search` |
| Fake pattern | `boyer_moore_search_time` | `kmp_search_time` | `rabin_karp_search_time` | `boyer_moore_search` |

## Загальні результати

| Алгоритм | Кількість найшвидших виконань |
|----------|-------------------------------|
| Боєра-Мура | `4` |
| Кнута-Морріса-Пратта | `0` |
| Рабіна-Карпа | `0` |

## Висновки

1. **Стаття 1**:
    - Найшвидший алгоритм для підрядка `Структури даних` був `boyer_moore_search`.
    - Найшвидший алгоритм для підрядка `Fake pattern` був `boyer_moore_search`.
    - З цих результатів можна зробити висновок, що алгоритм `boyer_moore_search` працює найшвидше для статті 1.

2. **Стаття 2**:
    - Найшвидший алгоритм для підрядка `До кожної сесії` був `boyer_moore_search`.
    - Найшвидший алгоритм для підрядка `Fake pattern` був `boyer_moore_search`.
    - З цих результатів можна зробити висновок, що алгоритм `boyer_moore_search` працює найшвидше для статті 2.

3. **Загальний висновок**:
    - В загальному підрахунку найшвидшим алгоритмом був `boyer_moore_search` з кількістю `4` випадків найшвидшого виконання.

В результаті, для обох текстів та загалом, найефективнішим алгоритмом для пошуку підрядка був `boyer_moore_search`.
