##Arbol DOM de HTML

#index.html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
    <header>
        <div class="contenedor">
            <img src="../assets/img/logo.png" alt="Logo" class="logo" aria-label="Logo">
            <nav aria-label="Menú principal">
                <ul>
                    <li><a href="index.html" aria-current="page">Inicio</a></li>
                    <li><a href="about.html">Sobre Nosotros</a></li>
                    <li><a href="services.html">Servicios</a></li>
                    <li><a href="contact.html">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section class="intro">
            <h1>Bienvenido a nuestra empresa de ciberseguridad</h1>
            <p>Protegemos tus datos y sistemas con soluciones de seguridad avanzadas.</p>
        </section>
        <section class="ciberseguridad">
            <h2>Importancia de la Ciberseguridad</h2>
            <p>En el mundo digital actual, la ciberseguridad es crucial para proteger la información confidencial y evitar ataques maliciosos. Nuestra empresa se dedica a proporcionar soluciones de seguridad que salvaguardan tus activos digitales.</p>
        </section>
    </main>
</body>
</html>


- Representación: 

```html
├── head
│   ├── meta (charset="UTF-8")
│   ├── meta (name="viewport", content="width=device-width, initial-scale=1.0")
│   ├── title (Inicio)
│   └── link (rel="stylesheet", href="../assets/css/styles.css")
└── body
    ├── header
    │   └── div (class="contenedor")
    │       ├── img (src="../assets/img/logo.png", alt="Logo", class="logo", aria-label="Logo")
    │       └── nav (aria-label="Menú principal")
    │           └── ul
    │               ├── li
    │               │   └── a (href="index.html", aria-current="page") (Inicio)
    │               ├── li
    │               │   └── a (href="about.html") (Sobre Nosotros)
    │               ├── li
    │               │   └── a (href="services.html") (Servicios)
    │               └── li
    │                   └── a (href="contact.html") (Contacto)
    └── main
        ├── section (class="intro")
        │   ├── h1 (Bienvenido a nuestra empresa de ciberseguridad)
        │   └── p (Protegemos tus datos y sistemas con soluciones de seguridad avanzadas.)
        └── section (class="ciberseguridad")
            ├── h2 (Importancia de la Ciberseguridad)
            └── p (En el mundo digital actual, la ciberseguridad es crucial para proteger la información confidencial y evitar ataques maliciosos. Nuestra empresa se dedica a proporcionar soluciones de seguridad que salvaguardan tus activos digitales.)
```

#about.html

```<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre Nosotros</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
    <header>
        <div class="contenedor">
            <img src="../assets/img/logo.png" alt="Logo" class="logo" aria-label="Logo">
            <nav aria-label="Menú principal">
                <ul>
                    <li><a href="index.html">Inicio</a></li>
                    <li><a href="about.html" aria-current="page">Sobre Nosotros</a></li>
                    <li><a href="services.html">Servicios</a></li>
                    <li><a href="contact.html">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section class="about">
            <h1>Sobre Nosotros</h1>
            <p>Somos una empresa líder en soluciones de ciberseguridad, dedicados a proteger la información de nuestros clientes con las mejores prácticas y tecnologías de vanguardia.</p>
        </section>
        <section class="ciberseguridad">
            <h2>Nuestro Enfoque en Ciberseguridad</h2>
            <p>La ciberseguridad es el núcleo de nuestra empresa. Trabajamos continuamente para innovar y mejorar nuestras soluciones, asegurándonos de que nuestros clientes estén siempre protegidos contra las amenazas emergentes.</p>
        </section>
    </main>
</body>
</html>
```
- Representación
```
html
├── head
│   ├── meta (charset="UTF-8")
│   ├── meta (name="viewport", content="width=device-width, initial-scale=1.0")
│   ├── title (Sobre Nosotros)
│   └── link (rel="stylesheet", href="../assets/css/styles.css")
└── body
    ├── header
    │   └── div (class="contenedor")
    │       ├── img (src="../assets/img/logo.png", alt="Logo", class="logo", aria-label="Logo")
    │       └── nav (aria-label="Menú principal")
    │           └── ul
    │               ├── li
    │               │   └── a (href="index.html") (Inicio)
    │               ├── li
    │               │   └── a (href="about.html", aria-current="page") (Sobre Nosotros)
    │               ├── li
    │               │   └── a (href="services.html") (Servicios)
    │               └── li
    │                   └── a (href="contact.html") (Contacto)
    └── main
        ├── section (class="about")
        │   ├── h1 (Sobre Nosotros)
        │   └── p (Somos una empresa líder en soluciones de ciberseguridad, dedicados a proteger la información de nuestros clientes con las mejores prácticas y tecnologías de vanguardia.)
        └── section (class="ciberseguridad")
            ├── h2 (Nuestro Enfoque en Ciberseguridad)
            └── p (La ciberseguridad es el núcleo de nuestra empresa. Trabajamos continuamente para innovar y mejorar nuestras soluciones, asegurándonos de que nuestros clientes estén siempre protegidos contra las amenazas emergentes.)
```

#services.html

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servicios</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
    <header>
        <div class="contenedor">
            <img src="../assets/img/logo.png" alt="Logo" class="logo" aria-label="Logo">
            <nav aria-label="Menú principal">
                <ul>
                    <li><a href="index.html">Inicio</a></li>
                    <li><a href="about.html">Sobre Nosotros</a></li>
                    <li><a href="services.html" aria-current="page">Servicios</a></li>
                    <li><a href="contact.html">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section class="services">
            <h1>Nuestros Servicios</h1>
            <p>Ofrecemos una amplia gama de servicios de ciberseguridad, desde evaluaciones de seguridad hasta implementaciones de soluciones de protección avanzadas.</p>
        </section>
        <section class="ciberseguridad">
            <h2>Servicios de Ciberseguridad</h2>
            <p>Nuestros servicios están diseñados para abordar todos los aspectos de la ciberseguridad, garantizando que tu organización esté protegida contra todas las formas de amenazas cibernéticas.</p>
        </section>
    </main>
