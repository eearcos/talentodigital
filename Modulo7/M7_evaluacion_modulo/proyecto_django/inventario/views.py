from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm, DetalleProductoForm, CategoriaForm, EtiquetaForm

# --- HOME ---
def index(request):
    # Requisito SQL PERSONALIZADO (Raw SQL)
    # Obtenemos el conteo total de productos usando SQL directo
    conteo_raw = 0
    try:
        for p in Producto.objects.raw('SELECT id, nombre FROM inventario_producto'):
            conteo_raw += 1
    except:
        conteo_raw = 0
        
    context = {
        'total_productos': Producto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_etiquetas': Etiqueta.objects.count(),
        'mensaje_sql': f"Conteo vía SQL Raw: {conteo_raw}"
    }
    return render(request, 'index.html', context)

# --- PRODUCTOS ---

@login_required # Seguridad
def lista_productos(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    
    # ORM Básico
    productos = Producto.objects.all().select_related('categoria')

    # ORM: Consultas con Filtros (filter, Q)
    if query:
        # Busca por nombre O descripción
        productos = productos.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # ORM: Anotaciones y Exclude (Ejemplo: Excluir productos con precio 0)
    productos = productos.exclude(precio=0)

    categorias = Categoria.objects.all()
    return render(request, 'productos/lista.html', {
        'productos': productos, 
        'categorias': categorias
    })

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form_producto = ProductoForm(request.POST)
        form_detalle = DetalleProductoForm(request.POST)
        
        if form_producto.is_valid() and form_detalle.is_valid():
            producto = form_producto.save()
            detalle = form_detalle.save(commit=False)
            detalle.producto = producto # Relación 1 a 1 manual
            detalle.save()
            return redirect('lista_productos')
    else:
        form_producto = ProductoForm()
        form_detalle = DetalleProductoForm()
    
    return render(request, 'productos/crear.html', {
        'form_producto': form_producto, 
        'form_detalle': form_detalle
    })

@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # Intentamos obtener el detalle si existe
    detalle = getattr(producto, 'detalleproducto', None)
    return render(request, 'productos/detalle.html', {'producto': producto, 'detalle': detalle})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # Obtener o crear detalle si no existe para evitar errores
    detalle, created = DetalleProducto.objects.get_or_create(producto=producto)

    if request.method == 'POST':
        form_producto = ProductoForm(request.POST, instance=producto)
        form_detalle = DetalleProductoForm(request.POST, instance=detalle)
        if form_producto.is_valid() and form_detalle.is_valid():
            form_producto.save()
            form_detalle.save()
            return redirect('lista_productos')
    else:
        form_producto = ProductoForm(instance=producto)
        form_detalle = DetalleProductoForm(instance=detalle)

    return render(request, 'productos/editar.html', {
        'form_producto': form_producto, 
        'form_detalle': form_detalle, 
        'producto': producto
    })

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})

# --- CATEGORÍAS (Lógica similar simplificada) ---

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.annotate(num_productos=Count('productos'))
    return render(request, 'categorias/lista.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/formulario.html', {'form': form, 'titulo': 'Editar Categoría'})

@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/eliminar.html', {'categoria': categoria})

# --- ETIQUETAS (CRUD simplificado) ---

@login_required
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})

@login_required
def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas/formulario.html', {'form': form, 'titulo': 'Crear Etiqueta'})

@login_required
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas/formulario.html', {'form': form, 'titulo': 'Editar Etiqueta'})

@login_required
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'etiquetas/eliminar.html', {'objeto': etiqueta})