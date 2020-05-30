DROP TABLE Avocado;
DROP TABLE Prices;
DROP TABLE DATE_t;


CREATE TABLE Avocado(
id NUMBER NOT NULL PRIMARY KEY
);

CREATE TABLE Prices(
id NUMBER NOT NULL PRIMARY KEY,
avgprice NUMBER NOT NULL);

CREATE TABLE DATE_t(
id NUMBER NOT NULL PRIMARY KEY,
month char(10) NOT NULL);

CREATE TABLE Regions(
id NUMBER NOT NULL PRIMARY KEY,
region char(20) NOT NULL);


ALTER TABLE Prices ADD CONSTRAINT price_fk FOREIGN KEY(id) REFERENCES Avocado(id);
ALTER TABLE DATE_t ADD CONSTRAINT month_fk FOREIGN KEY(id) REFERENCES Avocado(id);
ALTER TABLE Regions ADD CONSTRAINT region_fk FOREIGN KEY(id) REFERENCES Avocado(id);