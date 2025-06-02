from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import *
from core.pos.models import Category, Product, Client


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    #def get_queryset(self):
        # return Category.objects.filter(name__icontains='an')  o
        # return self.queryset.filter(name__icontains='an') o
    ##    print('get_queryset')
    #    print(self.request.data)
    #    return self.queryset.filter()

    def get(self, request, *args, **kwargs):
       #print('get')
       #print(self.request.query_params['name'])
       #print(self.request.query_params.get('name', 'William Vargas'))
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # puedo obtener la info de esta forma:
        #categorias = Category.objects.all()
        #serializers = CategorySerializer(categorias, many=True)    o
        # o de esta otra:
        #categorias = Category.objects.first()
        #serializers = CategorySerializer(categorias, many=False)  o
        # o de esta otra:
        #serializers = CategorySerializer(self.get_queryset(), many=True)  o
        # o de esta otra:
        #serializers = self.serializer_class(self.get_queryset(), many=True)
        # return Response(serializers.data) #self.list(request, *args, **kwargs)
        # o de esta otra:
        #queryset = self.get_serializer().Meta.model.objects.all()
        serializers = self.serializer_class(self.queryset.all(), many=True)
        #return self.list(request,*args, **kwargs)
        #return Response(serializers.data) #self.list(request, *args, **kwargs)
        # o de esta otra:
        #items = [i.toJSON() for i in Category.objects.all()]
        return Response(serializers.data)

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer

    # puede sobrescribir este metodo si es necesario
    #def post(self, request, *args, **kwargs):
    #    print(self.request.data)
    #    return self.create(request, *args, **kwargs)

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # si quiero ver que info me llega sobreescribo el metodo solo para agregar el print
    #def delete(self, request, *args, **kwargs):
    #    print(self.kwargs)
    #    return self.destroy(request, *args, **kwargs)
    # si quiere que me devuelva un mensaje confirmando el delete sobreescribo
    # el metodo delete
    def delete(self, request, *args, **kwargs):

        try:
            instance = self.queryset.get(pk=kwargs['pk'])
            instance.delete()
            return Response({'msg': f"Se ha eliminado la categoria (pk = {self.kwargs['pk']} )"})
        except Exception as e:
            return Response({'msg': f"NO existe la categoria (pk = {self.kwargs['pk']} )"})


class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        #para ver la info que me llega
        print(self.request.query_params)
        return Response({'resp': 'GET'})

    def post(self, request, *args, **kwargs):
        #para ver la info que me llega
        #print(self.request.data)
        #return Response({'resp': 'POST'})
        # para enviar los mismo que el metodo list
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)