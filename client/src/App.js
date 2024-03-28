import React, { useState, useEffect } from "react";

function App() {
  const [flicks, setFlicks] = useState([]);

  useEffect(() => {
    fetch("/movies") // Adjust the endpoint here based on your Flask routes
      .then((res) => res.json())
      .then((data) => {
        setFlicks(data); // Set the fetched data directly
        console.log(data);
      })
      .catch((error) => {
        console.error("Error fetching flicks:", error);
      });
  }, []);

  return (
    <div>
      {flicks.map((flick, i) => (
        <p key={i}>{flick.title}</p> {/* Assuming flicks have a 'title' attribute */}
      ))}
    </div>
  );
}

export default App;
