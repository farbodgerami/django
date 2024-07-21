from django.core import paginator
from django.db.models import manager
from django.http import JsonResponse
from base.products import products
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.serializers import *
from base.models import *
from rest_framework import status

# vase pagination darim:
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getproducts(request):
    query = request.query_params.get("keyword")
    if query == None:
        query = ""
    products = Product.objects.filter(name__icontains=query)
    # tedadesafe=(len(products)/ )
    page = request.query_params.get("page")
    if page == None:
        page = 1
    page = int(page)
    # arge dovvom vase maximum product dar har safe hast
    paginator = Paginator(products,3)
   
    try:
        # page mige boro kodoom safe
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    serializer = Productserializer(products, many=True)
    # return Response({serializer.data})
    return Response(
        {"products": serializer.data, "page": page, "pages": paginator.num_pages}
    )

 
@api_view(["GET"])
 
def getproduct(request, pk):
    try:
        product = Product.objects.get(_id=pk)
        serializer = Productserializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response("product not found...")

@api_view(["POST"])
@permission_classes([IsAdminUser])
def createproduct(request):
    user = request.user

    product = Product.objects.create(
        # havaset bashe ke user relationship dare:
        user=user,
        name="sample name",
        price=0,
        brand="sample",
        countinstocks=0,
        category="cat",
        description="sydfsdaj",
    )
    serializer = Productserializer(product, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateproduct(request, pk):
    data = request.data
  
    product = Product.objects.get(_id=pk)
    product.name = data["name"]
    product.price = data["price"]
    product.brand = data["brand"]
    product.countinstocks = data["countinstocks"]
    product.category = data["category"]
    product.description = data["description"]
  
    product.save()
    serializer = Productserializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def uploadimage(request):
    data = request.data
 
    productid = data["productid"]
    product = Product.objects.get(_id=productid)
    if data["image"] != "undefined":
        product.image.delete()
        product.image = request.FILES.get("image")
        product.save()
    return Response("image was uploaded")


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteproduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response("product deleted")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createproductreview(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)

    reviewsfromuser=Review.objects.filter(user=user,product=product).exists()
    # javab=reviewsfromuser.filter(product=product)
    # print(reviewsfromuser)
    data = request.data
    # havest be in basheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
    # print(product.review_set.filter(user=user))
    # review already exists
    # alreadyexists = product.review_set.filter(user=user).exists()
    if reviewsfromuser:
        message = {"detail": "product already reviewed"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    elif data["rating"] == 0:
        message = {"detail": "please select a rating"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data["rating"],
            comment=data["comment"],
        )
    # agha pass bekhai tedade yecho az database darari ine:
    # reviews = product.review_set.all()
    reviews=Review.objects.filter(product=product)
    print(reviews)
    product.numreviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    product.rating = total / len(reviews)
    product.save()
    return Response({"detail": "review added"})

@api_view(["GET"])
def gettopproducts(request):
      products = Product.objects.filter(rating__gte=4).order_by('rating')[0:5]#vase reverse:-rating
      serializer=Productserializer(products,many=True)
      return Response(serializer.data)

