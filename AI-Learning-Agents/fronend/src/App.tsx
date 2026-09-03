import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [provider, setProvider] = useState("gemini");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const sendMessage = async () => {
    if (!message.trim() || loading) return;

    setLoading(true);
    setResponse("");
    setError("");

    try {
      const result = await axios.get(
        "http://127.0.0.1:8000/chat",
        {
          params: {
            message,
            provider,
          },
        }
      );

      setResponse(result.data.response);
      setMessage("");

    } catch (error) {
      console.error(error);

      if (axios.isAxiosError(error)) {
        if (error.response) {
          const apiError = error.response.data?.error;

          if (apiError) {
            setError(
              `${apiError.message}\n\n` +
              `Error Code: ${apiError.error_code}\n` +
              `Error ID: ${apiError.error_id}`
            );
          } else {
            setError(
              error.response.data?.detail ||
              "Something went wrong while processing your request."
            );
          }
        } else if (error.request) {
          setError(
            "Unable to connect to the server. Please check if the backend is running."
          );
        } else {
          setError(
            "Unable to send the request. Please try again."
          );
        }
      } else {
        setError(
          "An unexpected error occurred. Please try again."
        );
      }
    } finally {
      setLoading(false);
    }
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

      <p>
        Choose an AI provider and ask the Agent a question.
      </p>

      <label>
        AI Provider:
      </label>

      <select
        value={provider}
        onChange={(e) => setProvider(e.target.value)}
        disabled={loading}
        style={{
          marginLeft: "10px",
          padding: "8px",
        }}
      >
        <option value="gemini">Google Gemini</option>
        <option value="openai">OpenAI</option>
        <option value="claude">Anthropic Claude</option>

        {/* Temporary option for testing backend error handling */}
        <option value="invalid">Invalid Provider - Test Error</option>
      </select>

      <br />
      <br />

      <input
        style={{
          width: "100%",
          padding: "12px",
          fontSize: "16px",
          boxSizing: "border-box",
        }}
        placeholder="Try: Calculate 125 + 350"
        value={message}
        disabled={loading}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />

      <br />
      <br />

      <button
        onClick={sendMessage}
        disabled={loading}
        style={{
          padding: "10px 20px",
          cursor: loading ? "not-allowed" : "pointer",
        }}
      >
        {loading ? "Thinking..." : "Send"}
      </button>

      <hr />

      {/* Error Notification */}
      {error && (
        <div
          style={{
            backgroundColor: "#ffe5e5",
            border: "1px solid #ff9999",
            padding: "12px",
            borderRadius: "8px",
            marginBottom: "15px",
            whiteSpace: "pre-wrap",
          }}
        >
          ⚠️ {error}
        </div>
      )}

      <h3>AI Response</h3>

      <div
        style={{
          border: "1px solid #ddd",
          padding: "15px",
          borderRadius: "8px",
          minHeight: "80px",
        }}
      >
        {loading
          ? "🤔 Agent is thinking..."
          : response || "No response yet..."}
      </div>
    </div>
  );
}

export default App;