import api from "../api/api";

export async function getProducts() {
  return api.get(`/products`)
}

export async function getProduct(id) {
  return api.get(`/products/${id}`)
}

export async function createProduct(data) {
  return api.post(`/products`, data)
}

export async function updateProduct(id, data) {
  return api.put(`/products/${id}`, data)
}

export async function deleteProduct(id) {
  return api.delete(`/products/${id}`)
}
