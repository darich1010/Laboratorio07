# 🌿 AgroRegistro - Laboratorio 07 (Programación Web con Django + Render)

Este repositorio corresponde al desarrollo del Laboratorio 07 de Programación Web. El objetivo fue **crear una API REST con Django, conectarla a una base de datos PostgreSQL en la nube y desplegarla en el servicio gratuito Render**.

---

## ✅ Estado del proyecto

- [x] API funcional en entorno local
- [x] Base de datos PostgreSQL remota (Render)
- [x] Despliegue exitoso en Render
- [ ] Pruebas completas de métodos en la nube

---

## 🌐 Proyecto desplegado

🔗 [https://laboratorio07-42ov.onrender.com/](https://laboratorio07-42ov.onrender.com/)  
🔒 Panel de administración: [https://laboratorio07-42ov.onrender.com/admin/](https://laboratorio07-42ov.onrender.com/admin/)

> ⚠️ *Render puede suspender momentáneamente el servicio por inactividad. Si aparece error o página caída, basta con abrir la URL y esperar unos segundos para que el servidor se reactive.*

---

## 📝 Explicación técnica

Se logró desplegar correctamente el proyecto Django usando:

- Django 5
- Django REST Framework
- PostgreSQL en Render
- Autenticación JWT (`simplejwt`)
- Archivos clave: `Procfile`, `requirements.txt`, configuración `DATABASES` y `ALLOWED_HOSTS`

Durante el despliegue se resolvieron múltiples errores relacionados con:

- Falta del módulo `psycopg2`
- Errores al resolver el host de PostgreSQL desde entorno local
- Migraciones bloqueadas por conectividad
- Dependencias faltantes en el entorno virtual

---

## 🧪 Pruebas REST (pendiente)

Aunque el despliegue fue exitoso, **no fue posible ejecutar las pruebas CRUD (GET, POST, PUT, DELETE) desde SoapUI o Postman hacia la nube**, debido a las siguientes razones:

- El servicio gratuito de Render entra en modo “sleep” tras un tiempo inactivo.
- El servidor tarda en despertar, causando errores de timeout o `404 Page not found` en pruebas externas.
- Durante los intentos, el sistema no procesaba correctamente los endpoints protegidos por JWT.

Estos errores fueron documentados y serán discutidos con el docente en busca de una solución viable para futuras implementaciones.

---

## 💬 Comentario final

Se logró el objetivo de **desplegar el backend de AgroRegistro en la nube con Django y PostgreSQL**, demostrando conocimientos sobre configuración y despliegue. Quedan pendientes las pruebas REST sobre el servidor en producción, que fueron imposibles de completar por las limitaciones mencionadas.

El funcionamiento completo del sistema fue validado previamente en entorno local con SoapUI durante el Laboratorio 6.

---

## 👨‍💻 Autor

**Dario Rafael Cornejo Hurtado**  
Estudiante de Ingeniería de Sistemas  
Curso: Programación Web - 2025-A  


