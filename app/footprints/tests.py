import pytest
from django.db import IntegrityError

from footprints.models import Choice, Lifestyle, UserChoice
from users.models import User


@pytest.mark.django_db
def test_lifestyle_str_returns_name():
	lifestyle = Lifestyle.objects.create(name="Transportation")
	assert str(lifestyle) == "Transportation"


@pytest.mark.django_db
def test_choice_str_returns_name():
	lifestyle = Lifestyle.objects.create(name="Food")
	choice = Choice.objects.create(name="Plant-based meal", carbon=6, lifestyle=lifestyle)
	assert str(choice) == "Plant-based meal"


@pytest.mark.django_db
def test_choice_name_is_unique():
	lifestyle = Lifestyle.objects.create(name="Home Energy")
	Choice.objects.create(name="LED lighting", carbon=4, lifestyle=lifestyle)

	with pytest.raises(IntegrityError):
		Choice.objects.create(name="LED lighting", carbon=5, lifestyle=lifestyle)


@pytest.mark.django_db
def test_user_choice_unique_together_constraint():
	user = User.objects.create(name="Alex")
	lifestyle = Lifestyle.objects.create(name="Transportation")
	choice = Choice.objects.create(name="Commute by bus", carbon=12, lifestyle=lifestyle)

	UserChoice.objects.create(user=user, choice=choice)

	with pytest.raises(IntegrityError):
		UserChoice.objects.create(user=user, choice=choice)


@pytest.mark.django_db
def test_footprint_list_api_returns_json(client):
	lifestyle = Lifestyle.objects.create(name="Food")
	Choice.objects.create(name="Beef meal", carbon=27, lifestyle=lifestyle)

	response = client.get("/api/footprints/")

	assert response.status_code == 200
	payload = response.json()
	assert isinstance(payload, list)
	assert payload[0]["name"] == "Beef meal"
	assert payload[0]["lifestyle"]["name"] == "Food"
