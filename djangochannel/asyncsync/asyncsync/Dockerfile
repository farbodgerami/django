FROM python:3.9.7-slim 
RUN pip install pip --upgrade 
WORKDIR /app
COPY ./r.txt /app
 
 
 
RUN pip install -r r.txt 
# RUN pip install django==4.1.0
# RUN pip install -U channels["daphne"]
# RUN pip install channels_redis

COPY . /app
 
EXPOSE 8000
# CMD ["gunicorn","-w","1", "asyncsync.wsgi:application","--bind","0.0.0.0:8000"]
# CMD ["gunicorn","-w","1", "asyncsync.wsgi:application" ]
# CMD ["daphne", "asyncsync.asgi:application","-b","0.0.0.0","-p","8000"]
# CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
# CMD ["python", "manage.py","runserver","--nothreading","0.0.0.0:8000"]
# CMD ["python", "manage.py","runserver"]


#  gunicorn asyncsync.wsgi:application --bind 0.0.0.0:7000

# daphne asyncsync.asgi:application --bind 0.0.0.0:8000

 
# function sync va time.sleep(second)
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
# daphne: hame ba ham sare 1 sanie vaisadan
# runserver: hame ba ham sare 1 sanie vaisadan

# function async va time.sleep(second)
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
#XXX: daphne: in kheili ajib!!!!!!!!!! az tabe 1 ta 6 mashghool boodan va vaghti hame ba ham 6 sanie gozasht ba ham vaisadan
# runserver: hame ba ham sare 1 sanie vaisadan

# function async va asyncio.sleep()
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
# daphne: hame ba ham sare 1 sanie vaisadan
# runserver: hame ba ham sare 1 sanie vaisadan

# natige:dar function async bayad oon ghesmati ke khasiate async dare ro async entekhab konim. masalan
# vaghti  be ye url request mizanim va agar tabe async hast bayad
#  async with session.get(url) as response:
# result = response.text() 
# bashe na  
# result = requests.get('url')
    # result = result.json()
#  va ya  await asyncio.sleep(seconds) bashe na  time.sleep(second)
# kollan yeseri function ha hastand ke dar function haye async yejoor dge neveshte mishan vagar na morede XXX pish miad



# cpu intensive:

# function async  
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 

# tebghe moshahedat dar gunicorn va dar cup intensiv ha ba bala bordane w dar majmoo etefaghi nemiofte va
# agar masalan 10 ta tab dashte bashim 2 sanie tabe 1 va sepas 2 sanie tabe 2 ba ta akhar ke dar majmoo mishe
# hodoode 20 sanie
# yani ba bala raftane worker ha be hamoon meghdar ham az ghodrateshoon kaste shode. albate dar kare hamzaman intore.
# agar masalan 1 tab refresh beshe mesle w=1 hamoon ghodrate ghabl ro dare.
# hal agar w 2 bashe 2 ta tab ham zaman anjam mishe vale dar hodoode 4 sanie. va badesh 2 tabe badi va in bar ham dar 
# majmoo 20 sanie 

# dar daphne 
# mesle computere mamooli amal mikone, yani vaghti yekari mikone tabe badi ke faal mishe oon yeki 
# ro meghdari zaif mikone eine  ine ke w dar gunicorn ro ye 8 ya 10 va ya bishtar bezarim 
# masalan yek tab 2 sanie tool mikeshe vale agar dar sanie 1 be bad ye tabe dgie shoroo be kar kone, ghodrat nesf mishe
# va in tab 1 sanie baad ro 2 sanie tool mide va in kamelan tabiie.

# function sync 
# tebghe moshahedat hich farghi ba async nadasht daghighan hamoon bood

# PASS: 
# dar cpu intensive async va sync baham hich farghi nadaran.
# dar cpu intensive daphne va gunicorn faghat in fargh ro daran ke gunicorn avval ye task ro kamel va ba bishtarin
# ghodrat anjam mide va badesh mire soraghe taske dge va in vaghti ke chand user ye requeste sangin midan kheili khoobe.
# usere avvali kare anjam mishe va aalaaf nemishe va badesh usere dovvomi. ke albatte chenin karai ro celery bayad anjam bede.
