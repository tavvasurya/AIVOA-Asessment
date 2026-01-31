import React, { useState } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { setResponse } from "../redux/interactionSlice";

export default function LogInteractionForm() {
  const dispatch = useDispatch();
  const response = useSelector((state) => state.interaction.response);

  const [hcpName, setHcpName] = useState("");
  const [interactionType, setInteractionType] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const submitHandler = async () => {
    try {
      setLoading(true);
      const res = await axios.post("/log-interaction", {
        hcp_name: hcpName,
        interaction_type: interactionType,
        summary: summary,
      });
      dispatch(setResponse(res.data));
    } catch (error) {
      dispatch(
        setResponse({
          error: "Request failed",
          details: error.message,
        })
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Log HCP Interaction</h2>

      <input
        placeholder="HCP Name"
        value={hcpName}
        onChange={(e) => setHcpName(e.target.value)}
      />
      <br />

      <input
        placeholder="Interaction Type"
        value={interactionType}
        onChange={(e) => setInteractionType(e.target.value)}
      />
      <br />

      <textarea
        placeholder="Summary"
        value={summary}
        onChange={(e) => setSummary(e.target.value)}
      />
      <br />

      <button onClick={submitHandler} disabled={loading}>
        {loading ? "Submitting..." : "Submit"}
      </button>

      {/* 🔹 SHOW RESPONSE */}
      {response && (
        <div style={{ marginTop: "20px" }}>
          <h3>AI Response</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
