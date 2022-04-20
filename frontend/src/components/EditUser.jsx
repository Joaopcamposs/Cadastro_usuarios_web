import React, {useContext, useEffect, useState} from "react";
import { UserContext } from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const EditUser= () => {
    const [token, setToken] = useContext(UserContext);
    const [user, setUser] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [loaded, setLoaded] = useState("");

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

    useEffect(() =>{
        getUser();  
    }, []);

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
        setName(data.name);
        setEmail(data.email);
        setCountry(data.country);
        setState(data.state);
        setCity(data.city);
        setPostalCode(data.postal_code);
        setStreet(data.street);
        setNumber(data.number);
        setComplement(data.complement);
        setCPF(data.CPF);
        setPIS(data.PIS);
        if(!response.ok){
            setErrorMessage("Algo deu errado. Não foi possível carregar os dados do usuário.");
        }else{
            setUser(data);
            setLoaded(true);
        }
    };  


    const updateUser = async () => {
        const requestOptions ={
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name: name, email: email,
            country: country, state: state, city: city,
            postal_code: postal_code, street: street, number: number,
            complement: complement, CPF: cpf, PIS: pis,
            hashed_password: password}),
        };

        const response = await fetch(`/api/user/${cpf}`, requestOptions);

        if(!response.ok){
            setErrorMessage("Algo deu errado ao atualizar o usuário");
        }
    };

    const deleteUser = async () => {
        const requestOptions ={
            method: "DELETE",
            headers: {"Content-Type": "application/json"},
        };

        const response = await fetch(`/api/user/${cpf}`, requestOptions);

        if(!response.ok){
            setErrorMessage("Falha ao excluir usuário");
        }
        setToken(null);
    };

    return(
        <>
            <ErrorMessage message={errorMessage}/>
            {loaded && user ? (
                <div className="box">
                <h1 className="title has-text-centered">Editar Cadastro</h1>
                    <section className="">
                        <form>
                            <label className="label">Nome</label>
                            <input type="text" className="input" value={name} 
                            onChange={(e) => setName(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Email</label>
                            <input type="email" className="input" value={email}
                            onChange={(e) => setEmail(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">País</label>
                            <input type="text" className="input" value={country}
                            onChange={(e) => setCountry(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Estado</label>
                            <input type="text" className="input" value={state}
                            onChange={(e) => setState(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Cidade</label>
                            <input type="text" className="input" value={city}
                            onChange={(e) => setCity(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">CEP</label>
                            <input type="number" className="input" value={postal_code}
                            onChange={(e) => setPostalCode(e.target.value)}/>
                            <br/><br/>
                            <label className="label">Rua</label>
                            <input type="text" className="input" value={street}
                            onChange={(e) => setStreet(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Número</label>
                            <input type="number" className="input" value={number}
                            onChange={(e) => setNumber(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Complemento</label>
                            <input type="text" className="input" value={complement}
                            onChange={(e) => setComplement(e.target.value)}/>
                            <br/><br/>
                            <label className="label">CPF</label>
                            <input type="number" className="input" value={cpf}
                            onChange={(e) => setCPF(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">PIS</label>
                            <input type="number" className="input" value={pis}
                            onChange={(e) => setPIS(e.target.value)} required/>
                            <br/><br/>
                            <label className="label">Senha</label>
                            <input type="password" className="input" value={""}
                            onChange={(e) => setPassword(e.target.value)} required/>
                            <br/>
                        </form>
                    </section>
                    
                    <div className="">
                        <br/>
                        <button className="button is-link" 
                        onClick={() => {updateUser()}}>Salvar</button>
                        <button className="button is-danger" 
                        onClick={() => {deleteUser()}} style={{float:"right"}}>Excluir</button>
                    </div>
                </div>
            ) : 
            <p>Carregando...</p>
            }
        </>
    );
}

export default EditUser;