</body>
</html>
```

- Representación

```
html
├── head
│   ├── meta (charset="UTF-8")
│   ├── meta (name="viewport", content="width=device-width, initial-scale=1.0")
│   ├── title (Servicios)
│   └── link (rel="stylesheet", href="../assets/css/styles.css")
└── body
    ├── header
    │   └── div (class="contenedor")
    │       ├── img (src="../assets/img/logo.png", alt="Logo", class="logo", aria-label="Logo")
    │       └── nav (aria-label="Menú principal")
    │           └── ul
    │               ├── li
    │               │   └── a (href="index.html") (Inicio)
    │               ├── li
    │               │   └── a (href="about.html") (Sobre Nosotros)
    │               ├── li
    │               │   └── a (href="services.html", aria-current="page") (Servicios)
    │               └── li
    │                   └── a (href="contact.html") (Contacto)
    └── main
        ├── section (class="services")
        │   ├── h1 (Nuestros Servicios)
        │   └── p (Ofrecemos una amplia gama de servicios de ciberseguridad, desde evaluaciones de seguridad hasta implementaciones de soluciones de protección avanzadas.)
        └── section (class="ciberseguridad")
            ├── h2 (Servicios de Ciberseguridad)
            └── p (Nuestros servicios están diseñados para abordar todos los aspectos de la ciberseguridad, garantizando que tu organización esté protegida contra todas las formas de amenazas cibernéticas.)
```

#contact.html

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
    <header>
        <div class="contenedor">
            <img src="../assets/img/logo.png" alt="Logo" class="logo" aria-label="Logo">
            <nav aria-label="Menú principal">
                <ul>
                    <li><a href="index.html">Inicio</a></li>
                    <li><a href="about.html">Sobre Nosotros</a></li>
                    <li><a href="services.html">Servicios</a></li>
                    <li><a href="contact.html" aria-current="page">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <section class="contact">
            <div class="contenedor">
                <h1>Contacto</h1>
                <form id="contact-form">
                    <label for="name">Nombre</label>
                    <input type="text" id="name" name="name" required>
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                    <label for="message">Mensaje</label>
                    <textarea id="message" name="message" required></textarea>
                    <button type="submit">Enviar</button>
                </form>
                <div id="response-message" style="display: none;"></div>
            </div>
        </section>
        <section class="ciberseguridad">
            <h2>Importancia de la Ciberseguridad</h2>
            <p>La ciberseguridad es fundamental para proteger la información confidencial y evitar ataques maliciosos. Nuestra empresa se dedica a proporcionar soluciones de seguridad que salvaguardan tus activos digitales, asegurando la integridad y la confidencialidad de tus datos.</p>
        </section>
    </main>
    <script>
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault();
            
            let formData = new FormData(this);
            fetch('http://127.0.0.1:5000/submit', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                let responseMessage = document.getElementById('response-message');
                if (data.status === 'success') {
                    responseMessage.innerHTML = '<p style="color: green;">' + data.message + '</p>';
                } else {
                    responseMessage.innerHTML = '<p style="color: red;">' + data.message + '</p>';
                }
                responseMessage.style.display = 'block';
            })
            .catch(error => {
                let responseMessage = document.getElementById('response-message');
                responseMessage.innerHTML = '<p style="color: red;">Error al enviar el formulario. Por favor, inténtelo de nuevo.</p>';
                responseMessage.style.display = 'block';
            });
        });
    </script>
</body>
</html>
```

- Representación

```
html
├── head
│   ├── meta (charset="UTF-8")
│   ├── meta (name="viewport", content="width=device-width, initial-scale=1.0")
│   ├── title (Contacto)
│   └── link (rel="stylesheet", href="../assets/css/styles.css")
└── body
    ├── header
    │   └── div (class="contenedor")
    │       ├── img (src="../assets/img/logo.png", alt="Logo", class="logo", aria-label="Logo")
    │       └── nav (aria-label="Menú principal")
    │           └── ul
    │               ├── li
    │               │   └── a (href="index.html") (Inicio)
    │               ├── li
    │               │   └── a (href="about.html") (Sobre Nosotros)
    │               ├── li
    │               │   └── a (href="services.html") (Servicios)
    │               └── li
    │                   └── a (href="contact.html", aria-current="page") (Contacto)
    └── main
        ├── section (class="contact")
        │   └── div (class="contenedor")
        │       ├── h1 (Contacto)
        │       └── form (id="contact-form")
        │           ├── label (for="name") (Nombre)
        │           ├── input (type="text", id="name", name="name", required)
        │           ├── label (for="email") (Email)
        │           ├── input (type="email", id="email", name="email", required)
        │           ├── label (for="message") (Mensaje)
        │           └── textarea (id="message", name="message", required)
        │           └── button (type="submit") (Enviar)
        │       └── div (id="response-message", style="display: none;")
        └── section (class="ciberseguridad")
            ├── h2 (Importancia de la Ciberseguridad)
            └── p (La ciberseguridad es fundamental para proteger la información confidencial y evitar ataques maliciosos. Nuestra empresa se dedica a proporcionar soluciones de seguridad que salvaguardan tus activos digitales, asegurando la integridad y la confidencialidad de tus datos.)
```

Estos árboles DOM proporcionan una visión estructurada de cómo están organizados y anidados los elementos en cada página HTML.
