select * from bookings;
insert into bookings (customer_id,booking_date,slot_start,slot_end,number_of_people,food_order,total_amount,payment_status,band_color,deleted) values (1,'2025-05-04','18:30:00','19:30:00',2,'nothing',200,'pending','yellow',false); 

select * from group_members;
ALTER TABLE group_members DROP COLUMN group_id;
ALTER TABLE group_members DROP COLUMN band_color;

ALTER TABLE bookings DROP COLUMN group_id;

DELETE FROM bookings;
ALTER SEQUENCE bookings_booking_id_seq RESTART WITH 1;

DELETE FROM group_members;