import unittest

from tests.base import BaseTestCase


class UserViewsTests(BaseTestCase):
    # test html login page
    def test_index(self):
        response = self.client.get("/login", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    # test html home page
    def test_home(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.get("/home?username=admin1", content_type="html")
        self.assertEqual(response.status_code, 302)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get("/", follow_redirects=True)
        self.assertIn(b"Please log in to access this page", response.data)

    # Test add list function
    def test_add(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.post(
            "/add",
            data=dict(
                description="test", content="test", deadline="12/12/2019 12:12 AM"
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # test edit function
    def test_edit(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.post(
            "/edit/1",
            data=dict(
                description="test2", content="test2", deadline="12/12/2019 12:12 AM"
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_finish(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.post(
            "/edit/1", data=dict(status=True), follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_share(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.post(
            "/sharing",
            data=dict(emailReceiver="2dowebsite2do@gmail.com", check=[1]),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # test profile function
    def test_profile(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.get("/profile/admin1", content_type="html")
        self.assertEqual(response.status_code, 302)

    # test contact function
    def test_contact(self):
        response = self.client.post(
            "/login",
            data=dict(username="admin1", password="admin2do"),
            follow_redirects=True,
        )
        response = self.client.post(
            "/contact",
            data=dict(
                name="anhle",
                email="minhanh6998@gmail.com",
                subject="aha",
                message="meme",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
