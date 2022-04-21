import React, {useContext, useEffect, useState} from "react";
import { UserContext } from "../context/UserContext";
import EditUser from "./EditUser";
import ErrorMessage from "./ErrorMessage";


const User = () =>{
    const [token] = useContext(UserContext);
    const [user, setUser] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [loaded, setLoaded] = useState("");
    const [editUser, setEditUser] = useState("");
    
    const getUser = async () => {
        const requestOptions ={
            method: "GET",
            headers: {
                "accept": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch("/api/users/me", requestOptions);
        const data = await response.json();
        if(!response.ok){
            setErrorMessage("Algo deu errado. Não foi possível carregar os dados do usuário");
        }else{
            setUser(data);
            setLoaded(true);
            setEditUser(false);
        }
    };

    useEffect(() =>{
        getUser();
    }, []);

    return(
        <>
            <ErrorMessage message={errorMessage}/>
            {loaded && user ? (
                !editUser ? (
                <div className="columns">
                    <div className="column is-tow-third">
                        <h1 className="title">Olá {user.name}</h1>
                    </div>
                    <div className="column is-one-third">
                        <button className="button is-danger" 
                        onClick={() => {setEditUser(true)}}>Editar Usuário</button>
                    </div>      
                </div>
                ) : <EditUser/>   
            ) : 
            <p>Carregando...</p>
            }
        </>
    )
};

export default User;