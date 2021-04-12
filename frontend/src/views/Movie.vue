<template>
    <div>
        <NavBar/>
        <div class="container">
            <div class="pt-4"><b-button type="is-primary" @click="login" style="background-color:#990033; float:right">Add Movie</b-button></div>
            <div class="center" v-if="!movies.length">
                <img alt="Vue logo" src="../assets/movies.png" style="height:120px"/>
                <p style="color:#990033" class="has-text-weight-bold is-capitalized is-size-4">No Movies Available</p>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar";

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
        methods: {
            // Log the user out
            logout() {
                this.$auth.logout({
                    returnTo: window.location.origin
                });
            }
        }
    }
</script>

<style scoped>
.center {
    padding: 150px 0;
}
</style>