from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Ticket
from .serializers import TicketSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@api_view(['GET', 'POST'])
@cache_page(60)
@permission_classes([IsAuthenticated])
def ticket_list(request):

    if request.method == 'GET':

        tickets = Ticket.objects.all()

        # -------- Filtering --------
        category = request.query_params.get('category')
        status_param = request.query_params.get('status')

        if category:
            tickets = tickets.filter(category=category)

        if status_param:
            tickets = tickets.filter(status=status_param)

        # -------- Search --------
        search = request.query_params.get('search')
        if search:
            tickets = tickets.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        # -------- Ordering --------
        ordering = request.query_params.get('ordering')
        if ordering:
            tickets = tickets.order_by(ordering)

        # -------- Pagination --------
        paginator = PageNumberPagination()
        paginator.page_size = 2

        paginated_tickets = paginator.paginate_queryset(tickets, request)
        serializer = TicketSerializer(paginated_tickets, many=True)

        return paginator.get_paginated_response(serializer.data)


    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET', 'PATCH', 'DELETE'])
@cache_page(60)
@permission_classes([IsAuthenticated])
def ticket_detail(request, id):

    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket Not Found'}, status=404)

    # -------- GET --------
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    # -------- PATCH (Update status or any field) --------
    if request.method == 'PATCH':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # -------- DELETE --------
    if request.method == 'DELETE':
        ticket.delete()
        clear_cache()
        return Response(
            {'message': 'Ticket deleted successfully'},
            status=204
        )
# Create your views here.




