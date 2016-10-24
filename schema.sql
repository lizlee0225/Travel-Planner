-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists travelers;
create table travelers (
	traveler_id integer primary key,
	traveler_name text not null
);

/*drop table if exists names;
create table names (
	name_id integer primary key,
	name text,
	travel_id integer,
	FOREIGN KEY (name) REFERENCES travelers(name),
	FOREIGN KEY (travel_id) REFERENCES travels(travel_id)
);*/

drop table if exists travels;
create table travels (
	travel_id integer primary key,
	trip_name text not null,
	destination text not null,
	friend text,
	traveler_name text,
	FOREIGN KEY (traveler_name) REFERENCES travelers(traveler_name)
);
