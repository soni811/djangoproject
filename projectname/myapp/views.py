from django.http import HttpResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Customer
from .serializers import ProductSerializer,CustomerSerializer,LoginSerializer
from .db import get_collection
from rest_framework import viewsets,status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

def home(request):
    return HttpResponse("Hello, Django!")

@api_view(['GET'])
def get_products(request):
    data = {"message": "Hello, this is the products API"}
    return Response(data)

@api_view(['POST'])
def save_product(request):
    name = request.data.get("name")
    price = request.data.get("price")

    if not name or not price:
        return Response({"error": "Name and Price are required"}, status=400)
    collection = get_collection() 
    product_data = {"name": name, "price": price}
    result = collection.insert_one(product_data)

    return Response({"message": "Product saved successfully", "id": str(result.inserted_id)}, status=201)

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


class CustomerListCreateView(APIView):
    """APIView is a class-based view (CBV) provided by Django REST Framework (DRF) for handling HTTP requests in an API. 
    It is a more advanced and flexible version of Django's standard View class, specifically designed for working with RESTful APIs.
    In Django, objects.all() is a query that retrieves all records from a database table (model).
    """
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
         How APIView Works : APIView: A class-based view in DRF to handle HTTP methods (GET, POST, PUT, DELETE).
        Inheritance: APIView is a subclass of Django's View,
        and it comes with added functionality tailored for REST API endpoints. By inheriting from APIView, 
        you can handle HTTP methods (like GET, POST, PUT, DELETE) in a structured way.
        Handles HTTP Methods: Instead of defining separate functions 
        for each HTTP method (like def get(), def post()), APIView provides a clean and organized way to define them as methods in a class.
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "You are authenticated!"})