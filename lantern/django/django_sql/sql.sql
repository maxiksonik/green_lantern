CREATE TABLE Restaurant(
    Restaurant_ID int PRIMARY KEY,
    NAME char(30) NOT NULL,
    Address char(50),
    City_ID int,
    FOREIGN KEY(City_ID) REFERENCES City(City_ID) NOT NULL
);

CREATE TABLE City(
    City_ID int PRIMARY KEY,
    Name varchar(30) NOT NULL,
    Country_ID int,
    FOREIGN KEY(Country_ID) REFERENCES Country(Country_ID) NOT NULL
);

CREATE TABLE Country(
    Country_ID int PRIMARY KEY,
    Name varchar(30) NOT NULL
);

CREATE TABLE Staff(
    Staff_ID int PRIMARY KEY,
    First_name varchar(25) NOT NULL,
    Last_name varchar(25) NOT NULL,
    Age int,
    Address varchar(50),
    Salary float NOT NULL,
    Phone_number varchar(13),
    Restaurant_ID int NOT NULL,
    FOREIGN KEY (Restaurant_ID) REFERENCES Restaurant(Restaurant_ID) NOT NULL
);

CREATE TABLE Dish(
    Dish_ID int PRIMARY KEY,
    Name varchar(30) NOT NULL,
    Menu_id int NOT NULL,
    Price float NOT NULL,
);

CREATE TABLE Menu(
    Menu_ID int PRIMARY KEY,
    NAME char(6) NOT NULL,
    Restaurant_ID int,
    FOREIGN KEY (Restaurant_ID) REFERENCES Restaurant(Restaurant_ID) NOT NULL
);

CREATE TABLE Menu_Dish(
    Menu_ID int NOT NULL,
    Dish_ID int NOT NULL,
    FOREIGN KEY (Menu_ID) REFERENCES Menu(Menu_ID) NOT NULL,
    FOREIGN KEY (Dish_ID) REFERENCES Dish(Dish_ID) NOT NULL
);

CREATE INDEX ixName on staff(First_name);
