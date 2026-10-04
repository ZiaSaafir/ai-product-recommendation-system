// src/services/api.js
const API_BASE = "http://127.0.0.1:8000/api";

// ===== TOKEN MANAGEMENT =====
export const getAccessToken = () => localStorage.getItem("access_token");
export const getRefreshToken = () => localStorage.getItem("refresh_token");

export const setTokens = (access, refresh) => {
  localStorage.setItem("access_token", access);
  localStorage.setItem("refresh_token", refresh);
};

export const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  window.location.href = "/login";
};

// ===== AUTH API =====
export const login = async (username, password) => {
  const response = await fetch(`${API_BASE}/auth/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    const data = await response.json();
    throw new Error(data.detail || "Login failed");
  }

  const data = await response.json();
  setTokens(data.access, data.refresh);
  return data;
};

export const register = async (username, email, password) => {
  const response = await fetch(`${API_BASE}/auth/register/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password }),
  });

  if (!response.ok) {
    const data = await response.json();
    throw new Error(data.detail || "Registration failed");
  }

  const data = await response.json();
  // Auto-login after registration
  if (data.access) {
    setTokens(data.access, data.refresh);
  }
  return data;
};

export const getCurrentUser = async () => {
  const response = await fetch(`${API_BASE}/auth/me/`, {
    headers: {
      Authorization: `Bearer ${getAccessToken()}`,
    },
  });

  if (!response.ok) {
    throw new Error("Failed to get user");
  }
  return response.json();
};

export const refreshToken = async () => {
  const response = await fetch(`${API_BASE}/auth/token/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh: getRefreshToken() }),
  });

  if (!response.ok) {
    throw new Error("Failed to refresh token");
  }

  const data = await response.json();
  setTokens(data.access, data.refresh);
  return data;
};

// ===== PRODUCTS API =====
export const getProducts = async () => {
  const response = await fetch(`${API_BASE}/products/`);
  if (!response.ok) throw new Error("Failed to get products");
  return response.json();
};

export const getProduct = async (id) => {
  const response = await fetch(`${API_BASE}/products/${id}/`);
  if (!response.ok) throw new Error("Failed to get product");
  return response.json();
};

// ===== INTERACTIONS API =====
export const getInteractions = async () => {
  const response = await fetch(`${API_BASE}/interactions/`, {
    headers: {
      Authorization: `Bearer ${getAccessToken()}`,
    },
  });
  if (!response.ok) throw new Error("Failed to get interactions");
  return response.json();
};

export const createInteraction = async (data) => {
  const response = await fetch(`${API_BASE}/interactions/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${getAccessToken()}`,
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error("Failed to create interaction");
  return response.json();
};