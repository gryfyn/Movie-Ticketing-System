import React, { useState, useEffect } from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import YouTube from 'react-youtube';
import './HomePage.css';
import supabase from '../../supabaseClient';
import { Link } from 'react-router-dom';
import Footer from '../utils/footer/Footer';
import Header from '../utils/header/Header';

const HomePage = () => {
  const [isOverlayVisible, setOverlayVisible] = useState(false);
  const [trailerId, setTrailerId] = useState('');
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const { data, error } = await supabase.from('movies').select('*');
      if (error) {
        console.error('Error fetching movies:', error.message);
      } else {
        setMovies(data);
      }
    };

    fetchMovies();
  }, []);

  const getYouTubeVideoId = (url) => {
    const regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  };

  const handleWatchTrailerClick = (url) => {
    const videoId = getYouTubeVideoId(url);
    if (videoId) {
      setTrailerId(videoId);
      setOverlayVisible(true);
    } else {
      console.error('Invalid YouTube URL');
    }
  };

  const handleCloseOverlay = () => {
    setOverlayVisible(false);
    setTrailerId('');
  };

  return (
    <div className="homepage" data-testid="homepage">
      <Header />

      <main className="main-content">
        <div className="featured-movie">
          <Carousel
            autoPlay={true}
            infiniteLoop={true}
            showThumbs={false}
            showArrows={false}
            showIndicators={false}
            showStatus={false}
            className="carousel"
          >
            {movies.map((movie, index) => (
              <div key={index} className="carousel-item">
                <img src={movie.backdropimg} alt={movie.title} className="featured-image" />
                <div className="movie-info">
                  <h1 style={{color: '#FFE1E9'}}>{movie.title}</h1>
                  <p style={{color: '#FFE1E9'}}>{movie.release_date} | {movie.duration} | {movie.genre ? movie.genre.join(', ') : ''}</p>
                  <button
                    className="watch-trailer"
                    onClick={() => handleWatchTrailerClick(movie.trailer_id)}
                    data-testid="trailer"
                  >
                    Watch Trailer
                  </button>
                </div>
              </div>
            ))}
          </Carousel>
        </div>

        <section className="movies-section">
          <h2>Latest Movies</h2>
          <div className="movies-list">
            {movies.map((movie, index) => (
              <Link
                to={`/movie/${movie.id}`}
                key={index}
                className="movie-item"
                style={{ textDecoration: 'none' }}
              >
                <img src={movie.image} alt={movie.title} />
                <p style={{ fontSize: '1.05em', textAlign: 'left', margin: '0', color: '#FFE1E9'}}>
                  {movie.title}
                </p>
              </Link>
            ))}
          </div>
        </section>

        <section className="movies-section">
          <h2>Blockbusters</h2>
          <div className="movies-list">
            {movies.map((movie, index) => (
              <Link 
                to={`/movie/${movie.id}`}
                key={index}
                className="movie-item"
                style={{ textDecoration: 'none' }}
              >
                <img src={movie.image} alt={movie.title} />
                <p style={{ fontSize: '1.05em',  textAlign: 'left', margin: '0', color: '#FFE1E9'}}>
                  {movie.title}
                </p>
              </Link>
            ))}
          </div>
        </section>
      </main>

      {isOverlayVisible && (
        <div className="overlay">
          <div className="overlay-content">
            <button className="close-button" onClick={handleCloseOverlay}>X</button>
            <YouTube
              videoId={trailerId}
              className="trailer-video"
              
              opts={{
                playerVars: {
                  autoplay: 1,
                },
              }}
            />
          </div>
        </div>
      )}

      <Footer />
    </div>
  );
};

export default HomePage;


//chaos is the normal state of things
//time kills all