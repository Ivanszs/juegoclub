CREATE DATABASE IF NOT EXISTS juegoclub;
USE juegoclub;

CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    telefono VARCHAR(30)
);

CREATE TABLE juego (
    id_juego INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    categoria VARCHAR(40) NOT NULL,
    precio_dia FLOAT NOT NULL
);

CREATE TABLE alquiler (
    id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_juego INT NOT NULL,
    dias INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_juego) REFERENCES juego(id_juego)
);

INSERT INTO cliente (nombre, apellido, dni, telefono) VALUES
('Juan', 'Perez', '38123456', '1145678901'),
('Maria', 'Gomez', '40987654', '1156781234');

INSERT INTO juego (nombre, categoria, precio_dia) VALUES
('Monopoly', 'Estrategia', 1500),
('TEG', 'Estrategia', 1200),
('Uno', 'Cartas', 600);

INSERT INTO alquiler (id_cliente, id_juego, dias) VALUES
(1, 1, 3);
