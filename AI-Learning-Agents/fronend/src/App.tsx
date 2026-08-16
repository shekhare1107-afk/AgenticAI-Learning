import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    if (!message.trim()) return;

    const result = await axios.get(
      `http://127.0.0.1:8000/chat`,
      {
        params: {
          message,
        },
      }
    );

    setResponse(result.data.response);
    setMessage("");
  };

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        fontFamily: "Arial",
      }}
    >
      <h1>🤖 AI Learning Agent</h1>

      <input
        style={{
          width: "100%",
          padding: "12px",
          fontSize: "16px",
        }}
        placeholder="Ask something..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br />
      <br />

      <button
        onClick={sendMessage}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        Send
      </button>

      <hr />

      <h3>AI Response</h3>

      <div
        style={{
          border: "1px solid #ddd",
          padding: "15px",
          borderRadius: "8px",
          minHeight: "80px",
        }}
      >
        {response || "No response yet..."}
      </div>
    </div>
  );
}

export default App;