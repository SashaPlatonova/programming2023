from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialazer import *
import datetime as DT
from django.db.models import Q


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ResidentList(generics.ListAPIView):
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Resident.objects.all()
        params = self.request.query_params
        return queryset


class ResidentCreateView(generics.CreateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        instance.set_password(instance.password)
        instance.save()


class ResidentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResidentRetrive(generics.RetrieveAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransportTypeListView(generics.ListAPIView):
    serializer_class = TransportTypeSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = TransportType.objects.all()
        params = self.request.query_params
        id = params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        return queryset


class TypeRetrive(generics.RetrieveAPIView):
    queryset = TransportType.objects.all()
    serializer_class = TransportTypeSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransportListView(generics.ListAPIView):
    serializer_class = TransportSer

    def get_queryset(self):
        queryset = Transport.objects.all()
        params = self.request.query_params
        id = params.get('id', None)
        type = params.get('type', None)

        if id:
            queryset = queryset.filter(id=id)

        if type:
            queryset = queryset.filter(type=type)

        return queryset


class TransportCreateView(generics.CreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransportDelete(generics.RetrieveDestroyAPIView):
    serializer_class = TransportCreateSerializer
    queryset = Transport.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params
        id = params.get('id', None)
        user = params.get('user', None)

        if id:
            queryset = queryset.filter(id=id)

        if user:
            queryset = queryset.filter(user_id=user)

        return queryset


class OrderSetFilteredByDateBusyView(generics.ListCreateAPIView):
    serializer_class = OrderSer

    def post(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        date_begin = request.data['date_begin']
        date_end = request.data['date_end']
        time_begin = request.data['time_begin']
        time_end = request.data['time_end']
        join_date = date_begin + ' ' + time_begin + ':00'
        begin_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        join_date = date_end + ' ' + time_end + ':00'
        end_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        queryset = queryset.filter(time_start__gte=begin_number)
        queryset = queryset.filter(time_end__lte=end_number)
        serializer = OrderSer(queryset, many=True)

        return Response(serializer.data)


class TransportSetFilteredByDateFreeView(generics.ListCreateAPIView):
    serializer_class = TransportSer

    def post(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        date_begin = request.data['date_begin']
        date_end = request.data['date_end']
        time_begin = request.data['time_begin']
        time_end = request.data['time_end']
        type = request.data['type']
        join_date = date_begin + ' ' + time_begin + ':00'
        begin_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        join_date = date_end + ' ' + time_end + ':00'
        end_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        queryset = queryset.filter(time_start__gte=begin_number)
        queryset = queryset.filter(time_end__lte=end_number)
        orders_id = queryset.values_list('transport_id_id', flat=True)
        queryset = Transport.objects.filter(~Q(id__in=orders_id))
        queryset = queryset.filter(type_id=type)
        serializer = TransportSer(queryset, many=True)

        return Response(serializer.data)


class TransportSetFilteredByDateBusyView(generics.ListCreateAPIView):
    serializer_class = TransportSer

    def post(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        date_begin = request.data['date_begin']
        date_end = request.data['date_end']
        time_begin = request.data['time_begin']
        time_end = request.data['time_end']
        type = request.data['type']
        join_date = date_begin + ' ' + time_begin + ':00'
        begin_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        join_date = date_end + ' ' + time_end + ':00'
        end_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        queryset = queryset.filter(time_start__gte=begin_number)
        queryset = queryset.filter(time_end__lte=end_number)
        orders_id = queryset.values_list('transport_id_id', flat=True)
        queryset = Transport.objects.filter(id__in=orders_id)
        queryset = queryset.filter(type_id=type)
        serializer = TransportSer(queryset, many=True)

        return Response(serializer.data)


class TransportFindByParamsView(generics.ListCreateAPIView):
    serializer_class = TransportSer

    def post(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        date_begin = request.data['date_begin']
        time_begin = request.data['time_begin']
        height = request.data['height']
        length = request.data['length']
        weight = request.data['weight']
        width = request.data['width']
        join_date = date_begin + ' ' + time_begin + ':00'
        begin_number = int(DT.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S').timestamp())
        end_number = begin_number + 10800
        queryset = queryset.filter(time_start__gte=begin_number)
        queryset = queryset.filter(time_end__lte=end_number)
        orders_id = queryset.values_list('transport_id_id', flat=True)
        queryset = Transport.objects.filter(~Q(id__in=orders_id))
        # todo: method calculation size + capacity from type
        queryset = queryset.filter(high__gte=height, width__gte=width, length__gte=length)
        serializer = TransportSer(queryset, many=True)

        return Response(serializer.data)
