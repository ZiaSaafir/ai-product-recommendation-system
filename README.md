# AI Product Recommendation System

A full-stack, AI-powered product recommendation platform built with **Django REST Framework** and **React**. The system learns from user interactions — views, clicks, likes, cart actions, and purchases — and delivers personalized recommendations using content similarity and weighted interaction signals.

---

## Table of Contents

- [Project Status](#project-status)
- [Tech Stack](#tech-stack)
- [Recommendation System](#recommendation-system)
- [How It Works](#how-it-works)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Recommendation Roadmap](#recommendation-roadmap)
- [Seed Product Data](#seed-product-data)
- [Running the Backend](#running-the-backend)
- [Running the Frontend](#running-the-frontend)
- [Current Achievement](#current-achievement)
- [Future Improvements](#future-improvements)
- [Purpose](#purpose)
- [License](#license)

---

## Project Status

**Current Milestone:** V2.1 — Content-Based Recommendation System

### Implemented Features

- User registration and authentication
- JWT-based authentication
- Product catalog REST API
- Product detail page
- User interaction tracking
- Interaction weighting system
- TF-IDF text vectorization
- Cosine similarity engine
- Personalized product recommendations
- Normalized recommendation scores (0–100)
- React frontend with Vite
- PostgreSQL database
- Realistic seeded catalog with 23 products

---

## Tech Stack

### Backend

| Technology | Purpose |
| --- | --- |
| Python | Core language |
| Django | Web framework |
| Django REST Framework | REST API |
| Simple JWT | Authentication |
| PostgreSQL | Database |
| scikit-learn | TF-IDF and similarity |

### Frontend

| Technology | Purpose |
| --- | --- |
| React | UI library |
| Vite | Build tool |
| JavaScript | Language |
| CSS | Styling |

---

## Recommendation System

The recommendation engine uses a content-based filtering approach.

Each product is represented by a text blob containing its name, description, category, and brand. This text is vectorized using TF-IDF, and cosine similarity is used to compare products the user has already interacted with against all other products.

Recommendation scores are then weighted by how strongly the user interacted with each product, and normalized to a 0–100 scale.

### Interaction Weights

| Interaction | Weight |
| --- | :---: |
| VIEW | 1 |
| CLICK | 2 |
| LIKE | 3 |
| CART | 4 |
| PURCHASE | 5 |

---

## How It Works
User Interaction
|
v
Interaction History
|
v
Interaction Weight
|
v
Product Text (Name + Description + Category + Brand)
|
v
TF-IDF Vectorization
|
v
Cosine Similarity
|
v
Weighted Recommendation Score
|
v
Personalized Recommendations

text

---

## API Reference

### Authentication

JWT-based authentication is used for protected endpoints.

### Products
GET /api/products/
GET /api/products/<id>/

text

### Interactions

Authenticated users can record: `VIEW`, `CLICK`, `LIKE`, `CART`, `PURCHASE`.
GET /api/interactions/
POST /api/interactions/

text

Example request:

```json
{
    "product": 22,
    "interaction_type": "LIKE"
}
Recommendations
text
GET /api/recommendations/
Example response:

json
{
    "count": 5,
    "results": [
        {
            "id": 20,
            "name": "Sony WH-CH720N",
            "category_name": "Headphones",
            "brand_name": "Sony",
            "recommendation_score": 82.06
        }
    ]
}
Project Structure
text
ai_product_recommendation/
├── backend/
│   ├── apps/
│   │   ├── accounts/
│   │   ├── products/
│   │   ├── interactions/
│   │   └── recommendations/
│   ├── seed_products.py
│   ├── manage.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   ├── css/
│   │   ├── services/
│   │   │   └── api.js
│   │   └── App.jsx
│   └── ...
└── README.md
Recommendation Roadmap
text
V1    Category-Based Recommendation
        |
        v
V2    Content-Based Recommendation
      TF-IDF + Cosine Similarity
        |
        v
V2.1  Interaction Weighting + Score Normalization    <- Current
        |
        v
V2.2  Recommendation Explanations
        |
        v
V3    Collaborative Filtering (KNN)
        |
        v
V4    Hybrid Recommendation System
        |
        v
V5    Evaluation + Recommendation Metrics
        |
        v
V6    Production Optimization
Seed Product Data
The project currently includes 23 realistic products across categories such as laptops, smartphones, monitors, gaming, accessories, headphones, and smartwatches.

Brands include Apple, Samsung, Sony, Logitech, ASUS, Dell, and HP.

The seed script is located at backend/seed_products.py.

On Windows PowerShell, run:

powershell
Get-Content seed_products.py | python manage.py shell
Running the Backend
powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Backend runs at http://127.0.0.1:8000/.

Running the Frontend
powershell
cd frontend
npm install
npm run dev
Frontend runs at http://localhost:5173/.

Current Achievement
The system has been tested with multiple user accounts and produces different recommendation results based on each user's interaction history.

This demonstrates that the recommendation engine is personalized, rather than simply returning the same product list to every user.

Future Improvements
Recommendation explanations

Better recommendation evaluation metrics

Collaborative filtering

KNN-based recommendations

Hybrid recommendation model

Additional interaction signals

Cold-start handling

Recommendation diversity

Performance optimization

Production deployment

Larger product dataset

Purpose
This project is being developed as a practical AI and full-stack engineering project to understand how recommendation systems work from the ground up — starting with interpretable content-based methods and gradually moving toward more advanced recommendation techniques.

License
This project is currently intended for learning, experimentation, and portfolio development.


![alt text](image.png)

![alt text](image-1.png)