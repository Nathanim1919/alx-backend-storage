-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students. 

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeIndividualWeightedScoreForUsers;
CREATE PROCEDURE ComputeIndividualWeightedScoreForUsers()
BEGIN
  DECLARE student_id INT;
  DECLARE total_score FLOAT DEFAULT 0;
  DECLARE total_weight FLOAT DEFAULT 0;
  DECLARE weighted_score FLOAT DEFAULT 0;

 
  DECLARE cursor cur_users IS
  SELECT student_id FROM users;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET NOT FOUND = TRUE;

  OPEN cur_users;

  fetch cur_users INTO student_id;

  loop:
    WHILE FOUND DO
      SET total_score = 0;
      SET total_weight = 0;

      SELECT SUM(scores.score * projects.weight), SUM(projects.weight)
      INTO total_score, total_weight
      FROM scores
      INNER JOIN projects ON scores.project_id = projects.id
      WHERE scores.student_id = student_id;  -- Filter by current student

      IF total_weight IS NOT NULL THEN
        SET weighted_score = total_score / total_weight;
      END IF;

      UPDATE users
      SET average_score = weighted_score
      WHERE student_id = student_id;

      FETCH cur_users INTO student_id;
    END LOOP;

  CLOSE cur_users;

  DEALLOCATE cur_users;
END;

DELIMITER ;

