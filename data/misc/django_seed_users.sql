SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

DO $$
BEGIN
	-- Skip seeding if Django tables are not created yet.
	IF to_regclass('public.users_user') IS NULL
	   OR to_regclass('public.footprints_choice') IS NULL
	   OR to_regclass('public.footprints_userchoice') IS NULL THEN
		RAISE NOTICE 'Skipping user seed data: tables not found yet.';
		RETURN;
	END IF;

	-- Seed users (idempotent by name).
	INSERT INTO users_user (name)
	SELECT 'Alice Green'
	WHERE NOT EXISTS (
		SELECT 1 FROM users_user WHERE name = 'Alice Green'
	);

	INSERT INTO users_user (name)
	SELECT 'Brandon Lee'
	WHERE NOT EXISTS (
		SELECT 1 FROM users_user WHERE name = 'Brandon Lee'
	);

	INSERT INTO users_user (name)
	SELECT 'Carmen Diaz'
	WHERE NOT EXISTS (
		SELECT 1 FROM users_user WHERE name = 'Carmen Diaz'
	);

	INSERT INTO users_user (name)
	SELECT 'Dev Patel'
	WHERE NOT EXISTS (
		SELECT 1 FROM users_user WHERE name = 'Dev Patel'
	);

	INSERT INTO users_user (name)
	SELECT 'Ella Brooks'
	WHERE NOT EXISTS (
		SELECT 1 FROM users_user WHERE name = 'Ella Brooks'
	);

	-- Seed user choices (idempotent by unique user-choice pair).
	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Commute by bus'
	WHERE u.name = 'Alice Green'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Plant-based meal'
	WHERE u.name = 'Alice Green'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Commute by car'
	WHERE u.name = 'Brandon Lee'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Beef meal'
	WHERE u.name = 'Brandon Lee'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'LED lighting'
	WHERE u.name = 'Carmen Diaz'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Plant-based meal'
	WHERE u.name = 'Carmen Diaz'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'High AC usage'
	WHERE u.name = 'Dev Patel'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Commute by bus'
	WHERE u.name = 'Dev Patel'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'LED lighting'
	WHERE u.name = 'Ella Brooks'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );

	INSERT INTO footprints_userchoice (user_id, choice_id)
	SELECT u.id, c.id
	FROM users_user u
	JOIN footprints_choice c ON c.name = 'Commute by car'
	WHERE u.name = 'Ella Brooks'
	  AND NOT EXISTS (
		SELECT 1
		FROM footprints_userchoice uc
		WHERE uc.user_id = u.id AND uc.choice_id = c.id
	  );
END
$$;