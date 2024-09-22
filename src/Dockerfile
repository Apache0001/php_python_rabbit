FROM php:8.2-apache

RUN apt-get update && \
apt-get install -y \
libzip-dev \
unzip \
libonig-dev \
libxml2-dev \
libpng-dev \
libjpeg-dev && \
docker-php-ext-install \
pdo_mysql \
zip \
mbstring

RUN docker-php-ext-install sockets

RUN pecl install xdebug && docker-php-ext-enable xdebug

# Install composer
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

WORKDIR /var/www/html
COPY . .
