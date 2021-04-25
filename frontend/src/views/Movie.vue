<template>
    <div>
        <NavBar/>
        <div class="container" style="text-align: center;">
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
                                <div style="color:#990033" class="has-text-weight-semibold">{{movie.title}}</div>
                                <div>{{movie.release_date}}</div>
                                </div>
                            </div>
                            <footer class="card-footer">
                                <a class="card-footer-item" style="color:#990033">Edit</a>
                                <a class="card-footer-item" style="color:#990033" @click="confirm(movie.id)">Delete</a>
                            </footer>
                        </div>
                    </div>
                </div>
            </div>
            <div class="center" v-else>
                <!-- <img alt="Vue logo" src="../assets/movies.png" style="height:120px"/> -->
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
            logout() {
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                this.$auth.logout({
                    returnTo: window.location.origin
                });
            },
            goToAddMovie(){
                this.$router.push('/add-movie')
            },
            async getMovies() {
                    const token = localStorage.getItem('token')

                    const { data } = await axios.get("http://127.0.0.1:5000/movies", {
                        headers: {
                        Authorization: `Bearer ${token}`
                        }
                    });
                    
                    this.movies = data.movies;
            },
            confirm(id) {
                this.$buefy.dialog.confirm({
                    message: 'Are you sure you want to delete this movie?',
                    onConfirm: () => this.deleteMovie(id)
                })
            },
            async deleteMovie(id) {
                axios.delete('http://127.0.0.1:5000/movies/' + id)
                .then(() => {
                    this.getMovies()
                });
            },
        }
    }
</script>

<style scoped>
    .center {
        padding: 150px 0;
    }
    .card {
        height: 100%;
        /* display: flex;
        flex-direction: column */
    }
    /* .card-footer {
        margin-top: auto
    } */
</style>