from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos simulados de productos para el MVP
PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Tarta de Fresas Frescas",
        "descripcion": "Deliciosa tarta artesanal con fresas orgánicas y crema pastelera de vainilla.",
        "precio": 15.00,
        "stock": 10,
        "imagen": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "nombre": "Macarons Surtidos (Caja 6)",
        "descripcion": "Auténticos macarons franceses con sabores a vainilla, pistacho y frambuesa.",
        "precio": 12.50,
        "stock": 25,
        "imagen": "https://images.unsplash.com/photo-1569864358642-9d1684040f43?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "nombre": "Pastel de Chocolate Intenso",
        "descripcion": "Bizcocho húmedo de cacao al 70% con cobertura de ganache y trozos de avellana.",
        "precio": 20.00,
        "stock": 2,
        "imagen": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "nombre": "Cheesecake de Arándanos",
        "descripcion": "Clásico postre neoyorquino horneado con mermelada rústica de arándanos silvestres.",
        "precio": 18.00,
        "stock": 0,
        "imagen": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    }
]

# Ruta principal (Home) - Catálogo Público
@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS)

# Ruta del Panel de Administración (GET para ver, POST para agregar)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Generar un ID auto-incremental simple
        nuevo_id = max(p['id'] for p in PRODUCTOS) + 1 if PRODUCTOS else 1
        
        # Recibir datos del formulario
        nuevo_producto = {
            "id": nuevo_id,
            "nombre": request.form.get('nombre'),
            "descripcion": request.form.get('descripcion', 'Sin descripción'),
            "precio": float(request.form.get('precio')),
            "stock": int(request.form.get('stock')),
            "imagen": request.form.get('imagen') or 'https://images.unsplash.com/photo-1551024601-bec78aea704b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80' # Imagen por defecto si está vacío
        }
        
        # Añadir al catálogo simulado
        PRODUCTOS.append(nuevo_producto)
        
        # Redirigir para evitar re-envío de formulario
        return redirect(url_for('admin'))
        
    return render_template('admin.html', productos=PRODUCTOS)

if __name__ == '__main__':
    # debug=True permite recargar el servidor automáticamente al guardar cambios
    app.run(debug=True, host='0.0.0.0', port=5000)
