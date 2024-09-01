#!/bin/bash

# Saia do script se qualquer comando falhar
set -e

# Coletando arquivos estáticos
python manage.py collectstatic --noinput

echo "Build process completed successfully!"