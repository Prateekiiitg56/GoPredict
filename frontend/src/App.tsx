import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { ThemeProvider } from 'next-themes'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
// --- 1. Import your new pages ---
import SignIn from './pages/SignIn'
import SignUp from './pages/SignUp'

function App() {
  const router = createBrowserRouter([
    { path: '/', element: <Home /> },
    
    // --- 2. Add the new routes here ---
    { path: '/sign-in', element: <SignIn /> },
    { path: '/sign-up', element: <SignUp /> },
    
    // Keep NotFound as the last route
    { path: '*', element: <NotFound /> },
  ])
  
  return (
    <ThemeProvider attribute="class" defaultTheme="light" enableSystem>
      <RouterProvider router={router} />
    </ThemeProvider>
  )
}

export default App