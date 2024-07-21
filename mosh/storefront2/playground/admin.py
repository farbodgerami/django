from django.contrib import admin
from django.shortcuts import get_object_or_404

# Register your models here.
# try:
#     abcd
# except Product.DoesNotExist:
#     return Response(satus=404)
# jaigozin:
# product=get_object_or_404(Product,pk=id)
# serializer=Productserializer(product)
# return Response(serializer.data)
# vase filter:
# ino yeja test kon:
# /products?collectino_id=1 khodesh mishe:/products/?collectino_id=1
# dar yek kelas:
# def get_yechi(self):
# collectionid=self.request.query_params['collection_id']
# return Product.objects.filter(collection_id)
# agar collectionid bood: vagarna kollesh ro neshiin bede
# queryset=Product.objects.all()
# if collectionid id not None:collectionid)
#    quryset= quryset.filter(collection_id=