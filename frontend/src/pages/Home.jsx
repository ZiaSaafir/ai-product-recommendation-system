
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  getAccessToken,
  getCurrentUser,
  logout,
} from "../services/api";

import "../css/Home.css";

function Home() {
  const [products, setProducts] = useState([]);
  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [recommendations, setRecommendations] = useState([]);
  const [recommendationLoading, setRecommendationLoading] =
    useState(true);

  // =====================================================
  // LOAD PRODUCTS + CURRENT USER
  // =====================================================

  useEffect(() => {
    const loadData = async () => {
      try {
        // Load products
        const response = await fetch(
          "http://127.0.0.1:8000/api/products/"
        );

        if (!response.ok) {
          throw new Error("Could not load products.");
        }

        const data = await response.json();

        setProducts(data.results || []);

        // Load current user
        const token = getAccessToken();

        if (token) {
          const currentUser = await getCurrentUser();
          setUser(currentUser);
        }
      } catch (err) {
        console.error("Home loading error:", err);

        setError(
          err.message || "Something went wrong."
        );
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  // =====================================================
  // LOAD AI RECOMMENDATIONS
  // =====================================================

  useEffect(() => {
    const loadRecommendations = async () => {
      const token = getAccessToken();

      // User is not logged in
      if (!token) {
        setRecommendations([]);
        setRecommendationLoading(false);
        return;
      }

      try {
        const response = await fetch(
          "http://127.0.0.1:8000/api/recommendations/",
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (!response.ok) {
          throw new Error(
            "Could not load recommendations."
          );
        }

        const data = await response.json();

        setRecommendations(data.results || []);
      } catch (err) {
        console.error(
          "Recommendation error:",
          err
        );

        // Don't break the whole homepage
        setRecommendations([]);
      } finally {
        setRecommendationLoading(false);
      }
    };

    loadRecommendations();
  }, [user]);

  // =====================================================
  // LOGOUT
  // =====================================================

  const handleLogout = () => {
    logout();
    setUser(null);
    setRecommendations([]);
  };

  // =====================================================
  // LOADING SCREEN
  // =====================================================

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>

        <p>Loading products...</p>
      </div>
    );
  }

  // =====================================================
  // ERROR SCREEN
  // =====================================================

  if (error) {
    return (
      <div className="error">
        <h2>Oops! Something went wrong</h2>

        <p>{error}</p>

        <button
          onClick={() =>
            window.location.reload()
          }
        >
          Try Again
        </button>
      </div>
    );
  }

  // =====================================================
  // UI
  // =====================================================

  return (
    <div className="home">

      {/* =================================================
          NAVBAR
      ================================================= */}

      <nav className="navbar">

        <Link to="/" className="logo">
          AI<span>Recommend</span>
        </Link>

        <div className="nav-links">

          <Link to="/">Home</Link>

          {user ? (
            <div className="user-menu">

              <span>
                Hello,{" "}
                <strong>
                  {user.first_name ||
                    user.username}
                </strong>
              </span>

              <button
                onClick={handleLogout}
              >
                Logout
              </button>

            </div>
          ) : (
            <div className="auth-menu">

              <Link to="/login">
                Login
              </Link>

              <Link
                to="/register"
                className="btn-register"
              >
                Register
              </Link>

            </div>
          )}

        </div>
      </nav>


      {/* =================================================
          HERO SECTION
      ================================================= */}

      <section className="hero">

        <div className="hero-content">

          <span className="badge">
            ✨ Smart Recommendations
          </span>

          <h1>
            Discover Products
            <br />

            <span>
              You'll Love.
            </span>
          </h1>

          <p>
            Explore amazing products and
            discover personalized recommendations
            based on your interests.
          </p>

          <a
            href="#products"
            className="btn-primary"
          >
            Explore Products
          </a>

        </div>

      </section>


      {/* =================================================
          AI RECOMMENDATIONS
      ================================================= */}

      {user && (
        <section className="recommendations">

          <div className="section-header">

            <div>

              <span className="label">
                AI POWERED
              </span>

              <h2>
                🤖 Recommended For You
              </h2>

              <p className="section-description">
                Products selected based on
                your activity and interests.
              </p>

            </div>

          </div>


          {recommendationLoading ? (

            <div className="recommendation-loading">

              <div className="spinner"></div>

              <p>
                Finding products for you...
              </p>

            </div>

          ) : recommendations.length === 0 ? (

            <div className="recommendation-empty">

              <div className="empty-icon">
                🤖
              </div>

              <h3>
                We're learning your preferences
              </h3>

              <p>
                View, like, add products to your
                cart, or interact with products
                to receive personalized
                recommendations.
              </p>

              <a
                href="#products"
                className="btn-primary"
              >
                Explore Products
              </a>

            </div>

          ) : (
<div className="grid">

  {recommendations.map((product) => {

    const score = Number(
      product.recommendation_score || 0
    );

    const percentage = Math.min(
      Math.round(score * 20),
      99
    );

    return (
      <div
        className="card recommendation-card"
        key={product.id}
      >

        {/* Recommendation badge */}
        <div className="recommendation-badge">
          ✨ Recommended
        </div>


        {/* Product image */}
        <div className="card-image">

          {product.image ? (
            <img
              src={product.image}
              alt={product.name}
            />
          ) : (
            <span>
              No Image
            </span>
          )}

        </div>


        {/* Product information */}
        <div className="card-body">

          <span className="category">
            {product.category?.name ||
              "Product"}
          </span>


          <h3>
            {product.name}
          </h3>


          <p>
            {product.description ||
              "No description available."}
          </p>


          {/* AI match */}
          <div className="ai-match">

            <div className="ai-match-header">

              <span>
                AI Match
              </span>

              <strong>
                {percentage}%
              </strong>

            </div>


            <div className="ai-match-bar">

              <div
                className="ai-match-progress"
                style={{
                  width: `${percentage}%`,
                }}
              ></div>

            </div>

          </div>


          {/* Price + button */}
          <div className="card-footer">

            <strong>
              ${product.price}
            </strong>

            <Link
              to={`/products/${product.id}`}
              className="view-button"
            >
              View
            </Link>

          </div>

        </div>

      </div>
    );
  })}

</div>
          )}

        </section>
      )}


      {/* =================================================
          ALL PRODUCTS
      ================================================= */}

      <section
        id="products"
        className="products"
      >

        <div className="section-header">

          <div>

            <span className="label">
              EXPLORE
            </span>

            <h2>
              Popular Products
            </h2>

          </div>

          <span className="count">
            {products.length} products
          </span>

        </div>


        {products.length === 0 ? (

          <div className="empty">

            <h3>
              No products found
            </h3>

            <p>
              Add some products to your
              database first.
            </p>

          </div>

        ) : (

          <div className="grid">

            {products.map(
              (product) => (

                <div
                  className="card"
                  key={product.id}
                >

                  <div className="card-image">

                    {product.image ? (

                      <img
                        src={product.image}
                        alt={product.name}
                      />

                    ) : (

                      <span>
                        No Image
                      </span>

                    )}

                  </div>


                  <div className="card-body">

                    <span className="category">

                      {product.category?.name ||
                        "Product"}

                    </span>


                    <h3>
                      {product.name}
                    </h3>


                    <p>
                      {product.description ||
                        "No description available."}
                    </p>


                    <div className="card-footer">

                      <strong>
                        ${product.price}
                      </strong>

                      <Link
                        to={`/products/${product.id}`}
                        className="view-button"
                      >
                        View
                      </Link>

                    </div>

                  </div>

                </div>

              )
            )}

          </div>

        )}

      </section>


      {/* =================================================
          FOOTER
      ================================================= */}

      <footer className="footer">

        <p>
          © 2026 AIRecommend — Smart
          Product Discovery
        </p>

      </footer>

    </div>
  );
}

export default Home;

