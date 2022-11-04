
#`GET` /planets; returns 200 and empty array
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

#`GET` /planets/1 returns a response body that matches our fixture
#check if one planet exists, check that status code == 200


# `GET`/planets/1  with no data in test database (no fixtures) returns 404
def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    # assert response_body == {"message":f"Planet {} not found"}#message for this error

# `GET` /planets with valid data (fixtures), returns 200 and populated array
def test_get_one_planet_with_two_records(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Baby",
        "description": "very smol"
    }

# `POST` /planets with JSON request body, returns 201