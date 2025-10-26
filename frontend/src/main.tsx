import React from 'react'
import ReactDOM from 'react-dom/client'
// --- 1. Import using path alias ---
import App from '@/App.tsx'
import '@/index.css'
import { AuthProvider } from '@/AuthContext'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {/* --- 2. Wrap your App component --- */}
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>,
)

