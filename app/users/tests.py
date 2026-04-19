import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_user_str_returns_name():
	user = User.objects.create(name="Kristen")
	assert str(user) == "Kristen"


@pytest.mark.django_db
def test_home_route_renders_register_template(client):
	response = client.get(reverse("home"))
	assert response.status_code == 200
	assert "users/register.html" in [t.name for t in response.templates if t.name]


@pytest.mark.django_db
def test_register_post_redirects_to_login(client):
	response = client.post(
		reverse("register"),
		{
			"username": "demo_user",
			"password": "secret123",
			"firstname": "Demo",
			"lastname": "User",
			"email": "demo@example.com",
		},
	)
	assert response.status_code == 302
	assert response.url == reverse("login")


@pytest.mark.django_db
def test_login_route_loads(client):
	response = client.get(reverse("login"))
	assert response.status_code == 200
