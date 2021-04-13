<template>
    <div>
        <NavBar/>
        <div class="container">
            <div class="pt-4" v-if="movies.length">
                <div class="columns" style="float:right"><b-button @click="goToAddMovie()" type="is-primary" style="background-color:#990033">Add Movie</b-button></div>
                <br/>
                <div class="columns is-multiline pt-6">
                    <div v-for="(movie, index) in movies" :key="index" class="column is-3" style="height:400px">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-5by4">
                                <img :src="movie.image_url" alt="Placeholder image">
                                </figure>
                            </div>
                            <div class="card-content">
                                <div class="content">
                                {{movie.title}}
                                <br>
                                <div>{{movie.release_date}}</div>
                                </div>
                            </div>
                            <footer class="card-footer">
                                <a href="#" class="card-footer-item">Edit</a>
                                <a href="#" class="card-footer-item">Delete</a>
                            </footer>
                        </div>
                    </div>
                </div>
            </div>
            <div class="center" v-else>
                <img alt="Vue logo" src="../assets/movies.png" style="height:120px"/>
                <p style="color:#990033" class="has-text-weight-bold is-capitalized is-size-4">No Movies Available</p>
                <b-button @click="goToAddMovie()" type="is-primary" style="background-color:#990033">Add Movie</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar";
    import axios from "axios";
    export default {
        name: 'Movie',
        components: {
            NavBar
        },
        data(){
            return {
                movies: []
            }
        },
        async mounted(){
            await this.getMovies()
        },
        methods: {
            // Log the user out
            logout() {
                this.$auth.logout({
                    returnTo: window.location.origin
                });
                localStorage.removeItem('token')
            },
            goToAddMovie(){
                this.$router.push('/add-movie')
            },
            async getMovies() {
                // Get the access token from the auth wrapper
                const token = await this.$auth.getTokenSilently();

                // Use Axios to make a call to the API
                const { data } = await axios.get("http://127.0.0.1:5000/movies", {
                    headers: {
                    Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
                    }
                });
                
                this.movies = data.movies;
            }
        }
    }
</script>

<style scoped>
    .center {
        padding: 150px 0;
    }
</style>