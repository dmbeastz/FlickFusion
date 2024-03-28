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
      <div>
        <h1>FlickFusion</h1>
      </div>
      <h2>Home</h2>
      <div>
        {movies.map((movie, i) => (
          <div key={i}>
            <p>{movie.title}</p>
            <p>Stars: {movie.stars}</p>
            <p>Year: {movie.year}</p>
            <img src={movie.poster} alt={`Poster for ${movie.title}`} />
          </div>
        ))}
      </div>
      <div>
        {series.map((serie, i) => (
          <div key={i}>
            <p>{serie.title}</p>
            <p>Stars: {serie.stars}</p>
            <p>Year: {serie.year}</p>
            <img src={serie.poster} alt={`Poster for ${serie.title}`} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
