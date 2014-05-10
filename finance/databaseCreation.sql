create database finance;
use finance;
create table company (name varchar(30), symbol varchar(30));

create table industry (name varchar(30));
create table industry (, day_price_change decimal(30, 3), market_cap varchar(30), price_to_earnings_ratio decimal(30, 3), roe_percent decimal(30, 3), div_yield_percent decimal (30, 3), debt_to_equity decimal(30, 3), price_to_book decimal(30, 3), net_profit_margin decimal(30, 3), price_to_free_cash_flow decimal(30, 3));

create table sector (sector varchar(30), day_price_change decimal(30, 3), market_cap varchar(30), price_to_earnings_ratio decimal(30, 3), roe_percent decimal(30, 3), div_yield_percent decimal (30, 3), debt_to_equity decimal(30, 3), price_to_book decimal(30, 3), net_profit_margin decimal(30, 3), price_to_free_cash_flow decimal(30, 3));

alter table company add column `id` int(10) unsigned primary KEY AUTO_INCREMENT;
alter table industry add column `id` int(10) unsigned primary KEY AUTO_INCREMENT;
alter table sector add column `id` int(10) unsigned primary KEY AUTO_INCREMENT;
