import React, { useContext, useState } from "react";

import { UserContext } from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Register = () =>{
    const[name, setName] = useState("");
    const[email, setEmail] = useState("");
    const[country, setCountry] = useState("");
    const[state, setState] = useState("");
    const[city, setCity] = useState("");
    const[postal_code, setPostalCode] = useState("");
    const[street, setStreet] = useState("");
    const[number, setNumber] = useState("");
    const[complement, setComplement] = useState("");
    const[cpf, setCPF] = useState("");
    const[pis, setPIS] = useState("");
    const[password, setPassword] = useState("");

    const[errorMessage, setErrorMessage] = useState("");
    const[, setToken] = useContext(UserContext);

    const submitRegister = async () => {
        const requestOptions ={
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name: name, email: email,
            country: country, state: state, city: city,
            postal_code: postal_code, street: street, number: number,
            complement: complement, CPF: cpf, PIS: pis,
            hashed_password: password}),
        };

        const response = await fetch("/api/user", requestOptions);
        const data = await response.json();

        if(!response.ok){
            setErrorMessage(data.detail);
        }else{
            setToken(data.access_token);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if(password.length >= 8){
            submitRegister();
        }else{
            setErrorMessage("Certifique-se de que a senha tenha mais de 8 caracteres")
        }
    };

    return(
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">Cadastro</h1>
                
                <div className="field">
                    <label className="label">Nome</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="Nome" value={name}
                        onChange={(e) => setName(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                        <input type="email" className="input" 
                        placeholder="Email" value={email}
                        onChange={(e) => setEmail(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">País</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="País" value={country}
                        onChange={(e) => setCountry(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Estado</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="Estado" value={state}
                        onChange={(e) => setState(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Cidade</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="Cidade" value={city}
                        onChange={(e) => setCity(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">CEP</label>
                    <div className="control">
                        <input type="number" className="input"
                        placeholder="CEP" value={postal_code}
                        onChange={(e) => setPostalCode(e.target.value)} 
                        // required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Rua</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="Rua" value={street}
                        onChange={(e) => setStreet(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Número</label>
                    <div className="control">
                        <input type="number" className="input"
                        placeholder="Numero" value={number}
                        onChange={(e) => setNumber(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Complemento</label>
                    <div className="control">
                        <input type="text" className="input" 
                        placeholder="Complemento" value={complement}
                        onChange={(e) => setComplement(e.target.value)} 
                        // required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">CPF</label>
                    <div className="control">
                        <input type="number" className="input"
                        placeholder="CPF" value={cpf}
                        onChange={(e) => setCPF(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">PIS</label>
                    <div className="control">
                        <input type="number" className="input"
                        placeholder="PIS" value={pis}
                        onChange={(e) => setPIS(e.target.value)} 
                        required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Senha</label>
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
                        Cadastrar
                    </button>
                </div>
            </form>
        </div>
    );
};

export default Register;