from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession | None:
    try:
        movie = Movie.objects.get(id=movie_id)
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        return MovieSession.objects.create(show_time=movie_show_time,
                                           movie=movie,
                                           cinema_hall=cinema_hall)
    except (Movie.DoesNotExist, CinemaHall.DoesNotExist) as e:
        print(f"Error: {e}")
        return None


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession | None:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        print(f"Error: MovieSession with {movie_session_id} does not exist.")
        return None


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession | None:
    try:
        session = MovieSession.objects.get(id=session_id)
        if show_time:
            session.show_time = show_time
        if movie_id:
            session.movie = Movie.objects.get(id=movie_id)
        if cinema_hall_id:
            session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.save()
        return session
    except MovieSession.DoesNotExist:
        print(f"Error: MovieSession with {session_id} does not exist.")
        return None


def delete_movie_session_by_id(session_id: int) -> None:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
    except MovieSession.DoesNotExist:
        print(f"Error: MovieSession with {session_id} does not exist.")
        return None
