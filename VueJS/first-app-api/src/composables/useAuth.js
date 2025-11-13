import { useRouter } from 'vue-router'

import { ref, computed } from 'vue'
import api, { setAuthHeader, clearAuthHeader } from '@/api/api'
import { useToast } from 'vue-toastification'

const tokenKey = 'access_token'
const toast = useToast()

const token = ref(localStorage.getItem(tokenKey) || null)

if (token.value) {
  setAuthHeader(token.value)
}

export function useAuth() {
  const router = useRouter()

  const isAuthenticated = computed(() => !!token.value)

  async function login(email, password = true) {
    const params = new URLSearchParams()
    params.append('username', email)
    params.append('password', password)

    const response = await api.post('/auth/token', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    const accessToken = response.data?.access_token
    if (!accessToken) {
      throw new Error('No access token in response')
    }
    token.value = accessToken
    localStorage.setItem(tokenKey, accessToken)
    setAuthHeader(accessToken)
    return response.data
  }

  async function register(...args) {
    let payload = {}

    if (args.length === 1 && typeof args[0] === 'object') {
      const obj = args[0]
      payload = {
        email: obj.email,
        password: obj.password,
        first_name: obj.firstName ?? obj.first_name ?? undefined,
        last_name: obj.lastName ?? obj.last_name ?? undefined,
      }
    } else {
      const [email, password, firstName, lastName] = args
      payload = {
        email,
        password,
        first_name: firstName ?? undefined,
        last_name: lastName ?? undefined,
      }
    }

    if (payload.first_name === undefined) delete payload.first_name
    if (payload.last_name === undefined) delete payload.last_name

    try {
      const res = await api.post('/auth/register', payload)
      return res.data
    } catch (err) {
      const msg =
        err?.response?.data?.detail ||
        err?.response?.data?.message ||
        err.message ||
        'Registration failed'
      throw new Error(msg)
    }
  }

  function logout() {
    token.value = null
    localStorage.removeItem(tokenKey)
    clearAuthHeader()
    toast.success('Logged out successfully.')
    router.push('/login').catch(() => {})
  }

  return {
    isAuthenticated,
    login,
    register,
    logout,
  }
}
