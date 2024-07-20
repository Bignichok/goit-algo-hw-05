import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

with open("article_1.txt", "r", encoding='utf-8') as file:
    article_1 = file.read()

with open("article_2.txt", "r", encoding='utf-8') as file:
    article_2 = file.read()

articles = [
    {"id": 'article_1', "article": article_1, "patterns": ['Структури даних', 'Fake pattern']},
    {"id": 'article_2', "article": article_2, "patterns": ["До кожної сесії", "Fake pattern"]}
]

results = {}

def measure_time(search_func, data, pattern):
    return timeit.timeit(lambda: search_func(data, pattern), number=1)

for article in articles:
    article_id = article['id']
    data = article['article']
    results[article_id] = {}
    
    for pattern in article["patterns"]:
        boyer_moore_search_time = measure_time(boyer_moore_search, data, pattern)
        kmp_search_time = measure_time(kmp_search, data, pattern)
        rabin_karp_search_time = measure_time(rabin_karp_search, data, pattern)

        results[article_id][pattern] = {
            'boyer_moore_search': boyer_moore_search_time,
            'kmp_search': kmp_search_time,
            'rabin_karp_search': rabin_karp_search_time
        }

print(results)

def analyze_results(results):
    """
    Аналізує результати вимірювань часу виконання пошукових алгоритмів.
    
    Аргументи:
    results (dict): Словник з результатами вимірювань часу виконання.
    
    Повертає:
    dict: Словник з найшвидшими алгоритмами для кожного підрядка в кожній статті та загалом.
    """
    summary = {
        'article_1': {},
        'article_2': {},
        'overall': {'boyer_moore_search': 0, 'kmp_search': 0, 'rabin_karp_search': 0}
    }
    
    for article_id, patterns in results.items():
        for pattern, times in patterns.items():
            min_time_algo = min(times, key=times.get)
            summary[article_id][pattern] = min_time_algo
            summary['overall'][min_time_algo] += 1
    
    return summary

summary = analyze_results(results)
print(summary)
