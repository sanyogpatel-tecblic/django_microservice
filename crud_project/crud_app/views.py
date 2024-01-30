from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
import json

from crud_app.models import Book
from crud_app.serializers import BookSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BookCrudView(View):
    model = Book
    serializer = BookSerializer

    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(self.model, pk=pk)
            serializer = self.serializer(book)
            return JsonResponse(serializer.data)
        else:
            books = self.model.objects.all()
            serializer = self.serializer(books, many=True)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = self.serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    def put(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        data = json.loads(request.body)
        serializer = self.serializer(instance=book, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        book.delete()
        return JsonResponse({"message": "Book deleted successfully."})
