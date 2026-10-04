AI Product Recommendation System

A full-stack AI-powered product recommendation system built with Django REST Framework and React. The project learns from user interactions such as views, clicks, likes, cart actions, and purchases, then recommends products based on content similarity and interaction strength.

Project Status

Current milestone: V2.1 — Content-Based Recommendation System

Implemented:

User registration and authentication

JWT authentication

Product catalog API

Product detail page

User interaction tracking

Interaction weighting

TF-IDF text vectorization

Cosine similarity

Personalized product recommendations

Normalized recommendation scores

React frontend

PostgreSQL database

Realistic seeded product catalog with 23 products

Tech Stack

Backend

Python

Django

Django REST Framework

Simple JWT

PostgreSQL

scikit-learn

Frontend

React

Vite

JavaScript

CSS

Recommendation System

The current recommendation engine uses a content-based approach.

Product information such as:

Product name

Description

Category

Brand

is converted into TF-IDF vectors.

Cosine similarity is then used to determine how similar products are to products the user has interacted with.

User interactions are weighted according to their strength:

Interaction

Weight

VIEW

1

CLICK

2

LIKE

3

CART

4

PURCHASE

5

The system uses these weights when calculating personalized recommendation scores.

How It Works

User Interaction
       |
       v
Interaction History
       |
       v
Interaction Weight
       |
       v
Product Text
(Name + Description + Category + Brand)
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

API

Authentication

JWT-based authentication is used for protected endpoints.

Products

GET /api/products/
GET /api/products/<id>/

Interactions

Authenticated users can record:

VIEW
CLICK
LIKE
CART
PURCHASE

Endpoint:

GET  /api/interactions/
POST /api/interactions/

Example:

{
    "product": 22,
    "interaction_type": "LIKE"
}

Recommendations

GET /api/recommendations/

Example response:

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

ai_product_recommendation/
│
├── backend/
│   ├── apps/
│   │   ├── accounts/
│   │   ├── products/
│   │   ├── interactions/
│   │   └── recommendations/
│   │
│   ├── seed_products.py
│   ├── manage.py
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   │
│   │   ├── css/
│   │   ├── services/
│   │   │   └── api.js
│   │   └── App.jsx
│   │
│   └── ...
│
└── README.md

Recommendation Roadmap

The project is being developed progressively:

V1  Category-Based Recommendation
        ↓
V2  Content-Based Recommendation
        ↓
     TF-IDF + Cosine Similarity
        ↓
V2.1 Interaction Weighting + Score Normalization
        ↓
V2.2 Recommendation Explanations
        ↓
V3  Collaborative Filtering
        ↓
    KNN
        ↓
V4  Hybrid Recommendation System
        ↓
V5  Evaluation + Recommendation Metrics
        ↓
V6  Production Optimization

Seed Product Data

The project currently includes 23 realistic products across categories such as:

Laptops

Smartphones

Monitors

Gaming

Accessories

Headphones

Smartwatches

Brands include:

Apple

Samsung

Sony

Logitech

ASUS

Dell

HP

The seed script is located at:

backend/seed_products.py

On Windows PowerShell, it can be executed with:

Get-Content seed_products.py | python manage.py shell

Running the Backend

Go to the backend directory:

cd backend

Activate your virtual environment:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

The backend will normally run at:

http://127.0.0.1:8000/

Running the Frontend

Go to the frontend directory:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

The frontend will normally run at:

http://localhost:5173/

Current Achievement

The system has been tested with multiple user accounts and produces different recommendation results based on each user's interaction history.

This demonstrates that the recommendation engine is personalized rather than simply returning the same product list to every user.

Future Improvements

Planned improvements include:

Recommendation explanations

Better recommendation evaluation

Collaborative filtering

KNN-based recommendations

Hybrid recommendation model

More interaction signals

Cold-start handling

Recommendation diversity

Performance optimization

Production deployment

Larger product dataset

Purpose

This project is being developed as a practical AI/full-stack engineering project to understand how recommendation systems work from the ground up, starting with interpretable content-based methods and gradually moving toward more advanced recommendation techniques.

License

This project is currently intended for learning, experimentation, and portfolio development