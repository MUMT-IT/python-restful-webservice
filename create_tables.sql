CREATE TABLE item_code
(
    item_id serial,
    display_code varchar(13),
    group_class varchar(4),
    type varchar(3),
    description varchar(4),
    CONSTRAINT item_pk PRIMARY KEY(item_id)
);