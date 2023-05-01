'''Django  Rest Framwork'''
a = 'hello'

# API ---> stands for Application programming interface 
# mesto soprikosnovenia klienta i servera , prednaznachena dlya vzaimodesitvia mejdu programmammi  

'''REST (representational state transfer ) --> style API, standart, kotoromu sleduet API'''

# PRINCIPLES 

# 1. razgranichevat klient i servera 
# 2. otsutsvie sostoianie ( net Sohronenie sostoiania) - server ne doljen hranit kakuiu-libo informatsiu o kliente 
# 3. Keshirovanie --
# 4. Mnogourovnevaia systema 
# 5. Ediniy interface 
# 6. Kod predostavlyaetsya po zaprosu 

# RESTfull API - API kotoroe sootvetsvuet principles rest


# Poryadok sozdania django applications 

# 1. Creating virtual envirenment 
# python3 -m venv vevn 

# 2. Activating venv 
# . venv/bin/activate

# 3. creating file req.txt 
# writing there: Django, djangorestframework, psycopg2-binary 

# 4. Downloading: pip3 install -r req.txt 

# 5. django-admin startproject <project_name> .  --> creating project, if no dot at the end budet vlojennost 

# 6. python3 manage.py startapp <app_name> -- creating application 

# 7. Registration of the new application: 
# open settings.py --> INSTALLED_APPS -> registration : rest_framework, <app_name>, 

# 8. in file settings setting database exaple below: 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'Name': 'test',
#         'USER': 'bektur',
#         'PASSWORD': 1,
#         'HOST': 'localhost',
#         'PORT': 5432
        
#     }
# }


# python3 manage.py makemigrations -> sozdaet file migratsii 

# python3 manage.py migrate ->


# python3 manage.py createsuperuser -- creating superuser / admin 

# python3 manage.py runserver   

# if the sever in use write down this code instead 

# lsof -t -i tcp:8000 | xargs kill -9
# lsof -t -i tcp:8000 | xargs kill -9

'''Models'''

# Kak prohodit zapros

# 1.  asgi/wsgi -> (te kto prinimaiut zapros i vozvrashaet otvet)
# 2. settings -> middlewares
# 3. urls -> marshrutizatory
# 4. views -> predstavlenie ( function, kotorye vozvrashaiut dannye v nujnom formate)
# 5.  serializers ( classes, kotorye perevodyat dannye is json v python i naoborot)
# 6. models ( classes, kotorye oboznachaet kak budet vygledet nasha tablitsa b DB)
# 7. managers ( objects) -> classes, katorye rabotaiut s ORM.
# 8. DB -> database ( baza dannyh )


# ==========================Polya=========================

# 1. 'CharField' -> dlya strokovogo znachenia ( obezyatelno nujno ukazyvat max_length)
# 2. 'SlugField' -> dlya hranenia slug ( obychno ispolzuetsya v url) soderjit tolko bykvy, chisla,-, _
# 3. 'TextField' -> dlya hranienia text
# 4. 'DecimalField' -> dlya drobnyh chisel ( max_digit: kol-vo sifr seloi chasti
# decimal_places ( kol-vo sifr posle zapyatoi) )
# 5. 'IntegerField' -> dlya chisel
# 6. BooleanField' -> dlya daty ( datetime.date ) --> mojno peredat argumenty: auto_now ->
# obnovlyaetsya pri izminenii zapisi auto_now_add -> zadaetsya tolko odin raz pri sozdanii
# 7. 'TimeField' -> dlya vremeni (auto_now, auto_now_add)
# 8. 'DateTimeField' -> dlya daty i vremeni
# 9. 'EmailField' -> dlya email
# 10. 'FileField' -> dlya files ( upload_to -> ukazanie derectory, gde budet file)
# 11. 'ImageField' -> dlya kartinok ( image)
# 12. 'JSONField' -> dlya strok v formate json


'''Klychevye parametry dlya poley ( optional) '''
# null -> esli True , budet v DB zapisyvat null, esli dannye ne peredany
# blank -> esli True, budet stavit pustuiy stroku ( ne obezyatelno dlya zapolnenia)
# default -> znachenie po umolchaniu
# unique -> esli True, to v etoi kalonke mogut hranitsya tolko unicalnye znachenia
# primary_key -> esli True? pervichniy key - identificator
# choices -> spisok s tuple ogranichevaem vozmojnye varianty dlya zapolneia


'''========================Svyazi======================'''


# ForeignKey -> svyaz odin k mnogim ( obezyatelno ukazat model kotoruiu my budem ssylatsya, on_delete, related_name - dlya obratnoi sviazi )

# ManyToManyField -> mnogii ko mnogim ( vse to je samoe , chto i ForeignKey)

'''=======================on_delete===================='''

# models.CASCADE -> kaskadnoe udalenie ( esli udalyaetsya glavniy obect, to udalyaetsya i zoviseshie ot ego )

# models.PROTECT -> vyzyvaet oshibku pri popytki udalenie glavniy object 
# models.SET_NULL -> ne udalyaet zavisyashee objecta, a esli null ( null= True)
# models.SET_DEFAULT - > esli opredilen default, to stavit ego
# models.DO_NOTHING - > nochego ne delaet, vyzyvaet oshibku 




# Product.objects.all()
# # SELECT * FROM products;
#
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие AND условие2;

# Product.objects.filter(Q(условие)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000) #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000) #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000) #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# SELECT * FROM products WHERE price <= 50000;

# Product.objects.filter(category_id__in=['phones', 'notebooks'])
# SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# Product.objects.filter(price__range=[20000, 50000])
# SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startswith='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartswith='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# SELECT name FROM products;

# Product.objects.only('name', 'price') #запрашивает указанные поля
# SELECT name, price FROM products;

# Product.objects.defer('name', 'price') #исключает указанные поля
# SELECT id, description, category_id FROM products;

# Product.objects.count()
# SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone 12',
#                        description='awddwdawd',
#                        price=78000,
#                        category_id='phones')
# INSERT INTO products (name, description, price, category_id) VALUES \
    # ('Apple Iphone 12', 'dwadaafafaw', 78000, 'phones');

# Product.objects.bulk_create([
#     Product(...),
#     Product(...)
# ]) #множественное создание

# Product.objects.update(price=50000)
# UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
#UPDATE products SET price=50000 WHERE ...;

# Product.objects.filter(id=1).update(price=50000)
#UPDATE products SET price=50000 WHERE id=1;

# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()



'''=========related_name========'''

# pozvolyaet obrashatsya iz svyazannyh object k tem , ot kotoryh eta svyaz sozdana (dlya obratnogo poiska)
# related_name -> sozdaet sviaz s obratnoi storony 

# cat = Category.objects.get(id=1)
# cat.posts.all() -> poluchenie vseh postov, otnosyashiesya k dannoi kategorii.

'''=========related_query_name========'''

# sozdaet imennoovanniy atribut , kotoriy  pozvolyaet delat zaprosy s ispolzovaniem methoda perfetfh_related - > zagruzhaet svyazannye objects ( optimiziruet zaprosy v bd )

# cat.post.all()

# QuerySet -> object poluchennye iz bazy dannyh , blogodoya manager'u ( objects)

# Manager - class, predostavlyet methody dlya dostupa k orm Django ( otpravlyet zapros v DB)
# default = objects 
# (obnovlyem, poluchaem, udalyem , filtruem dannye iz tablits)



