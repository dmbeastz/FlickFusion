import React, { useState, useEffect } from "react";

function App() {
  const [flicks, setFlicks] = useState([]);

  useEffect(() => {
    fetch("/flicks")
      .then((res) => res.json())
      .then((data) => {
        setFlicks(data.flick);
        console.log(data);
      })
      .catch((error) => {
        console.error("Error fetching flicks:", error);
      });
  }, []);

  return (
    <div>
      {flicks.map((flick, i) => (
        <p key={i}>{flick}</p>
      ))}
    </div>
  );
}

export default App;
