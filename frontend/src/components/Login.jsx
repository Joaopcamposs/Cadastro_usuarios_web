import React, {useState, useContext} from "react";
import ErrorMessage from "./ErrorMessage";
import { UserContext } from "../context/UserContext";

const Login = () => {
    const[cpf, setCPF] = useState("");
    const[password, setPassword] = useState("");
    const[errorMessage, setErrorMessage] = useState("");
    const[, setToken] = useContext(UserContext);

    const submitLogin = async () => {
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: JSON.stringify(`grant_type=&username=${cpf}&password=${password}&scope=&client_id=&client_secret=`),
        };

        const response = await fetch("/api/token", requestOptions);
        const data = await response.json();

        if(!response.ok){
            setErrorMessage(data.detail);
        }else{
            setToken(data.access_token);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        submitLogin();
    }

    return(
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">Login</h1>
                <div className="field">
                    <label htmlFor="" className="label">CPF</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="CPF" value={cpf}
                        onChange={(e) => setCPF(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label htmlFor="" className="label">Senha</label>
                    <div className="control">
                        <input type="password" className="input" 
                        placeholder="Senha" value={password}
                        onChange={(e) => setPassword(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <ErrorMessage message={errorMessage}/>
                <br/>
                <div className="has-text-centered">
                    <button className="button is-primary" type="submit">
                        Entrar
                    </button>
                </div>
            </form>
        </div>
    );
};

export default Login;