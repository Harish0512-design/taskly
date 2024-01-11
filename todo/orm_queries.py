
# tasks_queryset = Task.objects.all()

# queryset : set of objects in db

# <QuerySet [<Task: Complete Django- # 1>, <Task: Environments- # 2>, <Task: Docker- # 3>, <Task: Kubernates- # 4>, <Task: Django Rest Framework- # 5>, <Task: Jwt Token- # 6>]>

# single_task_obj = Task.objects.get(id=3)
# <Task: Docker- # 3>

# __contains like this : called as FieldLookups

# filtered_queryset = Task.objects.filter(content__contains = "Django")
# filtered_queryset = Task.objects.filter(content__icontains = "Django")

# filtered_queryset = Task.objects.filter(content__startswith = "Django")
# filtered_queryset = Task.objects.filter(content__istartswith = "Django")

# filtered_queryset = Task.objects.filter(content__endswith = "Django")
# filtered_queryset = Task.objects.filter(content__iendswith = "Django")

# filtered_queryset = Task.objects.filter(id__in=[3,4,5])

# filtered_queryset = Task.objects.filter(id__gt = 2)
# filtered_queryset = Task.objects.filter(id__gte = 2)

# filtered_queryset = Task.objects.filter(id__lt = 2)
# filtered_queryset = Task.objects.filter(id__lte = 2)

# filtered_queryset = Review.objects.filter(date_posted__isnull=True)

# filtered_queryset = Task.objects.filter(date_posted__year = 2024)
# filtered_queryset = Task.objects.filter(date_posted__month = 1)
# filtered_queryset = Task.objects.filter(date_posted__day = 11)

# filtered_queryset = Task.objects.filter(date_posted__date = datetime.date(2024, 1, 11))
# filtered_queryset = Task.objects.filter(date_posted__date_gt = datetime.date(2024, 1, 11))

# filtered_queryset = Task.objects.filter(date_posted__hour = 3)
# filtered_queryset = Task.objects.filter(date_posted__minute = 3)
# filtered_queryset = Task.objects.filter(date_posted__second = 3)


# FieldLookUps on single object

# queryset_obj = Task.objects.get(id__exact=14)
# queryset_obj = Task.objects.get(title__iexact="Django")

# queryset_obj = Review.objects.get(task__title__contains = "Django")


# queryset_obj = Task.objects.get(title__regex=r'^(An?|The) +')
# queryset_obj = Task.objects.get(title__iregex=r'^(An?|The) +')


# Note:
# query_obj_address = single_task_obj.query (or) tasks_queryset.query
# sql_limit_time = connection.queries
# o/p: [{'sql': 'SELECT "todo_task"."id", "todo_task"."date_updated", "todo_task"."title", "todo_task"."content", "todo_task"."date_posted" FROM "todo_task" WHERE "todo_task"."id" = 2 LIMIT 21', 'time': '0.016'}]



# IF I want to perform Complex LookUps or condition checking then use 'Q' Objects

# OR:
# Task.objects.get(Q(id__exact = 1) | Q(title__iexact = "django"))

# AND:
# Task.objects.get(Q(id__exact = 1) & Q(title__iexact = "django"))

# NOT:
# Task.objects.filter(~Q(id__exact = 1))


# limit, exclude(), order_by(), distinct(), values(), values_list()

# Task.objects.all()[:10]
# Task.objects.exclude(Q(title__icontains = "django") | Q(id=2))

# Task.objects.all().order_by('-id') # descending
# Task.objects.filter(title__icontains = "django").order_by('id') # ascending
# Task.objects.all().order_by('id', 'title')

# Task.objects.filter(title__icontains = "django").distinct()

# returns a list of dicts
# Task.objects.values()
# Task.objects.values('id', 'title')

# returns a list of tuples
# Task.objects.values_list()
# Task.objects.values_list('id', 'title')



# optimization purpose we use select_related and prefetch_related

# select_related()

# used as joins for foreign keys and one-to-one fields
# Review.objects.select_related('task').values_list('id', 'task__id', 'task__title')

# prefetch_related()

# used as joins for many-to-many or many-to-one (reverse foriegn key)
# Review.objects.prefetch_related('task').values_list('id', 'task__id')


# annotate()

# used for adding calculated field for every object in queryset.
# used for aggregations

# from django.db.models import Count, Avg, Max, Min, Sum, StdDev, Variance
# reviews = Review.objects.annotate(review_count = Count('task'))


# union(), intersection(), difference()

# qs1 = Author.objects.values_list('name')
# qs2 = Entry.objects.values_list('headline')

# qs1.union(qs2).order_by('name')

# qs1.union(qs2, qs3)

# qs1.intersection(qs2)

# qs1.difference(qs2)
