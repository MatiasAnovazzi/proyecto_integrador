#!/bin/bash
echo "Esperando a que MySQL esté listo..."

until mysqladmin ping -h db -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
  >&2 echo "MySQL no está listo aún - esperando..."
  sleep 2
done

echo "MySQL está listo - lanzando la aplicación"
exec "$@"
