from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse


def execute_custom_sql(query):
    with connections['default'].cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return results


def get_data(request):
    query = "SELECT * FROM myapp_data"
    data = execute_custom_sql(query)
    response_data = [{'id': row[0], 'content': row[1]} for row in data]
    return JsonResponse(response_data, safe=False)
