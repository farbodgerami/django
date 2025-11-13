from rest_framework import serializers
from ...models import *
from accounts.models import Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

# class PostSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title=serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields='__all__'   
        # fields=[id,'title',...]
        # fields=['id','title']
    
# class PostSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         # user=User.objects.get(id=self.context.get('request').user)
#         # validated_data['author']=Profile.objects.get(user__id=self.context.get('request').user.id)
#         validated_data["author"] = self.context.get("request").user
#         return super().create(validated_data)

#     snippet = serializers.ReadOnlyField(source="get_snippet")
#     # relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
#     absolute_url = serializers.SerializerMethodField()

#     # category=serializers.SerializerMethodField()
#     # category=CategorySerializer()#in badish ine ke dar view ke neshoon mide ma dge liste category haro nadarim(be anam khob)
#     # category=serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all() )
#     class Meta:
#         model = Post
#         fields = [
#             "id",
#             "author",
#             "title",
#             "content",
#             "status",
#             "category",
#             #   'relative_url',
#             "absolute_url",
#             "image",
#             "created_date",
#             "updated_date",
#             "published_date",
#             "snippet",
#         ]
#         # in vase ine ke nevisande ba esme digei postesho sabt nakone:
#         read_only_fields = ["author"]

#     def get_absolute_url(self, obj):
#         request = self.context.get("request")
#         return request.build_absolute_uri(obj.pk)

#     #  irade kar ine ke vase post kardan category zaher nemishe ke behesh meghdar bedim:
#     def get_category(self, obj):
#         return {obj.category.id, obj.category.name}

#     # in alie vase vaghti ke masalan faghat ye list az nam va id ha vase namayesh fetch kone va ba zadane item bere dakhel va ettelaate kamel fetch beshan
#     def to_representation(self, instance):
#         request = self.context.get("request")
#         # in vase ine ke betoonim satre zir ro dorost benevisim:
#         # print(request.__dict__)
#         rep = super().to_representation(instance)
#         rep["state"] = "list"
#         if request.parser_context.get("kwargs").get("id"):
#             rep["state"] = "single"
#             rep.pop("snippet", None)
#             rep.pop("relative_url", None)
#             rep.pop("absolute_url", None)
#         else:
#             rep.pop("content", None)

#         rep["category"] = CategorySerializer(
#             instance.category, context={"request": request}
#         ).data
#         # dar in ja snippet ro hkhastim ke hazf konim
#         return rep
