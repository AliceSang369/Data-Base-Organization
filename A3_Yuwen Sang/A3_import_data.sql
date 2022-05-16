show databases;
drop database if exists carInsurance;
create database carInsurance;
use carInsurance;

# create 7 tables
#1. Customers
drop table if exists Customers;
create table Customers(
	customerID int NOT NULL,
    cname varchar(30),
    age int,
    gender varchar(10),
    ssn int,
    dlNum int,
    planName varchar(20) NOT NULL,
    cityName varchar(20) NOT NULL,
    primary key (customerID));
describe Customers;

#2. Cars
drop table if exists Cars;
create table Cars(
	VINcode varchar(20) NOT NULL,
    brand varchar(15),
    color varchar(15),
    ctype varchar(10),
    customerID int NOT NULL,
    primary key (VINcode));
describe Cars;

#3. Cities (here we use states instead)
drop table if exists States;
create table States(
    cityName varchar(20) NOT NULL,
    climate varchar(15) NOT NULL,
    pDensity varchar(10) NOT NULL,
    primary key (cityName));
describe Cities;

#4. DrivingRecords
drop table if exists DrivingRecords;
create table DrivingRecords(
    recordID int NOT NULL,
    DRdate varchar(15),
    DRtype varchar(20) NOT NULL,
    customerID int NOT NULL,
    premiumID int NOT NULL,
    primary key (recordID));
describe DrivingRecords;

#5. Coverage
drop table if exists Coverage;
create table Coverage(
	coverageID int NOT NULL,
	cAmount varchar(10) NOT NULL,
    planName varchar(15) NOT NULL,
    price int NOT NULL,
    primary key (coverageID));
describe Coverage;

#6. Premium
drop table if exists Premium;
create table Premium(
	premiumID int NOT NULL,
    paymentPeriod varchar(15),
    cAmount varchar(10) NOT NULL,
    recordID int,
    customerID int NOT NULL,
    primary key (premiumID));
describe Premium;


