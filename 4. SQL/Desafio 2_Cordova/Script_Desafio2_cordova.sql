-- Desafio 2
-- Constanza Córdova


-- 1. Creación de base de datos 
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
año int not null,
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
-- Nota: se realizó la importación de los datos desde los archivos csv por medio de import data de DBeaver 

-- 4. Canciones que salieron el año 2018
select cancion.titulo_cancion, cancion.artista, album.año 
from cancion 
inner join album 
on cancion.album=album.titulo_album where año=2018;

-- 5. Albums y nacionalidad de su artista
select album.titulo_album, artista.nacionalidad 
from album
inner join artista 
on album.artista=artista.nombre_artista; 


-- 6. Número de track, canción, album, año de lanzamiento y artista 
-- ordenadas por año de lanzamiento de album, album y artista 
select cancion.numero_del_track, cancion.titulo_cancion, album.titulo_album, album.año, album.artista 
from cancion
inner join album 
on cancion.album=album.titulo_album 
order by album.año, album.titulo_album, album.artista;