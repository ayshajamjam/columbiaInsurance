CREATE TABLE Doctors (
	first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
	job_title VARCHAR(50) NOT NULL,
	degree VARCHAR(3) NOT NULL,
	about TEXT,
	npi CHAR(10),
	photo_link VARCHAR(300),
	avg_rating REAL CHECK (avg_rating >= 0 AND avg_rating <= 5),
	med_university VARCHAR(150),
	students_visited INTEGER CHECK (students_visited >= 0),
	contactno CHAR(10),
	conditions_treated VARCHAR(100) ARRAY[20],
    PRIMARY KEY(npi));

CREATE TABLE Hospitals (
	name VARCHAR(150) NOT NULL,
    address VARCHAR(150) NOT NULL,
	cms CHAR(6),
	contactno CHAR(10),
    PRIMARY KEY(cms));
 
CREATE TABLE StudentPatients (
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    uni VARCHAR(7),
	password VARCHAR(15),
    age INTEGER CHECK(age > 0),
	school VARCHAR(15),
    PRIMARY KEY(uni));

CREATE TABLE Medical_Issues (
	speciality VARCHAR(50),
    description VARCHAR(300),
    PRIMARY KEY(speciality));

CREATE TABLE Reviews (
	review_id INTEGER,
	date_of_visit DATE,
	content VARCHAR(1000),
	rating INTEGER CHECK (rating >= 0 AND rating <= 5),
	PRIMARY KEY (review_id));
 
CREATE TABLE Appointments (
	apt_id INTEGER,
	apt_date DATE NOT NULL,
	apt_time TIME NOT NULL,
	concern_description VARCHAR(300) NOT NULL, 
    PRIMARY KEY(apt_id));
 
CREATE TABLE Saves (
    uni VARCHAR(7),
	npi CHAR(10),
	PRIMARY KEY (uni, npi),
	FOREIGN KEY (uni) REFERENCES StudentPatients
		ON DELETE CASCADE,
	FOREIGN KEY (npi) REFERENCES Doctors
        ON DELETE NO ACTION
        ON UPDATE CASCADE);

CREATE TABLE Specializes_In (
	npi CHAR(10),
	speciality VARCHAR(50),
	PRIMARY KEY (npi, speciality),
	FOREIGN KEY (npi) REFERENCES Doctors
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (speciality) REFERENCES Medical_Issues
        ON UPDATE CASCADE);

CREATE TABLE Works_At (
	npi CHAR(10),
	cms CHAR (6),
	PRIMARY KEY (npi, cms),
	FOREIGN KEY (npi) REFERENCES Doctors,
	FOREIGN KEY (cms) 
        REFERENCES Hospitals);
 
CREATE TABLE Schedules (
    npi CHAR(10),
	cms CHAR (6),
    apt_id INTEGER,
    uni VARCHAR(7),
    PRIMARY KEY(npi, cms, apt_id, uni),
    FOREIGN KEY (npi, cms) REFERENCES Works_At (npi, cms),
    FOREIGN KEY (apt_id) REFERENCES Appointments,
    FOREIGN KEY (uni) REFERENCES StudentPatients
        ON DELETE CASCADE);
  
CREATE TABLE Writes (
	npi CHAR(10),
    uni VARCHAR(7),
    review_id INTEGER NOT NULL,
    date_written DATE NOT NULL,
    PRIMARY KEY (npi, uni),
    FOREIGN KEY (review_id) REFERENCES Reviews
    	ON DELETE CASCADE,
    FOREIGN KEY (npi) REFERENCES Doctors,
    FOREIGN KEY (uni) REFERENCES StudentPatients
    	ON DELETE CASCADE);

CREATE FUNCTION current_date_check ()
RETURNS TRIGGER
AS 
$$
BEGIN 
	IF NEW.apt_date < SYSDATE THEN 
        RAISE EXCEPTION 'Appt date error';
	END IF;
	RETURN NEW;
END

$$ LANGUAGE PLPGSQL;