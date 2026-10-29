from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import JsonResponse
from .models import Proyecto

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
    
class ProyectoView(View):
    def get(self, request, pk=None):
        if pk is not None:
            # Buscar un solo registro
            try:
                proyecto = Proyecto.objects.get(pk=pk)
                data = {"id": proyecto.id, "nombre": proyecto.nombre, "descripcion": proyecto.descripcion}
                return JsonResponse(data, status=200)
            except Proyecto.DoesNotExist:
                return JsonResponse({"error": "No encontrado"}, status=404)
        else:
            # Listar todos los registros
            proyectos = list(Proyecto.objects.values("id", "nombre", "descripcion"))
            return JsonResponse(proyectos, safe=False, status=200)
        
    def post(self, request):
        try:
            # Convertir el cuerpo de la petición (bytes) a un diccionario de Python
            body = json.loads(request.body)
            nombre = body.get("nombre")
            descripcion = body.get("descripcion")

            # Crear el registro en la base de datos
            proyecto = Proyecto.objects.create(nombre=nombre, descripcion=descripcion)

            return JsonResponse({
                "mensaje": "Creado exitosamente",
                "id": proyecto.id,
                "nombre": proyecto.nombre
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    def put(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
            body = json.loads(request.body)
            
            # Actualizar campos
            proyecto.nombre = body.get("nombre", proyecto.nombre)
            proyecto.descripcion = body.get("descripcion", proyecto.descripcion)
            proyecto.save()

            return JsonResponse({"mensaje": "Actualizado exitosamente"}, status=200)
        except Proyecto.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    def delete(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
            proyecto.delete()
            return JsonResponse({"mensaje": "Eliminado exitosamente"}, status=200)
        except Proyecto.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)
        
        