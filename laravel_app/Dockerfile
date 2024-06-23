# Laravel Dockerfile
FROM php:7.2-fpm

RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo pdo_sqlite

WORKDIR /var/www

COPY . .
COPY ../sales_data.db /var/www/sales_data.db  # Copy the SQLite database file

RUN composer install

CMD ["php-fpm"]