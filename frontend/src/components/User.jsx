import React, {useContext, useEffect, useState} from "react";
import { UserContext } from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";


const User = () =>{
    const [token] = useContext(UserContext);
    const[user, setUser] = useState("");
    const[errorMessage, setErrorMessage] = useState("");
    const[loaded, setLoaded] = useState("");

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
            setErrorMessage("Something went wrong. Couldn't load user data");
        }else{
            setUser(data);
            setLoaded(true);
        }
    };

    useEffect(() =>{
        getUser();
    }, []);

    return(
        <>
            <ErrorMessage message={errorMessage}/>
            {loaded && user ? (
                <h1 className="title">Hello {user.name}</h1>
            ) : 
            <p>Loading</p>
            }
        </>
    )
};

export default User;