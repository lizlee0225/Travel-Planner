-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists travelers;
create table travelers (
	name text primary key,
	email text not null
);

drop table if exists travels;
create table travels (
	travel_id integer primary key,
	trip_name text not null,
	destination text not null,
	name text,
	FOREIGN KEY (name) REFERENCES travelers(name)
);
