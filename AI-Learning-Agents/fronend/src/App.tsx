import { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");

  const connectBackend = async () => {
    const response = await axios.get("http://127.0.0.1:8000/");
    setMessage(response.data.message);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Learning Agent</h1>
      <button onClick={connectBackend}>Connect Backend</button>

      <h2>{message}</h2>
    </div>
  );
}

export default App;