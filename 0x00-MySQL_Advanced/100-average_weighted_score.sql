-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input: 

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;
	DECLARE weighted_score FLOAT DEFAULT 0;

	SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
	INTO total_score, total_weight
	FROM corrections
	INNER JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;


	IF total_weight IS NOT NULL THEN
		SET weighted_score = total_score / total_weight;
	END IF;


	UPDATE users SET average_score = weighted_score WHERE id = user_id;
END //

DELIMITER ;
