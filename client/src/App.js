import React, { useState, useEffect } from "react";

function App() {
  const [movies, setMovies] = useState([]);
  const [series, setSeries] = useState([]);

  useEffect(() => {
    // Fetch movies
    fetch("/movies")
      .then((res) => res.json())
      .then((data) => {
        setMovies(data); // Set the fetched movies
      })
      .catch((error) => {
        console.error("Error fetching movies:", error);
      });

    // Fetch series
    fetch("/series")
      .then((res) => res.json())
      .then((data) => {
        setSeries(data); // Set the fetched series
      })
      .catch((error) => {
        console.error("Error fetching series:", error);
      });
  }, []);

  return (
    <div>
      <h2>Movies</h2>
      <div>
        {movies.map((movie, i) => (
          <p key={i}>{movie.title}</p>
        ))}
      </div>
      <h2>Series</h2>
      <div>
        {series.map((serie, i) => (
          <p key={i}>{serie.title}</p>
        ))}
      </div>
    </div>
  );
}

export default App;
