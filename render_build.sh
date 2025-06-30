#!/usr/bin/env bash
# Script para ejecutar migraciones automáticamente al desplegar en Render

python manage.py migrate --noinput
