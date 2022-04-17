import React, { useEffect, useState } from "react";

const App = () => {
  const [message, setMessage] = useState("");

  const getWellcomeMessage = async () =>{
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();
    console.log(data);

    if(!response.ok){
      console.log("something messed up");
    }else{
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWellcomeMessage();
  }, []);
  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
}

export default App;
