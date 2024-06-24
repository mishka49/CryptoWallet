import './App.css';
import Navbar from './components/navbar/navbar'

import HomePage from './pages/home_page'
import WalletsPage from './pages/wallets_page'
import TransactionsPage from './pages/transactions_page'

import {Routes, Route, Link} from 'react-router-dom'
import HistoryPage from "./pages/history_page";
import SignUpPage from "./pages/signup_page";
import SignInPage from "./pages/signin_page";
import {useState} from "react";
import ProtectedRoute from "./routes/protectedRoutes";
import LogoutPage from "./pages/logout_page";

function App() {
    return (
        <>
            <div className="App">
                <Navbar/>
            </div>

            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/Wallets"
                       element={<ProtectedRoute element={<WalletsPage/>}/>}/>
                <Route path="/Transaction"
                       element={<ProtectedRoute element={<TransactionsPage/>}/>}/>
                <Route path="/History"
                       element={<ProtectedRoute element={<HistoryPage/>}/>}/>
                <Route path="/SignUp" element={<SignUpPage/>}/>
                <Route path="/SignIn" element={<SignInPage/>}/>
                <Route path="/Logout" element={<LogoutPage redirect={<SignInPage/>}/>}/>
            </Routes>
        </>
    );
}

export default App;
