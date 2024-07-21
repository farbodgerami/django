from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializer import *
from .models import *
server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[

        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            description='Category of servers to retrieve',
            location=OpenApiParameter.QUERY
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            description='number of servers to retrieve',
            location=OpenApiParameter.QUERY
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            description='filter servers by the current authenticated user(True/False)',
            location=OpenApiParameter.QUERY
        ),
                OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            description='includ the number of members for each erver in the response',
            location=OpenApiParameter.QUERY
        ),
                OpenApiParameter(
            name="by_serverid",
            type=OpenApiTypes.INT,
            description='include server by id',
            location=OpenApiParameter.QUERY
        ),
    ]

)
