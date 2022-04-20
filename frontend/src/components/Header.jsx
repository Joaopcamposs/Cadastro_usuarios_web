import React, { useContext } from "react";

import { UserContext } from "../context/UserContext";

const Header = () => {
    const [token, setToken] = useContext(UserContext);

    const handleLogout = () => {
        setToken(null);
    }

    return(
        !token ?
        <div className="has-text-centered m-6">
            <h1 className="title">Olá Visitante</h1>
            {token && (
            <button className="button" onClick={handleLogout}>
                Logout
            </button>)}
        </div>
        :
        <div className="has-text-centered m-6">
            {token && (
            <button className="button" onClick={handleLogout}>
                Logout
            </button>)}
        </div>
    );
};

export default Header;

