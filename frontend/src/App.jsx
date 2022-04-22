import React, { useContext, useEffect, useState } from "react";
import Register from "./components/Register";
import Login from "./components/Login";
import Header from "./components/Header";
import User from "./components/User";
import { UserContext } from "./context/UserContext";

const App = () => {
  const [token] = useContext(UserContext);
  const [register, setRegister] = useState("");

  return (
    <>
      <Header/>
        <div className="columns">
          <div className="column"></div>
          <div className="column m-5 is-one-third">
            {
              // if user not logged
              !token ? (
                <div className="rows has-text-centered">
                  <div className="columns is-centered">
                    <button className="button is-info"
                    onClick={() => setRegister(false)}
                    style={{width: "102px"}}
                    >Entrar</button>
                    <button className="button is-danger"
                    onClick={() => setRegister(true)}
                    style={{width: "102px"}}
                    >Cadastrar</button>
                  </div>
                  { !register ? <Login/> : <Register/> }
                </div>
              ) : 
                // <p>User logged</p>
                <User/>
            }
          </div>
          <div className="column"></div>
        </div>
    </>
  );
}

export default App;
