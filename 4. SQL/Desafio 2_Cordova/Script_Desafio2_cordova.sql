-- Desafio 2
-- Constanza C�rdova


-- 1. Creaci�n de base de datos 
create database top_spotify_2018;

-- 2. Crear tablas 
-- tabla artista
create table artista(
nombre_artista VARCHAR(50) not null primary key,
fecha_de_nacimiento DATE not null,
nacionalidad VARCHAR(30)
);


-- tabla album
create table album(
titulo_album VARCHAR(100) not null primary key,
artista VARCHAR(50) not null,
a�o int not null,
foreign key (artista) references artista(nombre_artista)
);


-- tabla cancion
create table cancion(
titulo_cancion VARCHAR(100) not null primary key,
artista VARCHAR(50) not null,
album VARCHAR(100) not null,
numero_del_track int not null,
foreign key (artista) references artista(nombre_artista),
foreign key (album) references album(titulo_album)
);


-- 3. Importar datos
-- Nota: se realiz� la importaci�n de los datos desde los archivos csv por medio de import data de DBeaver 

-- 4. Canciones que salieron el a�o 2018
select cancion.titulo_cancion, cancion.artista, album.a�o 
from cancion 
inner join album 
on cancion.album=album.titulo_album where a�o=2018;

-- 5. Albums y nacionalidad de su artista
select album.titulo_album, artista.nacionalidad 
from album
inner join artista 
on album.artista=artista.nombre_artista; 


-- 6. N�mero de track, canci�n, album, a�o de lanzamiento y artista 
-- ordenadas por a�o de lanzamiento de album, album y artista 
select cancion.numero_del_track, cancion.titulo_cancion, album.titulo_album, album.a�o, album.artista 
from cancion
inner join album 
on cancion.album=album.titulo_album 
order by album.a�o, album.titulo_album, album.artista;