<h1 align="center">Property Management API</h1>

## 🖥️ Tech Stack

**Backend:**

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)&nbsp;
![fastapi](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)&nbsp;
![mongodb](https://img.shields.io/badge/MongoDB-4DB33D?style=for-the-badge&logo=mongodb&logoColor=white)&nbsp;


## 📌 Screenshots:
![all](/img/allAPI.png)
![get](/img/getProperties.png)

## 🛠️ API Endpoints

1. **Create New Property**
    - **Endpoint:** `/properties`
    - **Method:** `POST`
    - **Input:** Property name, address, city, and state.
    - **Output:** List of properties with all details.

2. **Fetch Property Details**
    - **Endpoint:** `/properties/city/{city_name}`
    - **Method:** `GET`
    - **Input:** City name.
    - **Output:** A list of all properties that belong to the city name passed in the input.

3. **Update Property Details**
    - **Endpoint:** `/properties/{property_id}`
    - **Method:** `PUT`
    - **Input:** Property ID, property name, address, city, state.
    - **Output:** Same as create_new_property API with updated information.

4. **Additional APIs (Non-mandatory):**
    - **Find Cities by State**
        - **Endpoint:** `/properties/state/{state_name}`
        - **Method:** `GET`
        - **Input:** State ID or state name.
        - **Output:** All city names that belong to the state.
    - **Find Similar Properties**
        - **Endpoint:** `/properties/similar/{property_id}`
        - **Method:** `GET`
        - **Input:** Property ID.
        - **Output:** List of all properties that belong to the same city as that of given property ID.

<h2>📬 Contact</h2>

If you want to contact me, you can reach me through the below handle.

[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akshat-jaiswal-4664a2197)

© 2024 Akshat Jaiswal

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
