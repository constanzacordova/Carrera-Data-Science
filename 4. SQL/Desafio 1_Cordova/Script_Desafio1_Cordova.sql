-- Desafio 1
-- Constanza Córdova

-- 1. Crear base de datos biblioteca
create database biblioteca;

-- 2. Crear tabla libro
create table libro(
	id_libro SERIAL primary key,
	nombre_libro VARCHAR(100) not null,
	autor VARCHAR(50) not null,
	genero VARCHAR(50)
);


-- 3. Ingresar libro "Sapo y Sepo" 
-- Definir tabla a la que se insertará los datos
insert into libro 
-- columnas a insertar
(nombre_libro, autor, genero)
-- valores a insertar
values ('Sapo y Sepo', 'Arnold Lobel', 'cuento infantil')

-- 4. Ingresar libro "La Metamorfosis" 
-- Definir tabla a la que se insertará los datos
insert into libro 
-- columnas a insertar
(nombre_libro, autor, genero)
-- valores a insertar
values ('La Metamorfosis', 'Franz Kafka', 'novela')

-- 5. Crear tabla prestamo
create table prestamo(
	id_prestamo SERIAL primary key,
	FK_id_libro int,
	nombre_persona VARCHAR(100) not null,
	fecha_inicio DATE not null,
	fecha_termino DATE not null,
	foreign key (FK_id_libro) references libro(id_libro)
);

-- 6. Insertar columna prestado (booleano) a la tabla libro
alter table libro 
add prestado boolean;

-- 7. Ingresar el estado de prestamo de Sapo y Sepo (id_libro = 1)
-- Se asumen como valor True estado prestado, por lo que se actualizará dicho estado
update libro set prestado=true where id_libro=1


-- 8. Ingresar el estado de prestamo de La Metaforfosis (id_libro = 2)
-- Se asumen como valor True estado prestado, por lo que se actualizará dicho estado
update libro set prestado=true where id_libro=2



-- 9. Ingresar 5 préstamos asociados a Sapo y Sepo
-- prestamo 1
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('1', 'Constanza Cordova', '2020-05-18', '2020-05-21')

-- prestamo 2
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('1', 'Constanza Cordova', '2020-08-10', '2020-08-15')

-- prestamos 3
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('1', 'Marisol Marin', '2020-12-03', '2020-12-10')

-- prestamo 4
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('1', 'Fabian Herrera', '2021-02-06', '2021-02-10')

-- prestamo 5
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('1', 'Gabriela Martinez', '2021-03-18', '2021-03-23')


-- 10. Ingresar 6 préstamos asociados a La Metamorfosis
-- prestamo 1
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Constanza Cordova', '2020-05-18', '2020-05-23')

-- prestamo 2
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Constanza Cordova', '2020-08-09', '2020-08-15')

-- prestamos 3
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Marisol Marin', '2020-12-03', '2020-12-10')

-- prestamo 4
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Fabian Herrera', '2021-02-06', '2021-02-10')

-- prestamo 5
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Gabriela Martinez', '2021-03-18', '2021-03-23')

-- prestamo 6
insert into prestamo (fk_id_libro, nombre_persona, fecha_inicio, fecha_termino)
values ('2', 'Constanza Cordova', '2021-02-18', '2021-02-25')



-- 11. Crear nuevo libro
insert into libro (nombre_libro, autor, genero, prestado)
values ('Data Science for Dummies', 'Lillian Pierson', 'Data Science', False ) 


-- 12. Seleccionar libros y personas quienes pidieron libros prestado 
select libro.nombre_libro, prestamo.nombre_persona from libro
inner join prestamo on libro.id_libro=prestamo.fk_id_libro;

-- 13. Seleccionar todas las columnas de tabla prestamo para el libro sapo y sepo con orden decreciente de fecha_inicio
select * from prestamo 
where fk_id_libro = 1
order by fecha_inicio  desc;

