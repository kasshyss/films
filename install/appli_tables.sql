

CREATE TABLE creators(
	creator_id serial primary key
	,creator_name VARCHAR(35)
	,creator_birth DATE
	,creator_death DATE
);
CREATE TABLE films(
	film_id serial primary key
	,name VARCHAR(140)
	,creation_date DATE
	,resume VARCHAR(500)
);
CREATE TABLE note(
	note_id serial primary key
	,note_by VARCHAR(40)
	,final_note INTEGER
	,art INTEGER
	,story INTEGER
	,fun INTEGER
	,fk_film INT REFERENCES films(film_id)
);
CREATE TABLE films_creators(
	creator_id INT REFERENCES creators(creator_id)
	,film_id INT REFERENCES films(film_id)
);
CREATE TABLE ref_nationality(
	nat_id serial primary key 
	,nat_label VARCHAR(40)
);
CREATE TABLE creators_nationality(
	creator_id INT REFERENCES creators(creator_id)
	,nat_id INT REFERENCES ref_nationality(nat_id)
);
