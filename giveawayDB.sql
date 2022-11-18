CREATE database giveawayDB;
USE giveawayDB;


CREATE table participants(
    participantID int NOT NULL AUTO_INCREMENT,
    participantNAME VARCHAR(60),
    follower int NOT NULL,
    PRIMARY KEY (participantID)
                         );


