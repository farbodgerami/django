from ast import Pass

from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def findflights(request):
    flights = Flight.objects.filter(
        departurecity=request.data['departurecity'],
        arrivalcity=request.data['arrivalcity'],
        dateofdeparture=request.data['dateofdeparture'])
    serializer = Flightserializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def savereservation(request):
    flight = Flight.objects.get(id=request.data['flightid'])
    # agha dastan ine: shoma khodet sabtenam kardi too site vali oon chand nafare digei ke
    # mikhai vasashoon bilit begiri ke nakardan pass darim:
    passengar = Passengar()
    passengar.firstname = request.data['firstname']
    passengar.lastname = request.data['lastname']
    passengar.middlename = request.data['middlename']
    passengar.email = request.data['email']
    passengar.phone = request.data['phone']
    # avvalesh fekr kardam ke passengar save nemishe vali django mige ke ta savesh nakoni jelotar nemiram pass:
    passengar.save()
    reservation = Reservation()
    reservation.flight = flight
    reservation.passengar = passengar
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class Flightviewset(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = Flightserializer
    permission_classes = (IsAuthenticated, )


class Passengarviewset(viewsets.ModelViewSet):
    queryset = Passengar.objects.all()
    serializer_class = Passengarserializer


# class Reservationviewset(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = Reservationserializer

from rest_framework.views import APIView
from django.http import Http404


class Reservationlist(APIView):

    def get(self, request):
        students = Reservation.objects.all()
        serializer = Reservationserializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            print(data)
            flight = Flight.objects.get(id=data['flight'])
            passengar = Passengar.objects.get(id=data['passengar'])
            user = Reservation.objects.create(flight=flight,
                                              passengar=passengar)
            serializer = Reservationserializer(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'reservation with this detail already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class Reservationdetail(APIView):

    def get(self, request, pk):
        try:
            serializer = Reservationserializer(Reservation.objects.get(pk=pk))
            return Response(serializer.data)
        except:
            message = {'detail': 'matching query does not exist'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            data = request.data
            reservation = Reservation.objects.get(pk=pk)
            serializer = Reservationserializer(reservation, data=request.data)
            if data['flight'] != '':
                flight = Flight.objects.get(id=data['flight'])
                reservation.flight = flight
            if data['passengar'] != '':
                passengar = Passengar.objects.get(id=data['passengar'])
                reservation.passengar = passengar
            reservation.save()
            serializer = Reservationserializer(reservation, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'bad data'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('deleted')
