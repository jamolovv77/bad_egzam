from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Books, Orders


def add_autor(request):
    if request.method == "POST":
        Autor.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            email=request.POST["email"]
        )
        return redirect("add_books")

    return render(request, 'add_autor.html')


def add_books(request):
    if request.method == "POST":
        data = request.POST

        Books.objects.create(
            name=data["name"],
            author=get_object_or_404(Autor, pk=data["autor_id"]),
            category=data["category"],
            image=request.FILES.get("image")
        )

        return redirect("get_books")

    autor = Autor.objects.all()
    return render(request, 'add_book.html', {"autor": autor})


def get_books(request):
    books = Books.objects.all()
    return render(request, 'show_books.html', {"books": books})


def add_orders(request):
    if request.method == "POST":
        data = request.POST

        Orders.objects.create(
            book=get_object_or_404(Books, pk=data["book_id"]),
            customer_name=data["customer_name"],
            order_date=data["order_date"]
        )

        return redirect("get_orders")

    books = Books.objects.all()
    return render(request,'add_orders.html', {"books": books})


def get_orders(request):
    orders = Orders.objects.all()
    return render(request,'show_orders.html', {"orders": orders})


def home(request):
    return render(request,'home.html')