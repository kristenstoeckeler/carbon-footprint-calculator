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
	-- Skip seeding during early DB init if Django tables are not created yet.
	IF to_regclass('public.footprints_lifestyle') IS NULL
	   OR to_regclass('public.footprints_choice') IS NULL THEN
		RAISE NOTICE 'Skipping footprint seed data: tables not found yet.';
		RETURN;
	END IF;

	-- Seed lifestyles (idempotent).
	INSERT INTO footprints_lifestyle (name)
	SELECT 'Transportation'
	WHERE NOT EXISTS (
		SELECT 1 FROM footprints_lifestyle WHERE name = 'Transportation'
	);

	INSERT INTO footprints_lifestyle (name)
	SELECT 'Food'
	WHERE NOT EXISTS (
		SELECT 1 FROM footprints_lifestyle WHERE name = 'Food'
	);

	INSERT INTO footprints_lifestyle (name)
	SELECT 'Home Energy'
	WHERE NOT EXISTS (
		SELECT 1 FROM footprints_lifestyle WHERE name = 'Home Energy'
	);

	-- Seed choices (upsert by unique choice name).
	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'Commute by bus', 12, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Transportation'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;

	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'Commute by car', 28, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Transportation'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;

	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'Plant-based meal', 6, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Food'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;

	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'Beef meal', 27, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Food'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;

	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'LED lighting', 4, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Home Energy'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;

	INSERT INTO footprints_choice (name, carbon, lifestyle_id)
	SELECT 'High AC usage', 22, l.id
	FROM footprints_lifestyle l
	WHERE l.name = 'Home Energy'
	ON CONFLICT (name)
	DO UPDATE SET
		carbon = EXCLUDED.carbon,
		lifestyle_id = EXCLUDED.lifestyle_id;
END
$$;

